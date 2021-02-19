package main

import (
	"encoding/json"
	"io"
	"net/http"
	"strconv"

	_ "github.com/go-sql-driver/mysql"
	"github.com/gorilla/mux" // http router package
	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/mysql"
	"github.com/rs/cors"
	log "github.com/sirupsen/logrus" // Logger package
)

// Connect to the database
var db, connErr = gorm.Open("mysql", "root:rpass@/todolist?charset=utf8&parseTime=True&loc=Local")

// TodoItemModel is a blueprint struct used by GORM to make db migrations
type TodoItemModel struct {
	ID          int `gorm:"primary_key"`
	Description string
	Completed   bool
}

// GetItemByID hecks if todo with provided Id exists in the database
func GetItemByID(ID int) bool {
	result := db.First(&TodoItemModel{}, ID)
	if result.Error != nil {
		return false
	}
	return true
}

// GetTodoItems fetches all items matching the search complete criteria requested
func GetTodoItems(status bool) interface{} {
	var todos []TodoItemModel
	TodoItems := db.Where("completed = ?", status).Find(&todos).Value
	return TodoItems
}

// GetCompletedItems return slice of completed todoitems
func GetCompletedItems(w http.ResponseWriter, r *http.Request) {
	log.Info("Get completed items")
	items := GetTodoItems(true)
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(items)
}

// GetUncompletedItems return slice of completed todoitems
func GetUncompletedItems(w http.ResponseWriter, r *http.Request) {
	log.Info("Get uncompleted items")
	items := GetTodoItems(false)
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(items)
}

// DeleteItem removes a todolist item from the db
func DeleteItem(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	id, _ := strconv.Atoi(vars["id"]) // convert string to int
	err := GetItemByID(id)
	if err == false {
		w.Header().Set("Content-Type", "application/json")
		io.WriteString(w, `{"deleted": false, "error": "Record Not Found"}`)
	} else {
		log.WithFields(log.Fields{"Id": id}).Info("Deleting TodoItem")
		todo := &TodoItemModel{}
		db.First(&todo, id)
		db.Delete(&todo)
		w.Header().Set("Content-Type", "application/json")
		io.WriteString(w, `{"deleted": true}`)
	}
}

// UpdateItem updates a todolist item if it exits in the db
func UpdateItem(w http.ResponseWriter, r *http.Request) {
	// Get id of item to update from request
	vars := mux.Vars(r)
	id, _ := strconv.Atoi(vars["id"])

	// Check that item to update exists in DB
	check := GetItemByID(id)
	if check == false {
		w.Header().Set("Content-Type", "application/json")
		io.WriteString(w, `{"updated": false, "error": "Record Not Found"}`)
	} else {
		completed, _ := strconv.ParseBool(r.FormValue("completed"))
		log.WithFields(log.Fields{"Id": id, "Completed": completed}).Info("Updating TodoItem")
		todo := &TodoItemModel{}   // create a model object
		db.First(&todo, id)        // fetch the model with the matching id
		todo.Completed = completed // update the completed field of found obj
		db.Save(&todo)             // save changes
		w.Header().Set("Content-Type", "application/json")
		io.WriteString(w, `{"updated": true }`)
	}
}

// CreateItem fetches todo from http request and persists to database
func CreateItem(w http.ResponseWriter, r *http.Request) {
	description := r.FormValue("description")
	log.WithFields(log.Fields{"description": description}).Info("Saving new TodoItem to database")
	todo := &TodoItemModel{Description: description, Completed: false}
	db.Create(&todo)
	result := db.Last((&todo))
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(result.Value)
}

// healthy responds to requests at /healthy with a API running OK message
func healthy(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode("API is online")
}

func init() {
	log.SetFormatter(&log.TextFormatter{})
	log.SetReportCaller(true)
}

func main() {
	if connErr != nil {
		panic(connErr.Error())
	}

	log.Info("Connected to database.")
	defer db.Close()

	// Run database migrations
	db.Debug().AutoMigrate(&TodoItemModel{})

	log.Info("Starting Todolist API server.....")

	// Register routers
	router := mux.NewRouter()
	router.HandleFunc("/status", healthy).Methods("GET")
	router.HandleFunc("/todo/complete", GetCompletedItems).Methods("GET")
	router.HandleFunc("/todo/incomplete", GetUncompletedItems).Methods("GET")
	router.HandleFunc("/todo", CreateItem).Methods("POST")
	router.HandleFunc("/todo/{id}", UpdateItem).Methods("PUT")
	router.HandleFunc("/todo/{id}", DeleteItem).Methods("DELETE")

	// Add Cross Origin Resource Sharing verification
	handler := cors.New(cors.Options{
		AllowedMethods: []string{"GET", "POST", "PUT", "DELETE"},
	}).Handler(router)

	http.ListenAndServe(":8000", handler)
}

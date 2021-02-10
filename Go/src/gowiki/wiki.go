package main

import (
	// "fmt"
	"html/template"
	"io/ioutil"
	"log"
	"net/http"
	"regexp"
)

/* regex filepath validation expression
regexp.MustCompile will parse and compile the regular expression, and return a regexp.Regexp. MustCompile is distinct from Compile in that it will panic if the expression compilation fails, while Compile returns an error as a second parameter
*/
var validPath = regexp.MustCompile("^/(edit|save|view)/([a-zA-Z0-9]+)$")

/* templates holds all templates objects, for HTML files found at app init.
ParseFiles will read the contents of *.html and return a ponter to a template.Template object
Must is a wrapper to panic the application to exit is passed a non-nill erro, for example if a template file has not been found, in this case
*/
var templates = template.Must(template.ParseGlob("tmpl/*.html"))

// Page defines a wiki page's properties as saved in memory
type Page struct {
	Title string
	Body  []byte // io libraries require bytes instead of string
}

// save persists a page to a file
func (p *Page) save() error {
	filename := "data/" + p.Title + ".txt"

	// returns error just like Write(). 0600 > Unix Read-Write permission for creating the file.
	return ioutil.WriteFile(filename, p.Body, 0600)
}

/* loadPage reads a file from persistant storage into memory (body) and returns a pointer to a Page literal constructed with the proper title and body values
 */
func loadPage(title string) (*Page, error) {
	filename := "data/" + title + ".txt"
	body, err := ioutil.ReadFile(filename)

	if err != nil {
		return nil, err
	}

	return &Page{Title: title, Body: body}, nil
}

// HANDLER TO RENDER A WIKI PAGE: Simple Go web server //

// rootViewHandler makes web root redirect to '/view/FrontPage'
func rootViewHandler(w http.ResponseWriter, r *http.Request) {
	http.Redirect(w, r, "/view/frontPage", http.StatusFound)
	return
}

/* 	1. viewHandler, of the type http.HandlerFunc
2. http.ResponseWriter value assembles the HTTP server's response; by writing to it, we send data to the HTTP client
3. An http.Request is a data structure that represents the client HTTP request. r.URL.Path is the path component of the request URL. We are creating a sub-slice of Path from the len("/view/") character to the end (the filename of the resource being accessed)
*/
func viewHandler(w http.ResponseWriter, r *http.Request, title string) {
	p, err := loadPage(string(title))
	if err != nil {
		/* if view page is not found, load edit page to create content
		http.Redirect function adds an HTTP status code of http.StatusFound (302) and a Location header to the HTTP response
		*/
		http.Redirect(w, r, "/edit/"+title, http.StatusFound)
		return
	}
	// fmt.Fprintf(w, "<h1>%s</h1><div>%s</div>", p.Title, p.Body)
	renderTemplate(w, "view", p)
}

/* editHandler load the edit page and displays an HTML form. If the page does not exist, cerates an empty struct
 */
func editHandler(w http.ResponseWriter, r *http.Request, title string) {
	p, err := loadPage(title)
	if err != nil {
		p = &Page{Title: title}
	}
	renderTemplate(w, "edit", p)
}

// saveHandler submits the forms at /edit for saving to file
func saveHandler(w http.ResponseWriter, r *http.Request, title string) {
	body := r.FormValue("body")                  // string contents for new page
	p := &Page{Title: title, Body: []byte(body)} /* Create the new page object 												type conversion to byte to 													fit in struct body property
	 */
	err := p.save()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	http.Redirect(w, r, "/view/"+title, http.StatusFound)
}

/* renderTemplate is a helper render function that helps to remove duplicate view handler code
templateExecute executes the template, writing the generated HTML to the http.ResponseWriter. The .Title and .Body dotted identifiers refer to p.Title and p.Body
*/
func renderTemplate(w http.ResponseWriter, tmpl string, p *Page) {
	// w > http.ResponseWriter, p > *Page
	err := templates.ExecuteTemplate(w, tmpl+".html", p)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
}

/* makeHandler is a wrapper function literal that takes a handler function type (view, edit and edit above) and returns a function of the http.HandlerFunc type
The returned function is called a closure because it encloses values defined outside of it. In this case, the variable fn (the single argument to makeHandler) is enclosed by the closure. The variable fn will be one of our save, edit, or view handlers
Also helps to consolidate http.HandlerFunc error handling in on place
*/
func makeHandler(fn func(http.ResponseWriter, *http.Request, string)) http.HandlerFunc {
	/* extract the page title from the Request and call the provided handler 'fn'
	 */
	return func(w http.ResponseWriter, r *http.Request) {
		m := validPath.FindStringSubmatch(r.URL.Path)

		if m == nil {
			http.NotFound(w, r)
			return
		}
		fn(w, r, m[2])
	}
}

func main() {
	/* HandleFunc tells the http package to handle all requests to an endpoint using the specified view function
	ListenAndServe (a blocking function) always returns an error, since it only returns when an unexpected error occurs. In order to log that error we wrap the function call with log.Fatal
	*/

	// register view handlers
	http.HandleFunc("/", rootViewHandler)
	http.HandleFunc("/view/", makeHandler(viewHandler))
	http.HandleFunc("/edit/", makeHandler(editHandler))
	http.HandleFunc("/save/", makeHandler(saveHandler))

	// spin up web server to listen on port 8080 on any of the local interfaces
	log.Fatal(http.ListenAndServe(":8080", nil))
}

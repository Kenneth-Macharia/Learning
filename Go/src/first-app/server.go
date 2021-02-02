package main

import "net/http"

func main() {
	// Using *panic* to handle exceptional situations
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("Hello World"))
	})
	// starts a webserver on address :8080
	error := http.ListenAndServe(":8080", nil)
	// reporting err with panic, for port already in use
	if error != nil {
		panic(error.Error())
	}
}

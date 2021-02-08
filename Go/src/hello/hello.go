package main

import (
	"fmt"
	"greetings"
	"log"
)

func main() {
	// set log entry prefix & flag to disable verbose printing
	log.SetPrefix("greetings: ")
	log.SetFlags(0)

	// name slice
	names := []string{"Gladys", "Samantha", "Darrin"}
	message, err := greetings.Hellos(names)

	// handle returned error
	if err != nil {
		log.Fatal(err)
	}

	for _, msg := range message {
		fmt.Println((msg))
	}
}

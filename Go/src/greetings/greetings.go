package greetings

import (
	"errors"
	"fmt"
	"math/rand"
	"time"
)

// Hello returns a greeting for the named person or error if not name is provided
func Hello(name string) (string, error) {
	if name == "" {
		return "", errors.New("no name provided")
	}

	// create a random formatted message
	message := fmt.Sprintf(randomFormat(), name)
	return message, nil
}

// Seeds the rand package with the current time. Go executes init functions automatically at program startup, after global variables have been initialized.
func init() {
	rand.Seed(time.Now().UnixNano())
}

// randm Format returns a pre-formatted greeting randomly
func randomFormat() string {
	msgFormats := []string {
		"Hi %v. Welcome!",
		"Great to see you %v!",
		"Hail, %v! Well met!",
	}

	return msgFormats[rand.Intn(len(msgFormats))]
}

// Hellos returns a map that associates each of the named people with a greeting message
func Hellos(names []string) (map[string]string, error) {
	// map of names to messages
	messages := make(map[string]string)

	for  _, name := range names {
		msg, err := Hello(name)

		if err != nil {
			return nil, err
		}

		messages[name] = msg
	}

	return messages, nil
}

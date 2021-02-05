package main

import (
	"fmt"
	"sync"
	"time"
)

const (
	logInfo    = "INFO"
	logWarning = "WARNING"
	logError   = "ERROR"
)

var wg = sync.WaitGroup{}
var logCh = make(chan logEntry, 5)
var doneCh = make(chan struct{}) // A no-field struct in Go needs
// no memory allocation, hence is
// cheap to use as a type for a
// messaging(no data) only channel.

func main() {

	// Working with channels
	ch := make(chan int) // create a channel
	wg.Add(2)

	go func() { // receiver goroutine
		i := <-ch // receive value from channel
		fmt.Println(i)
		wg.Done()
	}()

	go func() { // Sender goroutine
		i := 42
		ch <- i // send value into channel
		i = 27  // Verify re-assigning i has no effect on goroutines
		wg.Done()
	}()
	wg.Wait()
	fmt.Println("----------------------")

	// Multiple goroutine and 1 channel
	for k := 0; k < 10; k++ {
		wg.Add(2)

		go func() {
			i := <-ch
			fmt.Println(i)
			wg.Done()
		}()

		go func() {
			ch <- 42
			wg.Done()
		}()
	}
	wg.Wait()
	fmt.Println("----------------------")

	// Designated receiver and sender goroutines
	wg.Add(2)
	go func(ch <-chan int) {
		// receiver goroutine
		i := <-ch
		fmt.Println(i)
		wg.Done()
	}(ch)

	go func(ch chan<- int) {
		// sender goroutine
		ch <- 50
		wg.Done()
	}(ch)
	wg.Wait()
	fmt.Println("----------------------")

	// Working with buffered channels
	buffCh := make(chan int, 10) // buffered channel with 10 slots
	wg.Add(2)
	go func(ch <-chan int) {
		for i := range ch { // itereating over channel
			fmt.Println(i)
		}
		wg.Done()
	}(buffCh)

	go func(ch chan<- int) {
		for i := 1; i < 10; i++ {
			ch <- i
		}
		close(ch) // CLOSE CHANNEL AFTER USE, else deadlock!
		wg.Done()
	}(buffCh)
	wg.Wait()
	fmt.Println("----------------------")

	// Working with select statement for goroutine exit stretegy
	go logger() // loggin goroutine, listening for and printing logs mgs

	// send some logs to the log channel
	logCh <- logEntry{time.Now(), logInfo, "App starting..."}
	logCh <- logEntry{time.Now(), logWarning, "App about to panic"}
	logCh <- logEntry{time.Now(), logError, "App panicked!"}
	logCh <- logEntry{time.Now(), logInfo, "App shut down."}
	time.Sleep((100 * time.Millisecond))

	doneCh <- struct{}{} // empty struct used to send msg that data was sent
	// msg sent here to signal we are done with the goroutine
}

type logEntry struct {
	time     time.Time
	severity string
	message  string
}

func logger() {
	for {
		select {
		case log := <-logCh:
			fmt.Printf("%v : [%v] %v\n",
				log.time.Format("2006-01-02 15:04:05"),
				log.severity,
				log.message)
		case <-doneCh:
			break // break loop when msg received that we are done with struct
		}
	}
}

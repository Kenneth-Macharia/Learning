package main

import (
	"fmt"
	"runtime"
	"sync"
)

var wg = sync.WaitGroup{}
var counter = 0
var m = sync.RWMutex{}

func main() {

	// Using Waitgroups (Out-of-order execution)
	for i := 0; i < 10; i++ {
		wg.Add(2)
		go sayHello()
		go increment()
	}
	wg.Wait()
	fmt.Println("----------------------")

	// Using Waitgroups + mutexes to sync goroutines
	// This however forces the goroutines to run synchronously
	// and is not concurrent.
	// For such an application its better not to use goroutines as
	// it would be faster than forcing goroutines to run this way.
	for i := 0; i < 10; i++ {
		wg.Add(2)

		m.RLock() // Adds a R lock for this func
		go sayHello2()

		m.Lock() // adds a RW lock for this func
		go increment2()
	}
	wg.Wait()
	fmt.Println("----------------------")

	// Querying CPUs available on local machine
	fmt.Printf("# of available CPUs: %v\n", runtime.NumCPU())

	// Set # of threads to use to execute Go app
	runtime.GOMAXPROCS(4)

	// Query set # of threads to use to execute Go app
	fmt.Printf("Max CPUs set: %v\n", runtime.GOMAXPROCS(-1))

}

func sayHello() {
	fmt.Printf("Hello #%v\n", counter)
	wg.Done()
}

func increment() {
	counter++
	wg.Done()
}

func sayHello2() {
	fmt.Printf("Hello #%v\n", counter)
	m.RUnlock() // Release the R lock
	wg.Done()
}

func increment2() {
	counter++
	m.Unlock() // release the RW lock
	wg.Done()
}

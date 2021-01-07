package main

import (
	"fmt"
)

func main()  {

	// Uninitialized variables have a default value of 0 or false
	var i int
	fmt.Printf("Uninitialized numerical var = %v\n", i)

	var b bool
	fmt.Printf("Uninitialized bool var = %v\n", b)

	var s string
	fmt.Printf("Uninitialized string var = %v\n", s)

	// creating floating types
	a := 3.14 // initializer syntax defaults to float64
	fmt.Printf("%v, %T\n", a, a)

	var c float32 = 3.4e32 // explicitly declare float32
	fmt.Printf("%v, %T\n", c, c)

	d := 2.1E14
	fmt.Printf("%v, %T\n", d, d)
}

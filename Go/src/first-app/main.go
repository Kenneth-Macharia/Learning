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

	// Working with complex numbers
	var n complex64 = 1 + 2i
	fmt.Printf("%v, %T\n", n, n)

	var k complex128 = 0 + 2i
	fmt.Printf("%v, %T\n", k, k)

	// Accessing the real & imaginary parts of complex numbers
	fmt.Printf("%v, %T\n", real(n), real(n))
	fmt.Printf("%v, %T\n", imag(k), imag(k))

	// Making a complex number using the complex(real_num, imag_num)
	var j complex64 = complex(5, 12)
	fmt.Printf("%v, %T\n", j, j)

	// Working with strings
	str := "this is a string"
	fmt.Printf("%v, %T\n", str, str)

	// Indexing strings: returns the unicode representation of 'i'
	fmt.Printf("%v, %T\n", str[2], str[2])

	// Type convert the byte representation of indexed str char to str rep
	fmt.Printf("%v, %T\n", string(str[2]), string(str[2]))

	// String operations
	str2 := "concatenation"
	fmt.Printf("%v, %T\n", (str + str2), (str + str2))

	// str > byte conversion
	str3 := []byte(str2)
	fmt.Printf("%v, %T\n", str3, str3)
	
}

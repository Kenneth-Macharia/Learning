package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"log"
	"math"
	"net/http"
	"reflect"
)

func main() {

	// Uninitialized variables have a default value of 0 or false
	var i int
	fmt.Printf("Uninitialized numerical var = %v\n", i)

	var b bool
	fmt.Printf("Uninitialized bool var = %v\n", b)

	var s string
	fmt.Printf("Uninitialized string var = %v\n", s)
	fmt.Println("---------------------------")

	// creating floating types
	a := 3.14 // initializer syntax defaults to float64
	fmt.Printf("%v, %T\n", a, a)

	var c float32 = 3.4e32 // explicitly declare float32
	fmt.Printf("%v, %T\n", c, c)

	d := 2.1e14
	fmt.Printf("%v, %T\n", d, d)
	fmt.Println("---------------------------")

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
	fmt.Println("---------------------------")

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

	// Updating string (String bytes appending)
	str4 := append([]byte("hello "), "world"...)
	fmt.Printf("Appended byte stream: %b\n", str4)
	fmt.Printf("String representation: %s\n", string(str4))
	fmt.Println("---------------------------")

	// Constants
	// const myConst float32 = math.Sin(1.57) Not Valid
	const myConst float32 = 3.142
	fmt.Printf("%v, %T\n", myConst, myConst)

	// Implicit type conversion with constants
	const o = 23
	var v int16 = 29
	fmt.Printf("%v, %T\n", o+v, o+v)
	fmt.Println("---------------------------")

	// Enumerated constants
	const (
		a2 = iota
		b2 = iota
		c2 = iota
	)

	fmt.Printf("%v\n", a2)
	fmt.Printf("%v\n", b2)
	fmt.Printf("%v\n", c2)

	const (
		a3 = iota
		b3
		c3
	)

	fmt.Printf("%v\n", a3)
	fmt.Printf("%v\n", b3)
	fmt.Printf("%v\n", c3)
	fmt.Println("----------")

	// Implementation of enumerated constants
	const (
		catSpec = iota
		dogSpec
		snakeSpec
	)

	var specType int = catSpec
	fmt.Printf("%v\n", specType == catSpec)
	fmt.Printf("%v\n", specType == dogSpec)

	var specType2 int
	fmt.Printf("%v\n", specType2 == catSpec)

	// Ignoring the zero for iota using a blank identifier
	const (
		_ = iota
		a4
		a5
	)
	fmt.Printf("%v\n", a4)
	fmt.Printf("%v\n", a5)

	// Implementing an offset for iota
	const (
		_ = iota + 3
		b4
		b5
	)
	fmt.Printf("%v\n", b4)
	fmt.Printf("%v\n", b5)

	// Formatting file size using enumerated constants
	const (
		_     = iota
		KiloB = 1 << (10 * iota)
		MegaB
		GigaB
		TeraB
		PetaB
		ExaB
		ZettaB
		YottaB
	)
	var filesize float64 = 4000000000000000000000000.00
	fmt.Printf("%.2fYB\n", filesize/YottaB)
	fmt.Println("----------")

	// Encoding info efficiently: Stores user roles using bits
	const (
		isAdmin          = 1 << iota //1
		canSeeFinancials             //2

		atHQ     //4
		atAfrica //16
		atEurope //32
	)

	var user1 byte = isAdmin | canSeeFinancials | atHQ //111
	fmt.Printf("%b\n", isAdmin)                        //1
	fmt.Printf("%b\n", canSeeFinancials)               //10
	fmt.Printf("%b\n", atHQ)                           //100
	fmt.Printf("%b\n", user1)                          //111

	// Check user1 permissions
	fmt.Printf("User1 an admin? %v\n", isAdmin&user1 == isAdmin)
	fmt.Printf("User1 at HQ? %v\n", atHQ&user1 == atHQ)
	fmt.Printf("User1 at HQ? %v\n", atAfrica&user1 == atAfrica)
	fmt.Println("---------------------------")

	// Working with arrays
	var identyMatrix [3][3]int
	identyMatrix = [3][3]int{{1, 0, 0}, {0, 1, 0}, {0, 0, 1}}
	fmt.Printf("%v\n", identyMatrix)

	var indentityMatrix2 [3][3]int
	indentityMatrix2[0] = [3]int{1, 0, 0}
	indentityMatrix2[1] = [3]int{0, 1, 0}
	indentityMatrix2[2] = [3]int{0, 0, 1}
	fmt.Printf("%v\n", indentityMatrix2)

	// Array copies and references
	arr := [...]int{1, 2, 3}
	arr2 := arr // arr2 is a copy of arr
	arr2[1] = 5
	arr3 := &arr2 // arr3 points to arr2
	arr3[2] = 9
	fmt.Printf("%v\n", arr)
	fmt.Printf("%v\n", arr2)
	fmt.Printf("%v\n", arr3)

	// Slices
	slice := []int{4, 3, 5, 6}
	fmt.Printf("%v\n", len(slice))
	fmt.Printf("%v\n", cap(slice))

	// Appending items to slices
	slice = append(slice, 7, 9)
	fmt.Printf("%v\n", len(slice))
	fmt.Printf("%v\n", cap(slice))

	slice2 := []int{10, 11, 23}
	slice = append(slice, slice2...)
	fmt.Printf("%v\n", len(slice))
	fmt.Printf("%v\n", cap(slice))

	// Popping element from slices
	slc := []int{1, 2, 3, 4, 5}
	slc2 := slc[1:] // head pop
	fmt.Printf("%v\n", slc2)
	slc3 := slc[1 : len(slc)-2] // tail pop
	fmt.Printf("%v\n", slc3)
	slcNew := []int{6, 7, 8, 9, 10}
	slc4 := append(slcNew[:2], slcNew[3:]...) //mid section pop
	fmt.Printf("%v\n", slc4)
	fmt.Println("---------------------------")

	// Declare structs
	type Doctor struct {
		number     int
		actorName  string
		companions []string //slice
	}

	// Using structs
	aDoctor := Doctor{
		number:    3,
		actorName: "Jon Pertwee",
		companions: []string{
			"Liz Shaw",
			"Jo Grant",
			"Sarah Jane Smith",
		},
	}

	// Working with structs
	fmt.Println(aDoctor)

	// Accessing struct individual data using dot notation
	fmt.Println(aDoctor.actorName)
	fmt.Println(aDoctor.companions[2])

	// Anonymous struct
	bDoctor := struct{ name string }{name: "Jon Pertwee"}
	fmt.Printf("Anonymous struct: %s\n", bDoctor)

	// Embedding with structs
	type Animal struct {
		Name   string
		Origin string
	}

	type Bird struct {
		Animal   // embedding Animal properties
		SpeedKPH float32
		CanFly   bool
	}

	//Initialize struct
	bird1 := Bird{}

	// Set properties
	bird1.Name = "Emu"
	bird1.Origin = "Australia"
	bird1.SpeedKPH = 48
	bird1.CanFly = false

	fmt.Println(bird1)
	fmt.Println(bird1.Name)
	fmt.Println(bird1.Origin)
	fmt.Println(bird1.CanFly)

	// Using struct tags
	type Mountains struct {
		Name     string `max:"100"`
		Location string
		height   int
	}

	// Accessing struct tags
	objectType := reflect.TypeOf(Mountains{})
	field, ok := objectType.FieldByName(("Name"))
	fmt.Println(field.Tag, ok)
	field2, _ := objectType.FieldByName(("Name"))
	fmt.Println(field2.Tag)

	// Using the Go 'ok' variable to ensure that the key "Name" exists.
	// We can also use the _ symbol to ignore this value
	fmt.Println("---------------------------")

	// Floating point equality comparison
	// Passes for low precision numbers
	myNum := 0.12

	if myNum == math.Pow(math.Sqrt(myNum), 2) {
		fmt.Println("Equal")
	} else {
		fmt.Println("Not equal")
	}

	// Fails for high precision numbers
	myNum2 := 0.122562

	if myNum2 == math.Pow(math.Sqrt(myNum2), 2) {
		fmt.Println("Equal")
	} else {
		fmt.Println("Not equal")
	}

	// Fix for high precision equality tests using error epsilon value
	myNum3 := 0.122562

	if math.Abs(myNum3/math.Pow(math.Sqrt(myNum3), 2)-1) < 0.001 {
		fmt.Println("Equal")
	} else {
		fmt.Println("Not equal")
	}
	fmt.Println("---------------------------")

	// Using continue in for loops
	for i := 0; i < 10; i++ {
		if i%2 == 0 {
			continue
		}
		fmt.Println(i)
	}

	// Using break with a label
loop:
	for i := 0; i <= 3; i++ {
		for j := 1; j <= 3; j++ {
			fmt.Println(i * j)

			if i*j >= 3 {
				break loop
			}
		}
	}

	// Looping over collections
	phrase := "hello world"
	for i, v := range phrase {
		fmt.Println(i, string(v))
	}

	// Working with the keys/indice or values only
	sPop := map[string]int{
		"California": 3978359,
		"Texas":      2794898,
		"New York":   1977245,
	}
	// Key only
	for k := range sPop {
		fmt.Println(k)
	}
	// Values only using the 'write only' operator
	for _, v := range sPop {
		fmt.Println(v)
	}
	fmt.Println("----------")

	// Using *defer* to release resources immediately after creation
	res, err := http.Get(("http://www.google.com/robots.txt"))
	if err != nil {
		log.Fatalln(err)
	}
	defer res.Body.Close()
	// working with res resource after closing it above
	robots, err := ioutil.ReadAll(res.Body)
	if err != nil {
		log.Fatalln(err)
	}
	fmt.Printf("%s", robots)
	fmt.Println("----------")

	// recovering from panics
	fmt.Println(("Start main execution..."))
	panicker()
	fmt.Println("Ending main execution")
	fmt.Println("---------------------------")

	// Pointers
	val := 23
	var pointer *int = &val // create pointer to value in a in memory
	fmt.Println(val, pointer)
	fmt.Println(&val, pointer) // confirming the two addresses are same
	fmt.Println(val, *pointer) // confirming the values
	*pointer = 46              // Using the pointer to change the referenced value
	fmt.Println(val, pointer)
	fmt.Println("----------")

	someArr := [3]int{1, 2, 3}
	fmt.Printf("%v, %p, %p, %p\n", someArr, &someArr[0], &someArr[1], &someArr[2])

	// Object pointers
	type myStruct struct {
		foo int
	}

	var ms *myStruct
	ms = &myStruct{foo: 42} //ms points to s struct which has a property with a value 42
	fmt.Println(ms)

	// An uninitialized pointer will be set to nil
	var ms2 *myStruct
	ms2 = new(myStruct) // can't initialize fields with new keyword
	fmt.Println(ms2)

	// Use the pointer to get a struct property value (dereferencing)
	var ms3 *myStruct
	ms3 = new(myStruct)
	(*ms3).foo = 42
	fmt.Println((*ms3).foo)

	// Complex type derefencing is implied by the compiler
	var ms4 *myStruct
	ms4 = new(myStruct)
	(*ms4).foo = 50
	fmt.Println(ms4.foo)
	fmt.Println("---------------------------")

	// Passing values by reference to functions using pointers
	greeting, name := "Hello", "Stacey"
	greetings(&greeting, &name) // Pass value address to function
	fmt.Println(name)           //Confirm value was changed by function

	// Passing varidic parameters
	sum("Sum is:", 1, 2, 3, 4, 5)
	fmt.Println(*sum2(3, 4, 5)) //dereference sum2's return value

	// Returning multiple values (If err is thrown, main exits here)
	retVal, err := throwsError(5.0, 1.0)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(retVal)

	// Anonymous function used within loop
	for i := 0; i < 5; i++ {
		func(i int) {
			// Anonymous functions
			fmt.Println(i)
		}(i) // Passing the for loop counter to the function is safer for asyn processing
	}

	// Using methods with structs
	// Initialize struct
	obj := greeter{
		greeting: "Hello",
		name:     "Go",
	}
	obj.greet()
	obj.greet2()
	fmt.Println("---------------------------")

	// Using primitive type interface
	myInt := IntCounter(0) //cast an int to an intcounter
	var inc Incrementer = &myInt

	for i := 0; i < 10; i++ {
		fmt.Println(inc.Increment())
	}

	// Interface composition implementation with empty interface
	// intermediate type conversion checking
	var wc interface{} = NewBufferedWriterCloser()
	if wc, ok := wc.(WriterCloser); ok {
		wc.Write([]byte("Hello YouTube listeners, this is a test!"))
		wc.Close()
	} else {
		fmt.Println("Type conversion failed")
	}

	// ####################	END OF MAIN() ##################
}

// ########## STRUCTS, INTERFACES AND METHODS #########

// Structs and methods
// declare a struct type
type greeter struct {
	greeting string
	name     string
}

// declare a method. Receiving the context by-val via obj
func (obj greeter) greet() {
	fmt.Println(obj.greeting, obj.name)
}

// declare another method. Receiving the context by-ref via obj.
func (obj *greeter) greet2() {
	// changes here will propagate to the struct
	fmt.Println(obj.greeting, obj.name) //implicit dereferencing
}

// Interfaces: primitive type

// Incrementer is an int type interface
type Incrementer interface {
	Increment() int
}

// IntCounter is an int type alias to implement the interface
type IntCounter int

// Increment is a method to increment the int type
func (ic *IntCounter) Increment() int {
	*ic++
	return int(*ic)
}

// ******* INTERFACE COMPOSITION *******

// Writer is the first interface to be composed
type Writer interface {
	Write([]byte) (int, error)
}

// Closer is the second interface to be composed
type Closer interface {
	Close() error
}

// WriterCloser is the composed interface
type WriterCloser interface {
	Writer //embed the Writer interface
	Closer //embed the Closer interface
}

// BufferedWriterCloser implements the composed interface
type BufferedWriterCloser struct {
	buffer *bytes.Buffer
}

// Write method overriden with a BufferedWriterCloser method
func (bwc *BufferedWriterCloser) Write(data []byte) (int, error) {
	// This method writes the buffer contents in 8 char chunks
	n, err := bwc.buffer.Write(data)
	if err != nil {
		return 0, err
	}

	v := make([]byte, 8)
	for bwc.buffer.Len() > 8 {
		_, err := bwc.buffer.Read(v)
		if err != nil {
			return 0, err
		}
		_, err = fmt.Println(string(v))
		if err != nil {
			return 0, err
		}
	}

	return n, nil
}

// Close method overide with a BufferedWriterCloser method
func (bwc *BufferedWriterCloser) Close() error {
	// This method flushes the buffer if it has less than 8 chars
	for bwc.buffer.Len() > 0 {
		data := bwc.buffer.Next(8)
		_, err := fmt.Println(string(data))
		if err != nil {
			return err
		}
	}

	return nil
}

// NewBufferedWriterCloser is a buffer initializer for the
// BufferedWriterCloser struct that retuns an obj with a buffer
// initialized
func NewBufferedWriterCloser() *BufferedWriterCloser {
	return &BufferedWriterCloser{
		buffer: bytes.NewBuffer([]byte{}), // Initializer
	}
}

// ################ FUNCTIONS ######################

func server() {
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

func panicker() {
	// panicking function

	fmt.Println(("about to panic..."))

	// Handle panic using defer, anonymous function & recover
	defer func() {
		if err := recover(); err != nil {
			log.Println(err)
		}
	}()
	panic("Something bad happened")

	// Code after *panic* in a panicking function does not execute and is thus
	// unreacheable
}

func greetings(greeting, name *string) { //Takes string pointer types
	// Passing pointers as arguments
	fmt.Println(*greeting, *name)
	*name = "Ted" //Re-assigning value
	fmt.Println(*name)
}

func sum(msg string, values ...int) {
	result := 0

	for _, val := range values {
		result += val
	}
	fmt.Println(msg, result)
}

func sum2(vals ...int) *int { // int pointer type return
	result := 0

	for _, val := range vals {
		result += val
	}

	return &result
}

func throwsError(a, b float64) (float64, error) {
	if b == 0.0 {
		return 0.0, fmt.Errorf("Cannot divide by %f", b)
	}

	return a / b, nil
}

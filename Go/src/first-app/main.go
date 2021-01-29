package main

import (
	"fmt"
	"math"
	"reflect"
)

func main()  {

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

	d := 2.1E14
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
	str4 := append([]byte("hello " ), "world"...)
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
		_ = iota
		KiloB = 1 << (10 * iota)
		MegaB
		GigaB
		TeraB
		PetaB
		ExaBy
		ZettaB
		YottaB
	)
	var filesize float64 = 4000000000000000000000000.00
	fmt.Printf("%.2fYB\n", filesize/YottaB)
	fmt.Println("----------")

	// Encoding info efficiently: Stores user roles using bits
	const (
		isAdmin = 1 << iota  //1
		canSeeFinancials  //2

		atHQ  //4
		atAfrica  //16
		atEurope  //32
	)

	var user1 byte = isAdmin | canSeeFinancials | atHQ //111
	fmt.Printf("%b\n", isAdmin)  //1
	fmt.Printf("%b\n", canSeeFinancials)  //10
	fmt.Printf("%b\n", atHQ)  //100
	fmt.Printf("%b\n", user1)  //111

	// Check user1 permissions
	fmt.Printf("User1 an admin? %v\n", isAdmin & user1 == isAdmin)
	fmt.Printf("User1 at HQ? %v\n", atHQ & user1 == atHQ)
	fmt.Printf("User1 at HQ? %v\n", atAfrica & user1 == atAfrica)
	fmt.Println("---------------------------")

	// Working with arrays
	var identyMatrix [3][3] int
	identyMatrix = [3][3]int { [3]int{1, 0, 0}, [3]int{0, 1, 0}, [3]int{0, 0, 1}, }
	fmt.Printf("%v\n", identyMatrix)

	var indentityMatrix2 [3][3] int
	indentityMatrix2[0] = [3]int {1, 0, 0}
	indentityMatrix2[1] = [3]int {0, 1, 0}
	indentityMatrix2[2] = [3]int {0, 0, 1}
	fmt.Printf("%v\n", indentityMatrix2)

	// Array copies and references
	arr := [...]int{1, 2, 3}
	arr2 := arr  // arr2 is a copy of arr
	arr2[1] = 5
	arr3 := &arr2  // arr3 points to arr2
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
	slc2 := slc[1:]  // head pop
	fmt.Printf("%v\n", slc2)
	slc3 := slc[1:len(slc) - 2]  // tail pop
	fmt.Printf("%v\n", slc3)
	slcNew := []int{6, 7, 8, 9, 10}
	slc4 := append(slcNew[:2], slcNew[3:]...)  //mid section pop
	fmt.Printf("%v\n", slc4)
	fmt.Println("---------------------------")

	// Declare structs
	type Doctor struct {
		number int
		actorName string
		companions []string  //slice
	}

	// Using structs
	aDoctor := Doctor{
		number: 3,
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
	bDoctor := struct{name string}{name: "Jon Pertwee"}
	fmt.Printf("Anonymous struct: %s\n", bDoctor)

	// Embedding with structs
	type Animal struct {
		Name string
		Origin string
	}

	type Bird struct {
		Animal  // embedding Animal properties
		SpeedKPH float32
		CanFly bool
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
		Name string `max:"100"`
		Location string
		height int
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
	// Passes for small precision numbers
	myNum := 0.12

	if myNum == math.Pow(math.Sqrt(myNum), 2) {
		fmt.Println("Equal")
	} else {
		fmt.Println("Not equal")
	}

	// Fails for small precision numbers
	myNum2 := 0.122562

	if myNum2 == math.Pow(math.Sqrt(myNum2), 2) {
		fmt.Println("Equal")
	} else {
		fmt.Println("Not equal")
	}

	// Fix for large precision equality tests using error epsilon value
	myNum3 := 0.122562

	if math.Abs(myNum3 / math.Pow(math.Sqrt(myNum3), 2) - 1) < 0.001 {
		fmt.Println("Equal")
	} else {
		fmt.Println("Not equal")
	}
}

# Intro

- Developed by a team at Google comparising of Robert Griesemer, Rob Pike and
  Ken Thompson.
- "Developed while waiting for C++ programs to compile".
- Developed to build highly scalable and concurrent applications.
- Developed due to limitiation of existing languages in use at Google at the
  time i.e Python (easy but slow), Java (fast but increasingly complex type
  system) and C/C++ (fast but slow compile times and increasingly complex type
  system)
- Concurrency is also patched into the the above languages.
- Some weaknesses addressed and improvements included into Go are:

    1. Strong typed - variables types can't change over time
    2. Statically typed - variables types must be declared at compile time
    3. Fast - both compile and run times
    4. Compiles direct to machine code
    5. Concurrency built in
    6. Simple - also leaves out some complex features
    7. Memory managed and speed optimized gabarge collection
    8. Compiles into a single binary including dependancies
    9. Strong dev community

_"Go is expressive, concise, clean, and efficient. Its concurrency mechanisms
make it easy to write programs that get the most out of multicore and
networked machines, while its novel type system enables flexible and modular
program construction. Go compiles quickly to machine code yet has the convenience
of garbage collection and the power of run-time reflection. It's a fast,
statically typed, compiled language that feels like a dynamically typed,
interpreted language"_

## Setting up a Go local environment

- Using the binary availble on golang.org, install Go to _/usr/local/go_

_Check install location after installation using `$ which go`_

- Downloaded libraries using `$ go get <lib>` go into `~/go` (or golib), if the
 directory does not exist run `$ go get github.com/nsf/gocode` to download the
 syntax auto complete library, which will set up either directories for you.
- Add the folder to PATH so as to access the binaries via the `$ go` command:

    1. Add to .bashrc file the env variable called
       GOPATH: `export GOPATH=/Users/kenneth/go`
    2. Update PATH with the new executable location `export PATH=$PATH:$GOPATH/bin`
    3. Source the .bashrc file to update the changes `source ~/.bashrc`

_The above ensures that the first segment of GOPATH will be used by `go get <lib>`_

- Set up your workspace folder:

    1. Create a project folder with an _src_, _bin_ and _pkg_ folder to hold the
    source code, compiled binaries and dependancy (to be included in project
    binaries but not needing re-compling).
    2. Add the workspace folder above to GOPATH, similarly to the library folder
       above and update PATH as well.

## Version controlling Go app

- Set up app folders using the `/go_workspace/github.com/<github_account_name>/app_folder`
  structure when using source control, to make the applications go gettable i.e
  downloadable using `go get <lib>`, since github will create a similar folder structure.

## Writing the first Go app

- Go files have a .go extension
- Packages are how Go code is organised into sub-libraries. They are then importable
  into your existing Go app to add functionality.
- All Go app files must be part of a package, declared at the top of the file.
- Imported packages follow next in the `import {}` statement.
- A main package with a main function is a Go app's entry point and is required
  for every Go application.
- Use `go run <path to main.go>` to run a Go app, which temporarily complies the
  application src files, then run the generated binary.
- Use `go build <path to package>` to compile the app package (app folder) into an
  executable in the main app folder (if it finds a main package with a main function).
  The run the executable to start the app `./executable`
- Use `go install <path to an enty-point package>` to build an app binary into
  the _bin_ folder.

## Variables

- Declaring variables:

    1. `var <variable name> <variable type>` e.g _var i int = 2_ Explcit type
       declaration
    2. `<variable name> := <value`> e.g _i := 2_ the complier infers the type
       using the value

- Only the explicit declaration syntax can be used to declare global variables
   but both can be used to declare local scope variables_
- Variables declared, must be used
- Uninitialized variables have a default value of 0(numericals), false(bools),
  ""(text) and 0 + 0i(complex nums)_

- Declare a block of global scope variables:

      var (
          var1 string = "somestring"
          var2 int = 2
          var3 float32 = 23.9
          var4float64 = 33.9
      )

- Variable shadowing: an inner scope variable with the same name as a package/
  global level, taking precedence.
- Lowecase first letter variables are scoped to _ONLY_ the package they are declared
  in and cannot be used by importing packages while uppecase first letter variables.
  are exportable and can be used in importing packages.
- Naming convention rules:

    1. Length of the variable name reflects the life span of the variable e.g single
    letter names for loop counters and more descriptive names for longer lived variables.
    2. Acronyms such as URL should be in caps
    3. Use _PascalCase_ or _camelCase_

- Type conversions:

    1. int > float32: `f = float32(i)`
    2. float32 > int: `i = int(f)` _note this can lead to precision loss_

        _In Go, a string is a stream of bytes. Converting an int to a string i.e
        `var i int = 42` `j = string(i)` retrieves the unicode character represented
        by the int. Converting back and forth between string and int should be via
        the `strconv` package_

    3. int > string: `import "strconv"` `s = strconv.Itoa(i)`

- Primitive types

    1. Boolean `bool`: _true_ or _false_
    2. Signed ints:

        (a) 8bit int `int8`: _-128 <> 127_
        (b) 16bit int `int16`: _-32,768 <> 32,767_
        (c) 32bit int `int | int32`:  _-2,147,483,648 <> 2,147,483,647_
        (d) 64bit int `int64`: _-9,223,372,036,854,775,808 <> 9,223,372,036,854,775,807_

    3. Unsigned ints:

        (a) 8bit uint `byte | uint8`: _0 <> 255_
        (b) 16bit uint `uint16`: _0 <> 65,535_
        (c) 32bit uint `uint32`: _0 <> 4,294,967,295_

        - Go insists on explicit type conversion even for close types e.g
          (int + int16), do this instead (int + int(int16))
        - Int operators include: `+`, `-`, `*`, `/` (integer division and yields
          an int always) and `%` (the remainder)

    4. Bitwise operators: when comparing bit representation of two ints, they return
    the result of the set bits (1) comparison of the two, converted
    back into an int:

        a) `&` (and): _1 if both corresponding bits have been set_
        b) `|` (or): _1 if either of the corresponding bits have been set or both_
        c) `^` (exclusive or): _1 if either of the corresponding bits have been set
         but not both_
        d) `&^` (and not): _1 if neither of the corresponding bits have been set_

    5. Bit shifting is _adding or subtracting powers of 2_
        - If `a := 8` then:

            a) Left bit shifting: `a << 3` = `8 * 2^3` = 64
            b) Right bit shifting: `a >> 3` = `8 / 2^3` = 1

    6. Floating types: _comform to the IEEE 64 standard_

        a) `float32` _+-1.18E-38 <> +-3.4E38_
        b) `float64` _+-2.23E-308 <> +-1.8E308_

          _- Modulus, bitwise operators and bit shifting operators are not available
          to floats_

        `See code samples in main.go`

    7. Complex type: opens up Go to be used for data science.

        a) `complex64` (float32 + float32 for the real & imaginary part)
        b) `complex128` (float64 + float64 for the real & imaginary part)

        `See code samples in main.go`

    8. Text types:

        a) string: are utf8 character thus can't encode all the characters. Are
           also a stream of bytes (uint8 chars). They are also an array of characters.
          Are also immutable.

        - String operations:

            - Concatenation: `string1 + string2`
            - Type conversion into bytes: `b := []byte(str)` convenient
            for tranferring strings or files across application and not
             worry about formating etc

        `See code samples in main.go`

        b) rune: are utf32/int32 characters. Can be upto 32bits thus has
         operations used during encoding runes to know the actual length e.g a
         string (utf8) is a valid rune.

        - Declared using single quotes e.g r := 'a'
        - Refer to the go docs for info on how to work with runes.

## Constants

- Declared using the `const` keyword
- Their naming convention is similar to varibles _`camel_case`
  for `package-scoped constants` and `Pascal_Case` for exportable constants_
- Typed constants declared same as variables `const myConst int = 2`
_Constants have to be assigned at compile time and must contain
 a definite value and not as a result of a runtime operation
 e.g function result or application runtime arguments_

- All primitive types mentioned above are applicable to constants
  as well as their operations.
- Constant types dont have to be explicitly declared `const a = 42`
 is valid. These defined as _literals_ can be used in operations
 with other typed variables unlike variable only operations that must be
 of the same type.
-_Enumerated constants_: are constant blocks that auto-generate
  enumerated values using a built-in counter called `iota`
- Iota auto-generates ints from 0 for each constant declared in
  the constants block. ``See code samples in main.go``

## Collections Types

- Types that hold multiple values at the same time. These include:

  a) Arrays: Are fixed length declared at compile time .Unlike variables
   that will be stored anywhere in memory, arrays store their elements
   contiguously (next to each other), ensuring that they can be accessed
   efficiently. Are also ordered.

  - Using arrays:

      1. `grades := [_size_] _type_ {elem, elem, elem}` explicitly
      specify the array size.
      2. `grades := [...] _type_ {elem, elem, elem}` creates an array
      large enough to hold the literals declared
      3. `var students [_size_] _type_` then initialize `students[0] = "Lisa"`
      4. Access array element `students[2]`
      5. Get array size `len(students)`

    _Arrays can only store data of the same type from primitives to arrays_

    - In other languages arrays are pointers to the elements stored in
    memory and re-assigning the array re-assigns the pointer to the
    initial values instead of making a copy of the array and re-assiging
    it. In Go, re-assigning arrays creates a new copy.

    - To change this behaviour use the _address of `&`_
    operator to specifiy a varible to reference the original value
    in memory. This operator in Go, is used to retrieve the memory
    address _in hex format_ of a value.

    `See code samples in main.go`

    _Most common use for arrays in Go is to back slices_

    b) Slices: Works similarly to arrays
    with all array functionalities. Are reference types to the
    underlying array. They are also not fixed length and resize as
    elements are added to them _usually to twice the previous size_,
    giving them extra capacity.

    - Using slices:

      1. `a := [] _type_ {elem, elem}` create a slice of the entire
      underlying array.
      2. `a := arr[:]` create a slice of the entire arr
      3. `a := arr[3:]` create a slice from the 4th element of arr
      4. `a := arr[:6]` creates a slice upto the 6th element of arr
      5. `a := arr[3:6]` creates a slice of arr between the 4th and the 6th elements.
      6. `a := make([]_type_, _len_)` if capacity is same as length
      7. `a := make([]_type_, _len_, _capacity_)` if len is different from cap
      8. `len(a)` return the size of the slice
      9. `cap(a)` returns the size of the underlying array
      10. `append(_parentSlice_, item, item, item)`
      11. `append(_parentSlice_, _sliceToAppend_...)`

      _If appending more items than the size of the slice, a copy
      operation will be triggered to move over all the elements to a new
      bigger slice, which can be costly. Using the `make()` can be used
      to avoid this_
      _since slice operations are reference operations there ever is
      only one underlying array being affected_

    c) Maps: an un-ordered key-value pair data structure. Their length is determined
    by the number of elements in them.

      _Map keys have to be equality testable_
      _All primitives and arrays, interfaces, pointers, structs and
      channels can be tested for equality but not slices, maps or functions_

    - Using maps:

      1. _Literal syntax declaration_: `mapName := map[_keys type_]
      _values type_{key:value, key:value}`
      2. Using `make()` when the values are not available at declaration
        time: `mapName := make(map[_keys type_]_values type_)
      3. Accessing maps values: `mapName[_key_]`
      4. Adding values: `mapName[_key_] = _value`
      5. Deleting values: `delete(_mapName_, _key_)
      6. Get number of elements: `len(mapName)`

      _Accessing non-existing keys in a map returns `0`_

      - To check if the key does exist:

      1. `return_val, ok := mapName[_key_]` : the `ok` variable will
      contain true if the key exists or false otherwise.
      2. To check existance only: `_ , ok := mapName[_key_]`

      _Similar to slices, maps are passed by reference thus a change
      downstream affects the original map_

    d) Struct: key-value pair data structure that can be used to group
    different typed data that is related e.g properties of an individual,
    similar to objects. The key-values can be of any type including arrays and slices.

    `See code samples in main.go`

    - Naming conventions for other variables apply to structs, including
    the key names.
    - Anonymous structs can also be used for short-lived code such as json
     responses from a web server.
    - They are declared as: `structName := struct{_key_ _vlaue data type_}
    {_key_: _value_}

    _struct unlike map are passed by value thus copies of the original
    structs are passed and changing one does not affect the other_
    _To pass structs by reference, use the `&` address of operator just
    like with arrays_

    - Go does not have some object oriented features like _inheritance_
    which represents a _is-a_ relationship between objects.
    - It uses _embedding_ to implement _composition-like_ features
    representing a _has-a_ relationship with structs.
    - Embedding involves adding a struct1 type within another struct2 to
    add struct1 properties to struct2, thus struct2 now _has_ struct1-like
    properties, even though the two are different and not related.
    - Embedding is appropriate when trying to add a _base_ behaviour that
     can be built upon but is not appropriate when behaviour needs to be
    used inter-changeably such as in polymorphism, in which case
    _interfaces_ are better suited._

    `See code samples in main.go`

    _Tags / field MetaData_ can be added to struct properties e.g for
    validation use. Tags are space-separated string literals added after
    the property type, within back ticks. They can also be key-value pairs.
    - Tags can only be accessed using Go's _reflection_ package.
    - Tags are to implemented by other frameworks and by themselves have
    no meaning in Go, other than literals added to struct properties.

    `See code samples in main.go`

## Control Flow

(a) If statements:

  1. `if _bool condition_ { code for true } else { code for false }`
  2. `if _bool condition_ {} else if _other bool condition_ {} else {}`

- Initializer syntax: `if pop, ok := myMap["key"]; ok {}` and uses the key
  existance check as the bool condition.
- All logical operators work with if statements: `< > >= <= == != && || !`

_Short-circuting is when Go ignores the rest of the tests in an || or &&
test, if a preceeding test meets the requirements for the overall test_

- Equality tests for floating point numbers can result in unexpected
  results, since they are only approximations of decimal.
`See code examples in main.go`

(b) Switch statements:

- Tag syntax: overlapping conditions are not allowed.

  1.Single case values:

      switch _comparison tag_ {
        case _value to compare_:
          _code to execute_

        case _value to compare_:
          _code to execute_

        default:
          _code to execute_
      }

  2.Multiple unique case values:

      switch _comparison tag_ {
        case value1, value2, value3:
          _code to execute_

        case value1, value2:
          _code to execute_

        default:
          _code to execute_
      }

  3.Multiple unique case initialized values:

      switch _comparison tag_ {
        case value1, value2, value3:
          _code to execute_

        case value1, i := 2 + 3; i:
          _code to execute_

        default:
          _code to execute_
      }

- Tagles syntax: overlapping conditions e.g below are allowed and the
  first match is processed.

      i : = 10
      switch {
        case i <= 10:
          _code to execute_

        case i <= 20:
          _code to execute_

        default:
          _code to execute_
      }

  _Since Go switches have an implicit `break` statement to prevent
   case fall through, it allows for the use of the
   `fallthrough` keyword to allow the next case to be processed as well,
   whether or not the condition passes_
  _An explicit `break` keyword can be used to breakout of a case execution early_

  - You can also types to evaluate switch conditions:

      `var i interface{} = 1` // Interfaces can take any type in Go

        switch i.(type) {
          case int:
            _code to execute_
          casefloat64:
            _code to execute_
          case [3]int:
            _code to execute (arrays must be same type & size_
          default:
            _code to execute_
        }

(c) _defer_: used on a statement in a function, will cause the
statement to be executed after the function but just before the function
returns. With multiple defer statement are executed in a LIFO order.
Variables associated with deferred statements will be evaluated
upto the defer.

  `See code sample in server.go`

(d) _panic_: Go does not have _Exception_ since they are considered
normal occurrences in Go e.g reading from a non-existing file. Go
returns _errors_ rather than throw exceptions and execution continues.
In situations where execution can't continue _panic_ is used instead.

    - Go runtime will raise a _panic_ where execution can't continue,
    since there are no in-built panic handling mechanisms.
    - We can raise a _panic_ where we anticipate execution will fail and
     where critical errors are likely to occur that we need handling of.

(e) _recover_: used to guratee execution after the code that panics. The
 panicking code e.g function still crashes but execution continues after
panicked function. The useful place to user `recover()` is within
deferred functions so that the application can look for panics and
decide how to handle them.

  _`returns` happen after `panics` happen after `defers` happen after a
   function executes `everything in {}`_
  _if recover cant be implemeted in panicking code, the panic can be
  delegated for handling further up the call stack by re-throwing it_

   `See code samples in main.go`

## Looping

- For loop is the only looping structure but can be used as while or do while loop.
- Syntax:

  1. `for i := 0; i < 5; i++ {}`
  2. `for i := 0; i < 5; i = i + 2 {}`
  3. Two counters: `for i, j := 0; i < 5; i, j = i + 1 {}`

      _The loop increment operation is not an expression, it is an independent statement_

  4. `i := 0` `for ; i < 5; i++ {}`
  5. Emulating a while loop:
      - `for i := 0; i < 5; { i++ }`
      - `i := 0` `for ; i < 5; { i++ }`
      - Best while loop emulator: `i := 0` `for i < 5 { i++ }`
  6. Infinate loop using _break_ keyword: `for { _break_ if some
  condition here is true }.

      _`break` cna be used with a `label` to indicate where to return
      execution flow and can be useful with nested loops_

  7. Ignore an interation using _continue_ keyword if some condition is
  true.
  8. Looping through collections using _for ... range_, which works for
   strings, slices, arrays and maps.
      - `arr := [3]int{1, 2, 3}`
      - `for index/key, value := range arr {}`

    `See code samples in main.go`

## Pointers



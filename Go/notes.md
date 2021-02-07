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

## Modules and Packages

- Packages are how Go code is organised and take the form of .go files. Packages
  usually perform specific functions and methods to perform those functions
  e.g `http`
- Inside the files, the package to which the file belongs to is indicates as the
  line `package <package fileName>`
- Imported/ external packages follow next in the `import ()` statement.
- A main package with a main function is a Go app's entry point and is required
  for every Go application.
- Multiple package files can be bundled into a directory to form a `module`. Modules
  define a family of related packages e.g `net`
- Modules also specifiy the context Go needs to run code including the version and
  dependancies required.
- Modules are started with the `go mod init <module download URL>` command, which
  creates a `go.mod` file in the module folder, identifying the module are
  importable by other modules.

## Building and running Go apps

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

    d) Struct: a collection of key-value pair data structure that can be used to
    group different typed data that is related e.g properties of an individual,
    similar to objects. The key-values can be of any type including arrays and slices.

    `See code samples in main.go`

    - Naming conventions for other variables apply to structs, including
    the key names.
    - Anonymous structs can also be used for short-lived code such as json
     responses from a web server.
    - They are declared as: `structName := struct{_key_ _value data type_}
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

        a10 := "start"
        defer fmt.Println(a10)
        a10 = "end"

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
  6. Infinite loop using _break_ keyword: `for { _break_ if some
  condition here is true }.

      _`break` can be used with a `label` to indicate where to return
      execution flow and can be useful with nested loops_

  7. Ignore an interation using _continue_ keyword if some condition is
  true.
  8. Looping through collections using _for ... range_, which works for
   strings, slices, arrays and maps.
      - `arr := [3]int{1, 2, 3}`
      - `for index/key, value := range arr {}`

    `See code samples in main.go`

## Pointers

- Are numerical representations of data addresses in memory.
- Created using an `asterisk` as prefix to a type.
- We can then use the _addressof_ to get the address of a variable.
- The `*` can also be used to retrive the value being referenced from
a pointer by dereferencing it i.e `*b` while the `&` can be used to
get the address a value that is stored at in memory i.e `&a`

  _Go although allowing variable pointers, does not allow pointer
  arithmetic like C/C++, to keep things simple_
  _There is however the `unsafe` package in Go, that can be used to
  achieve this but will not be checked by the compiler_
  _An uninitialized pointer has the value `nil`_
  _Pointers are responsible for the by-ref passing of slices and maps
  because they have internal pointers, which are copied along_

  `See code samples in main.go`

## Functions

- Blocks of code that implement specific logic within an application and
  are declared using the `func` keyword, followed by params brackets and
  curly braces denoting the functions body. `func() {}`
- Are first class citizens in Go that can be passed around like variables.

  _Go applications must have an entry point, in package main, with a main
  function (taking no args and returning no value)_

- Naming convention is similar to variables.
- Functions parameters are declared like normal variables without the
  `var` keyword, in the params brackets, separated by commas.

  _If multiple params have the same type, specify the type for the last one only_

- Params are normally passed by-value to functions, but pointers to
  other values can also be passed as well, in this case the value is passed by-ref.
- Passing values by ref using pointers can have perfomance
  improvemenets, if the data being passed to a function is large,
  instead of passing copies everytime the data is required.
- Variadic functions take an undefined number of arguments
  declared as `func(args ...int) {}` which adds all args passed in
  into a slice named _args_.
- Variadic parameters passed to a function can only be one and must
  be the last parameter passed in and be of the same type.
- A function's return type is specified after args braces:
 `func(arg type) type {}`
- Functions in Go can return local variables as pointers, that can
  be dereferenced in the calling code to access the underlying value.
- Since the local return value is held in the function's stack
  memory, returning values by-ref may not be safe in other
  programming languages because once the function returns, its
  stack memory is also cleared.
- In Go however, a function's pointer return value is promoted to
  the shared heap memory and will be available even after
  the function returns.
- For short functions, names return values may be result in cleaner
  code, because the return values do not have to be declared within
  the body of the func:
  `func(arg type) (returnVal type) {_return_}`
- You can return more than one return value in Go.

### Anonymous / Immediately invoked functions

- Used when using functions as types and declared as `func() {}()`,
  with the brackets after the body, imeediately invoking the
  function.
- They can be used to limit scope within another function in a
  bested structure or within a loop.
- Anonymous functions can also be assinged to variables and invoked
  from the varible of type _func()_:

  `var f func() = func() {}` or `f := func() {}`
  `f()`
- You can create custom anonymous function type signatures as well:

        var funcVar func(float64, float64) (float64, error)

        funcVar = func(a, b float64) (float64, error) {
          _function block code_
        }

### Methods

- Are functions that execute within known contexts _(types)_, and in
  Go, they can be associted with any type including primitives.

`See code samples in main.go`

## Interfaces

_In the real world, the implementation details of classes change,
 often quite substantially. If other classes are relying on the
 internal implementation details of the class, then code dependent
 on that class will start to malfunction when those details change.
  By defining an interface, a class promises other classes
  which depend on it "I will always have these properties and
  methods available, even if the details of how I execute them may
  change."_

- Intefaces in Go are automatically implemented, if the implementer
  has all the methods defined in the interface.
- Interfaces are types _(interface)_ just like structs, but unlike
structs which describe data, interfaces describe behaviour by
storing method definitions e.g from the Go i/o package

        type Writer interface {
            Write([]byte) (int, err)  // no. bytes written & err
        }

- Anything implementing the above interface will take the slice of
  bytes and write it somewhere e.g to console, tcp connenction or a
  file.
- To implement it we can define a console writer which will take
  the bytes slice and print to console e.g using a struct

        type ConsoleWriter struct {}

- In Go, interfaces are implicitly implemented by defining a method
  with a similar signature as an interface method and not by using
  keywords such as _implements_ e.g.

        func (cw ConsoleWriter) Write(data []byte) (int, error) {
            // Custom implementation of the interface

            n, err := fmt.Println(string(data))
            return n, err
        }

- We can then use the ConsoleWriter to write text to the console:

        func main() {
            var writerObj Writer = ConsoleWriter{}
            writerObj.Write([]byte("Hello Go"))
        }

- Interfaces drive polymorphism by enabling an object to take
  different forms depending on the implemetation of an interface i.e
  how it's methods are being overriden.
- In the above example, the writerObj defined can be a console
  writer, tcp writer or file writer depending on the implementation
  code _(the struct & its method in our case)_, but it will always
  write some bytes to some output.

### Naming Interfaces

- The name of an interface should reperesent what the interface
  does i.e:

  1. Single method interfaces: interface name is the _method name +
  `er`_ e.g. above example: method: `Write`; interface: `Writer`
  2. Multiple method interface: name interface by what it does.

- Name should begin with caps as well as the method names.

### Composing interfaces together (Similar to structs)

- This is a key feature for scalable coding in Go because of
single  method interfaces which while defineing very specific
behaviours, they are not very opinionated and thus can be
implemented in alot of ways.
- Composition adds other interface features into other in a sort of
 nesting that solves problems like requiring more methods in a
single-method interface but can't decompose the interface down.

- Type conversions can be performed on interfaces as well. For
instance the `WriterCloser` object used to print out text in the
sample code example can be cast into a `BufferedWriterCloser`
object to be able to access more info about it:

        newBWC, ok := wc.(*BufferedWriterCloser)

  // Check if the conversion succeeded so that the app does not
  panic (which is expensive), if the conversion fails:

        if ok { //investigate newBWC }
        else { // show the conversion failed }

### Empty Interface

- An interface defined on the fly that has no methods, using the
  syntax `interface{}` or `type interface {}` e.g

  var myObj interface{} = NewBufferedWriterCloser()

- Its useful when dealing with many types that are not compartible
  with each other and that would require some type checking later
  and is mostly used an intermediate conversion step.
- Objects of the empty interface will later require conversion into
  a useful object that has methods to implement.
- We can use a `type switch` to check an empty interface object:

        var i interface {} = true

        switch i.(type) {
          case int:
            // handle an int
          case string:
            // handle string
          default:
            // handle anything else
        }

### Method Sets for Pointers and Values

- When implementing an interface and we use a value type e.g `var
writerObj Writer = ConsoleWriter{}`, then all methods in the type,
must have `value receivers` i.e `func (obj ConsoleWriter) Method1()
{}` `func (obj ConsoleWriter) Method2() {}`.
- When implementing an interface and we use a pointer type e.g
`var writerObj Writer = &ConsoleWriter{}`, then the methods in
the type can both `pointer & value receivers` i.e `func (obj *ConsoleWriter)
Method1(){}` `func (obj ConsoleWriter) Method2() {}`.

_Pointers have access to the underlying type as well as the type's
data thus care should be taken when using pointer receivers in
methods as those methods can make alterations to the type_

### Best practices for working with interfaces

1. Use many small interface instead of few monolithic ones, then
compose them together if needing large ones.
2. Export concrete types instead of their interfaces for packages
that will be consumed by others and let them create the interfaces.
3. Do export interfaces for concrete types that I will be consuming.
4. Design functions and methods to receive interfaces whenever
possible so as to make them flexible.

`See code samples in main.go`

## Goroutines

- Most programming languages use OS threads, which have individual
 functions call stack, to handle code assigned to these threads.
- These call stacks tend to be large _about 1MB RAM_ and take a
while to set up applications, making creation and destruction of threads expensive.
- Go, on the hand uses, green threads which are an abstration of OS
threads called goroutines, which ensure we dont have to interact
with OS threads directly.
- The Go runtime has a scheduler that maps goroutines onto the OS
threads and takes turns with every available CPU thread, assigning
the various goroutines, a certian amount of processing time on
those threads.
- Because of this abstration, goroutines can start with very small
stack spaces because they can be reallocated quickly, making them
cheap to create and destroy.
- This allow the running of thousands or even tens of thousands of
goroutines to run at the same time, which is not possible with
languages that rely on large OS threads.
- Since Go has `closures` _(persistent scope which holds on to local
variables after the code execution has moved out of that block),_
goroutines _(functions executed using the `go` keyword)_ have
access to variable defined in parent scopes, even through the
goroutine and the parent scoped code, run in different execution
stacks. This can however create _race conditions_ and should be avoided:

          func main() {
            var msg string = "hello"

            go func() {   // anonymous func has access to msg var
                          // in different execution stack

              fmt.Println(msg)
            }()
            msg = "goodbye"   // gets printed because the
                              // main thread changes the var before
                              // the goroutine acts on it

            time.Sleep(100 * time.Millisecond)

          }

- The best way is to pass arguments into goroutines so that main
threaad and the goroutine are decoupled, because a copy of the value will be passed:

          func main() {
            var msg string = "hello"

            go func(msg string) {
              fmt.Println(msg)  // prints out OK
            }(msg)

            msg = "goodbye"
            time.Sleep(100 * time.Millisecond)

          }

- Using `Sleep` sync app execution to the real world clock which is
 unreliable and should not be used in production.
- The way to go is to use `Wait group` which syncs multiple
goroutines together by informing the `main thread` of existing
goroutines to sync with so that execution take just enough time to
remain efficient:

          var wg = sync.WaitGroup{}  // define the wait group

          func main() {
            var msg = "hello"
            wg.Add(1)  // register # of goroutines to wait for
            go func(msg string) {
              fmt.Println(msg)
              wg.Done()   // decrements the # of goroutines added
                         // to 0 so that the application can exit
            }(msg)
            msg = "goodbye"
            wg.Wait()   // Main goroutine to wait for the others
          }

_The main goroutine `running main()` just stores data and spawns other goroutines_

- While using still waitgroups, the goroutines even synced to how
they will access the common data, will still execute out of order
from what is expected. To fix this, use a `Mutex`.
- A mutex is a lock, that the application will honour. It is used
to protect data such that only one entity can have access to the
data at any one time.

### Parallelism

- By default Go will assign threads equal to the number of CPU cores
on the local machine.

_runtime.GOMAXPROCS(`int > 0`) is used to set the MAX number of
OS threads that can be executing simulteanously for an app._
_runtime.GOMAXPROCS(`int < 0`) is used to query the set MAX number
of OS threads_
_runtime.NumCPU() is used to query the available CPUs on the local machine_

- GOMAXPROCS is a tuning tool, to setting the right number of
threads for your application. 1:1 threads vs machine core count
should be the minimum and by adding more, the application tends to
 be faster. In production, profile the app with different values for
GOMAXPROCS to find the sweet spot.

`See code samples in main.go`

### Goroutine Best Practices

1. Don't create goroutines when creating libraries, rather let the
 consumers control the concurrency to avoid sync issues, unless you
function returns a channel, in which case the consumers will only
be listening for a return value.
2. Know how the goroutine will end, to avoid memory leaks because
of perpetual goroutines e.g by closing its channel in a `defer` or
a select statement.
3. Check for race conditions at compile time using `-race` flag
with `go run`, `go install` or `go build`

## Channels

- Make concurrency(ability to run asynchrounously) and parallelism
(running asynchronously) in Go shine.
- Channels allow data to be safely passed on between goroutines
in order to avoid issues like race conditions and memory sharing issues.
- Creating a channel: `ch := make(chan int)`
- Channels are also strongly typed, thus int channels can only
transmit ints, string > strings, pointers > pointers etc.
- Value copies are passed into a channel just like other primitives.
- For non-buffered channels, if multiple goroutines are sending
data into a channel but non is consuming the data and vice versa
then there will be a `deadlock` situation because one of the
goroutines will block the channel indefinately, attempting to write
to a non-empty channel or reading from an empty one.
- Below creates a deadlock because 5 goroutines will attempt to
write into the channel, while there is only one reading from the channel:

          go func() {
              i := <- ch
              // Do something with i
          }

          for j := 0; j < 5; j++ {
            go func() {
              ch <- 42
            }
          }

- The first goroutine with access to the channel on either end
blocks it for use and releases it to the others, once done.
- You can have goroutines read and write to and from a channel but
best practice is to designate writers and readers.
- Receiver goroutines declared as `go func(ch <- chan int) {}(ch)`
 and sender goroutines declared as `go func(ch chan <- int) {}(ch)`

### Buffered Channels

- Made to operate where senders and receivers operate at different
frequencies so that the channel is not blocked by the speedier goroutines.
- Use a for loop in the receiver goroutine to retrieve the values
from a buffered channel and ensure that the sender closes the
channel once doen writing, so that the receiver loop knows when to
stop iterating over the channel, otherwise there will be a deadlock
due to a non-terminating loop and hence non-terminating goroutine.

_Once a channel is closed, data cant be written to and an
attempt to will `panic` the application and the only remedy
here being to try a `recover`_
_You can however check on the receiving end whether or not the
channel is open or close by using the `, ok` within the for loop
just like with maps:

        go func(ch <- chan int) {
          for {
              if i, ok := <- ch; ok {
                 // continue reading in values
              } else {
                break
              }
          }
        }

### Select Statements

- We can a select statement to listen in on various channels for
messages and decide on execution flow based on which channel
responds first.
- A good example for this is when developing a goroutine terminate strategy.
- A select statement is syntactically similar to a switch but
applies to channels and cna be used without a `default` case
to ensure it blocks until a match is found.
- It blocks continuously if there are no messages from any of the monitored channels.
- If multiple channels receive a value simulteanously, then any one
of them will proceed _no rule on which one_
- A `default` makes the select non-blocking in which case if
matching case is not found the default executes and the select
exits.

`See code samples in main.go`

# Intro

- Developed by a team at Google comparising of Robert Griesemar, Rob Pike and
  Ken Thompson.
- "Developed while waiting for C++ programs to compile".
- Developed to build highly scalable and concurrent web applications.
- Developed due to limitiation of existing languages in use at Google at the
  time i.e Python (easy but slow), Java (fast but increasingly complex type
  system) and C/C++ (fast but slow compile times and increasingly complex type
  system)
- Concurrency is also patched into the the above languages.
- Weaknesses addressed and improvements included into Go are:

    1. Strong typed - variables types can't change over time
    2. Statically typed - variables types must be declared at compile time
    3. Fast - both compile and run times
    4. Concurrency built in
    5. Simple - also leaves out some complex features
    6. Memory managed and speed optimized gabarge collection
    7. Compiles into a single binary including dependancies
    8. Strong dev community

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

- Downloaded libraries `using $ go get <lib>` go into `~/go` (or golib), if the directory does not exist run `$ go get github.com/nsf/gocode` to download the syntax auto complete library.
- Add the folder to PATH so as to access the binaries via the `$ go` command:

    1. Add to .bashrc file the env varible called
       GOPATH `export GOPATH=/Users/kenneth/go`
    2. Update PATH with the new executable PATH `export PATH=$PATH:$GOPATH/bin`
    3. Source the bashrc file to update the changes to it `source ~/.bashrc

_The above ensure that the first segment of $GOPATH will be used by `go get <lib>`_

- Set up your workspace folder:

    1. Create a project folder with an _src_, _bin_ and _pkg_ folder to hold the source code, compiled binaries and dependancy that will be included in project binaries but do not need re-compling.
    2. Add the workspace folder above to GOPATH, similarly to the library folder
       above.

## Version controlling Go app

- Set up app folders using the `/go_workspace/github.com/<github_account_name>/app_folder`
  structure when using source control, to make the applications go gettable i.e
  downloadable using `go get <lib>`, since github will create a similar folder structure.

## Writing the first Go app

- Go files have a .go extension
- Packages are how go code is organised into sub-libraries. They are then importable
  into your existing go app to add functionality.
- All go app files must be part of a package, declared at the top of the file.
- Imported packages follow next in the `import {}` statement.
- A main package with a main function is a go's app entry point and is required
  for every go application.
- Use `go run <path to main.go>` to run a go app, which temporarily complies the
  application src files, then run the generated binary.
- Use `go build <path to package>` to compile the app package (app folder) into an
  executable in the main app folder(if it find a main package with a main function).
  The run the executable to run the app `./executable`
- Use `go install <path to an enty-point package>` to build an app binary into
  the _bin_ folder.

## Variables

- Declaring variables:

    1. `var <variable name> <variable type>` e.g _var i int = 2_ Explcit type
       declaration
    2. `<variable name> := <value`> e.g _i := 2_ the complier infers the type using the value

_- Only the explicit declaration syntax can be used to declare global variables
   but both can be used to declare local scope variables_
_- variables declared, must be used_
_- Uninitialized variables have a default value of 0(numericals), false(bools),  ""(text) and 0 + 0i(complex nums)_

- Declare a block of global scope variables:

    var (
        var1 string = "somestring"
        var2 int = 2
        var3 float32 = 23.9
        var4float64 = 33.9
    )

- Variable shadowing: an inner scope variable with the same name as a package/ global level, taking precedence.
- Lowecase first letter variables are scoped to _ONLY_ the package they are declared.
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

        _In go a string is a stream of bytes. Converting an int to a string i.i.e `var i int = 42` `j = string(i)` retrieves the unicode character represented by the int. Converting back and forth between string and int should be via the `strconv` package_

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
        - Int operators include: `+`, `-`, `*`, `/` (integer division and yields an int always) and `%` (the remainder)

    4. Bitwise operators: when comparing bit representation of two ints, they return
    the result of the set bit (1) comparison of the two, converted back into an int:

        a) `&` (and): _1 if both corresponding bits have been set_
        b) `|` (or): _1 if either of the corresponding bits have been set or both_
        c) `^` (exclusive or): _1 if either of the corresponding bits have been set
         but not both_
        d) `&^` (and not): _1 if neither of the corresponding bits have been set_

    5. Bit shifting is _adding or subtracting powers of 2.
        - If `a := 8` _2^3_ then:

            a) Left bit shifting: `a << 3` = `2^3 * 2^3` = `2^6` = 64
            b) Right bit shifting: `a >> 3` = `2^3 / 2^3` = `2^0` = 1

    6. Floating types: _comform to the IEEE 64 standard_

        a) `float32` _+-1.18E-38 <> +-3.4E38_
        b) `float64` _+-2.23E-308 <> +-1.8E308_

        _modulus, bitwise operators and bit shifting operators are not available to floats_

        `See code samples in main.go`

    7. Complex type: opens up go to be used for data science.

        a) `complex64` (float32 + float32 for the real & imaginary part)
        b) `complex128` (float64 + float64 for the real & imaginary part)

        `See code samples in main.go`

    8. Text types:

        a) string: are utf8 character thus can't encode all the characters. Are also a stream of bytes (uint8 chars). They are also an array of characters. Are also immutable.

        - String operations:

            - Concatenation: `string1 + string2`
            - Type conversion into bytes: `b := []byte(str)` convenient for tranferring strings or files across application and not worry about formating etc

        `See code samples in main.go for`

        b) rune: are utf32/int32 characters. It can be upto 32bits thus has operations used during encoding runes to know the actual length e.g a string (utf8) is aa valid rune.

        - Declared used single quotes e.g r := 'a'
        - Refer to the go docs for info on how to work with runes.

## Constants

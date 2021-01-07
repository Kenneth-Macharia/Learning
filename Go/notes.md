# Intro

- Developed by a team at Google comparising of Robert Griesemar, Rob Pike and Ken Thompson.
- "Developed while waiting for C++ programs to compile".
- Developed to build highly scalable and concurrent web applications.

## Why Go

- Developed due to limitiation of existing languages in use at Google i.e Python (easy but slow), Java (fast but increasingly complex type system) and C/C++ (fast but slow compile times and increasingly complex type system)
- Concurrency is also patched into the the above languages.
- Weaknesses addressed and improvements included into Go are:

    1. Statically typed
    2. Fast - both compile and run times
    3. Concurrency built in
    4. Simple
    5. Gabarge collected (memory managed)
    6. Compiles into a single binary including dependancies

## Setting up a Go local environment

- Using the binary availble on golang.org, install Go to _/usr/local/go_

_Check install location after installation using `$ which go`_

- Downloaded libraries `using $ go get <lib>` go into `~/go`, if the directory does not exist run `$ go get github.com/nsf/gocode` to download the auto complete libarary.
- Add the folder to PATH s as to access the binaries via the `$ go` command:

    1. Add to .bashrc file the env varible called GOPATH `export GOPATH=/Users/kenneth/go`
    2. Update PATH with the new executable PATH `export PATH=$PATH:$GOPATH/bin`
    3. Source the bashrc file to update the changes to it `source ~/.bashrc

_The above ensure that the first segment of $GOPATH will be used by `go get <lib>`_

- Set up the workspace folder:

    1. Create a project folder with an _src_, _bin_ and _pkg_ folder to hold the source code, compiled binaries and dependancy that will be included in project binaries but do not need re-compling.
    2. Add the workspace folder above to GOPATH, similarly to the library folder above.

## Version controlling Go app

- Set up app folders using the `/go_workspace/github.com/<github_account_name>/app_folder` structure when using source control, to make the applications go gettable i.e downloadable using `go get <lib>`, since github will create a similar folder structure.

## Writing the first Go app

- Go files have a .go extension
- Packages are how go code is organised into sub-libraries. The are then importable into your existing go app to add functionality.
- All go app files must be part of a package, declared at the top of the file.
- Imported packages follow next
- A main package with a main function is a go's app entry point and is required for every go application.
- Use `go run <path to main.go>` to run a go app, which temporarily complies the application src files, then run the generated binary.
- Use `go build <path to package>` to compile the app package (app folder) into an executable in the main app folder(if it find a main package with a main function). The run the executable to run the app `./executable`
- Use `go install <path to an enty-point package>` to build an app binary into the _bin_ folder.

## Variables

- Declaring variable:

    1. `var <variable name> <variable type>` e.g _var i int = 2_ Explcit type declaration
    2. `<variable name> := <value`> e.g _i := 2_ the complier infers the type using the value

_Only the explicit declaration su=yntax can be used to declare global variables but both can be used to declare local scope variables._
_variables declared, must be used_
_Uninitialized variables have a default value of 0(numericals), false(bools) or ""(text)_

- Declare a block of global scope variables:

    var (
        var1 string = "somestring"
        var2 int = 2
        var3 float32 = 23.9
        var4float64 = 33.9
    )

- Lowecase first letter variables are scoped to _ONLY_ the package they are declared in and cannot be used by importing packages while uppecase first letter variables are exported and can be used in importing packages.
- Naming convention rules:

    1. Length of the variable name reflects the life span of the variable e.g single letter names for loop counters and more descriptive names for longer lived variables.
    2. Acronyms such as URL should be in caps
    3. Use _PascalCase_ or _camelCase_

- Type conversions:

    1. int > float32: `f = float32(i)`
    2. float32 > int: `i = int(f)` _note this can lead to precision loss_
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

- Go insists on explicit type conversion even for close types e.g (int + int16) > (int + int(int16))
- Int operators include: `+`, `-`, `*`, `/` (yields an int always) and `%`

    4. Bit operators: when comparing bit representation of two ints, they return the result of the set bit (1) comparison of the two, converted back into an int:

        a) `&` : and _1 if both corresponding bits have been set_
        b) `|` : or _1 if either of the corresponding bits have been set or both_
        c) `^` : exclusive or _1 if either of the corresponding bits have been set but not both_
        d) `&^` : and not _1 if neither of the corresponding bits have been set_

    5. Bit shifting is _adding or subtracting powers of 2.
        - If `a := 8` _2^3_ then:

            a) Right bit shifting: `a << 3` = `2^6` = 64
            b) Left bit shifting: `a >> 3` = `2^0` = 1

    6. Floating types: _comform to the IEEE 64 standard_

        a) `float32` _+-1.18E-38 <> +-3.4E38_
        b) `float64` _+-2.23E-308<> +-1.8E308_

        _modulus, bit operators and bit shifting operators are not available to floats_

    7. Complex type: 

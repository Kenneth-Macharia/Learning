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
    6. Compiles into a single bunary including dependancies

## Setting up a Go local environment

- Using the binary availble on golang.org, install Go to _/usr/local/go_

_check install location after installation using `$ which go`_

- Downloaded libraries `using $ go get <lib>` go into `~/go`, if the directory does not exist run `$ go get github.com/nsf/gocode` to download the auto complete libarary.
- Add the folder to PATH s as to access the binaries via the `$ go` command:

    1. Add to .bashrc file the env varible called GOPATH `export GOPATH=/Users/kenneth/go`
    2. Update PATH with the new executable PATH `export PATH=$PATH:$GOPATH/bin`
    3. Source the bashrc file to update the changes to it `source ~/.bashrc

_the above ensure that the first segment of $GOPATH will be used by `go get <lib>`_

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

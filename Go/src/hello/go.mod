module hello

go 1.15

// used for finding module locally by replacing the import path from the
// actual module path declared in its go.mod file to the path specified

// **** ENSURE TO RUN $ go build TO LOCATE THE MODULE AND ADD IT AS A DEPENDANCY
replace greetings => ../greetings

require greetings v0.0.0-00010101000000-000000000000

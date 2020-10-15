# auto

If only the problems also got simpler by making this...

## Commands

1. run: Run a C/Cpp file

```
> ./auto run -h

usage: auto run [-h] [-i INPUT] [-o [OUTPUT]] program [args]

Compile and run the Cpp program

positional arguments:
  program               Name of the program you want to run, doesn't need the
                        cpp extension
  args                  arguments to be passed in to the program

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Name of the input file, default "input.txt"
  -o [OUTPUT], --output [OUTPUT]
                        Output file, default prints to stdout
```

2. compile: Compile your program

```
> ./auto compile -h

usage: auto compile [-h]

Utility to compile the Cpp program. Uses g++ by default

optional arguments:
  -h, --help  show this help message and exit
```

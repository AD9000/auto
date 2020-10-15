#!/usr/bin/env python3

from argparse import ArgumentParser, REMAINDER, OPTIONAL

parser = ArgumentParser(description="Your best friend when it comes to competitive programming")

# parser.add_argument('command')
# parser.add_argument('args', nargs=REMAINDER)
# runParser = ArgumentParser(description="Run it boi")

run = parser.add_subparsers(dest='command')


p = run.add_parser('run', description="Compile and run the Cpp program")

p.add_argument('program', help="Name of the program you want to run, doesn't need the cpp extension")

p.add_argument('-i', '--input', help="Name of the input file, default \"input.txt\"")

p.add_argument('-o', '--output', help="Output file, default prints to stdout", nargs=OPTIONAL)

p.add_argument('args', help="arguments to be passed in to the program", nargs=OPTIONAL)

# print(parser.parse_args())

comp = run.add_parser('compile', description="Utility to compile the Cpp program. Uses g++ by default")

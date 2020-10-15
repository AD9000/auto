#!/usr/bin/env python3

from argparse import ArgumentParser, REMAINDER

parser = ArgumentParser(description="Your best friend when it comes to competitive programming")

parser.add_argument('command')
parser.add_argument('args', nargs=REMAINDER)
# runParser = ArgumentParser(description="Run it boi")

# run = parser.add_subparsers(description="Compile and run the Cpp program")
# p = run.add_parser('run')

# p.add_argument('-d')



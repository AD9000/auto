#!/usr/bin/env python3
from subprocess import Popen, PIPE, run
import sys
import os

# compiler
from config import config
from .helpers import prettyPrint


def autocompile(progname, args=[], makefile: str = None) -> None:
    if (makefile):
        print("> make")
        # compile and run program
        make = Popen(['make'], stdout=PIPE, stderr=PIPE)
        out, err = map(bytes.decode, make.communicate())
    else:
        compiler = config['compiler']

        options = ['-Wall', '-Wextra', '-Wshadow', '-Wformat=2', '-Wfloat-equal', '-Wconversion', '-Wlogical-op', '-D_GLIBCXX_DEBUG', '-D_GLIBCXX_DEBUG_PEDANTIC',
                   '-D_FORTIFY_SOURCE=2', '-fsanitize=address', '-fsanitize=undefined', '-fno-sanitize-recover', '-fstack-protector', '-O2', '--std=c++14']

        makeArgs = [compiler, progname, *options]
        if args:
            makeArgs.extend(args)

        prettyPrint('Compiling...')
        print('>', ' '.join(makeArgs))
        make = Popen(makeArgs, stdout=PIPE, stderr=PIPE)
        out, err = map(bytes.decode, make.communicate())

        print()
        return out, err

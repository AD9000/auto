#!/usr/bin/env python3
from subprocess import Popen, PIPE, run
import sys
import os

# compiler
from config import config

def autocompile(makefile: str=None, args=[]) -> None:
  if (makefile):
    # compile and run program
    make = Popen(['make'], stdout=PIPE, stderr=PIPE)
    out, err = map(bytes.decode, make.communicate())
  else:
    compiler = config['compiler']

    options = ['-Wall', '-Wextra', '-Wshadow', '-Wformat=2', '-Wfloat-equal', '-Wconversion', '-Wlogical-op', '-D_GLIBCXX_DEBUG', '-D_GLIBCXX_DEBUG_PEDANTIC', '-D_FORTIFY_SOURCE=2', '-fsanitize=address', '-fsanitize=undefined', '-fno-sanitize-recover', '-fstack-protector', '-O2', '--std=c++14']
    

    make = Popen([compiler, *options, *args], stdout=PIPE, stderr=PIPE)
    out, err = map(bytes.decode, make.communicate())

    return out, err

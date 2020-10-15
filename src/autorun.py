#!/usr/bin/env python3

from subprocess import Popen, PIPE, run
import sys
import os
from .autocompile import autocompile
from .helpers import prettyPrint
from collections import defaultdict
import time


def runProg(progName, inp, args=[]):
    prog = Popen([progName, *args], stdout=PIPE, stderr=PIPE, stdin=PIPE)
    out, err = prog.communicate(input=inp.encode())
    s = prog.wait()
    return out, err


def checkOutput(out: bytes, err: bytes):
    if (out):
        print(out.decode(), end='')

    if (err):
        print(err.decode(), end='')
        return True


def autoRun(progName, args: list = [], options=defaultdict(lambda: None)):
    runParts = progName.split('.')
    runName = ''
    if (len(runParts) == 1):
        # add the cpp extension as default
        runName = progName
        progName += '.cpp'
    else:
        runName = ''.join(progName[:-1])

    args.extend(['-o', runName])
    out, err = autocompile(progName, args, options['makefile'])
    checkOutput(out, err)

    runMessage = ['./', runName]
    runMessage += [' < ', options['input']] if options['input'] else []

    # running the prog
    inp = options['input']
    if (inp):
        with open(inp) as fp:
            inp = fp.read()
    else:
        inp = ''

    prettyPrint("Input")
    print(inp)
    # print()

    prettyPrint(''.join(runMessage))
    runName = './' + runName

    out, err = runProg(runName, inp)
    checkOutput(out, err)

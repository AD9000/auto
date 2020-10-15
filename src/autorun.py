#!/usr/bin/env python3

from subprocess import Popen, PIPE, run
import sys
import os
from src.autocompile import autocompile
from collections import defaultdict


def autoRun(progName, args=[], options=defaultdict(lambda: None)):
  runParts = progName.split('.')
  runName = ''
  if (len(runParts) == 1):
    # add the cpp extension as default
    runName = progName
    progName += '.cpp'
  else:
    runName = ''.join(progName[:-1])
  
  out, err = autocompile(progName, args, options['makefile'])

  if (out):
    print (out, end='')

  if (err):
    print (err, end='')
    return

  # progName = ''.join(progName.split('.')[:-1])

  print('running:', runName)
  
  # running the prog
  inp = options['input']
  if (inp):
    with open(inp) as fp:
      inp = fp.read()
  else:
    inp = ''

  prog = Popen([runName], stdout=PIPE, stderr=PIPE)
  out, err = prog.communicate(input=inp)

  if (out):
    print (out, end='')

  if (err):
    print (err, end='')
    return

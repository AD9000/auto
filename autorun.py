#!/usr/bin/env python3

from subprocess import Popen, PIPE, run
import sys
import os
from autocompile import autocompile

def autoRun(makefile=None, args=[]):
  out, err = autocompile(makefile, args)

  if (out):
    print (out, end='')

  if (err):
    print (err, end='')
    return

    

    

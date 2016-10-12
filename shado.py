#!/usr/bin/env python

from __future__ import print_function

import sys
import os

def main(name, args):
    if name == 'shado':
       print("Running shado commands")
    else:
       print("Shadowing {}".format(name))


if __name__ == '__main__':
   main(sys.argv[0], sys.argv[1:])

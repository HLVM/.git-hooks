#!/usr/bin/env python
# NOTE this file MUST be inside the repo root directory and named ".whitespace-linter"

usage = """Whitespace linter
For the input file:
  1. finds tabs in file
  2. finds trailing whitespaces in line
Call: (help message)  whitespace-linter.py -h
      (verdict only)  whitespace-linter.py filename
      (error details) whitespace-linter.py filename -d
Could be used in Git hook scripts."""

import sys, os

argv = sys.argv[1:] # Could use argparse here, but I didn't bother.
if "-h" in argv:
    print(usage)
    sys.exit(0)
elif "-d" in argv:
    details = True
    argv.remove("-d")
else:
    details = False

num_args = len(argv) # argv does not have "-d" or "-h"
if num_args != 1:
    print("[Error] wrong number of argument: one file path needed, %d given" % num_args)
    print(usage)
    sys.exit(1)

filename = sys.argv[1]

if os.path.isdir(filename):
    print("[Error] path %s is a directory" % filename)
    sys.exit(1)
if not os.path.isfile(filename):
    print("[Error] file %s not found" % filename)
    sys.exit(1)

num_error, num_line = 0, 0
with open(filename, 'r') as f: # read-only
    line = ""
    prev_line = ""
    while True:
        line = f.readline()
        if len(line) == 0: # end of file
            break
        num_line += 1
        tab_count = line.count('\t') # for '\t'
        if tab_count != 0:
            num_error += 1
            if details:
                print("- Tab: %d tab%s on line %d" % (tab_count, 's' if tab_count > 1 else '', num_line))
        if len(line.rstrip()) != len(line.rstrip('\n')): # for trailing whitespaces
            num_error += 1
            if details:
                print("- Whitespace: trailing whitespaces on line %d" % num_line)
        prev_line = line

    if prev_line != "" and prev_line != "\n":
        pass # deactivated to indulge clang-format's behavior of removing last newline
        # num_error += 1
        # if details:
        #     print("- Newline missing: the last line is not \"\\n\"")

if num_error > 0 and not details:
    print("\t- %d whitespace error%s in file %s" % (num_error, 's' if num_error > 1 else '', filename))
    print("\t  for details: %s %s -d" % ("./.whitespace-linter", filename))
    sys.exit(1)

sys.exit(0)

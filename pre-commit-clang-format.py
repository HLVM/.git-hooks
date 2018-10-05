#!/usr/bin/env python
# Basically does git-clang-format's work, but I'd like to keep dependency small.

import os, sys, subprocess
import mygitutils, shouldvisit # my own

THIS_DIR = os.path.dirname(__file__)
FORMAT_UTIL = "clang-format"

files = mygitutils.get_staged_modified_in_tracked() # modified files (staged only)
if len(files) == 0:
    sys.exit(0)
for path in files:
    if shouldvisit.should_visit(path):
        print("\tvisit %s" % path)
        # -i: modify in-place
        if 0 != subprocess.call(" ".join([FORMAT_UTIL, "-i", path]), shell=True):
            print("[Error] error: %s -i %s" % (FORMAT_UTIL, path))
            sys.exit(1)
    else:
        print("\tskip  %s" % path)

# restage and exit
if 0 == subprocess.call(" ".join(["git add"] + files), shell=True):
    sys.exit(0)
else:
    print("[Error] error at re-running 'git add' after formatting")
    sys.exit(1)
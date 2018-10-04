#!/usr/bin/env python
# This script basically does git-clang-format's work, but I'd like to keep dependency small
# so I wrote my own

import os, sys, subprocess
import mygitutils, shouldvisit # my own

THIS_DIR = os.path.dirname(__file__)
FORMAT_UTIL = "clang-format"

# get tracked modified files (staged only)
files = mygitutils.get_staged_modified_in_tracked()

for path in files:
    if shouldvisit.should_visit(path):
        print("\tvisit %s" % path)
        subprocess.call(" ".join([FORMAT_UTIL, "-i", path]), shell=True) # -i: modify in-place
    else:
        print("\tskip  %s" % path)

sys.exit(0)
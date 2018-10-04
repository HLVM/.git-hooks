#!/usr/bin/env python

import os, sys, subprocess
import mygitutils, shouldvisit # my own

if len(sys.argv[1:]) != 1:
    print("[Error] need path to repo as argument")
    sys.exit(1)

REPO_DIR = sys.argv[1]
if not os.path.samefile(REPO_DIR, "."):
    print("[Error] you are not at project root")
    sys.exit(1)
LINTER_SCRIPT = os.path.join(REPO_DIR, ".whitespace-linter")
if not os.path.isfile(LINTER_SCRIPT):
    print("[Error] %s not found" % LINTER_SCRIPT)
    sys.exit(1)

# get tracked modified files (staged only)
files = mygitutils.get_staged_modified_in_tracked()

ret_sum = 0
for path in files:
    if shouldvisit.should_visit(path):
        print("\tvisit %s" % path)
        ret_sum += subprocess.call(" ".join([LINTER_SCRIPT, path]), shell=True)
    else:
        print("\tskip  %s" % path)

sys.exit(0 if ret_sum == 0 else 1)

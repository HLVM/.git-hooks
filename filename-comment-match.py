#!/usr/bin/env python
# Check whether filename matches with the
# file name in the head comment

import os, sys, re

if len(sys.argv[1:]) != 1:
    print("[Error] need path to repo as argument")
    sys.exit(1)

REPO_DIR = sys.argv[1]
if not os.path.samefile(REPO_DIR, "."):
    print("[Error] you are not at project root")
    sys.exit(1)

def check_filename(comment_filename, filename, line_num):
    if comment_filename != filename:
        print("[Error] %s line %d:" % (filepath, line_num))
        print("        filename in intro is \x1b[38;5;196m%s\x1b[0;m" % comment_filename)
        print("        but should be \x1b[38;5;155m%s\x1b[0;m" % filename)
        return False
    return True

INTERESTED_FILENAME_SUFFIXES = [
    ".cc", ".cpp", ".c", ".h",
    ".py", ".sh", ".js",
    ".json", ".yaml", ".yml", ".sch"
]
FILENAME_LINE = re.compile(r'\A(#|\s?\*)\s?(F|f)ile:\s+(.+)')
error_count = 0
for dirpath, _, filenames in os.walk("."):
    for filename in filenames:
        is_interested = False
        for suffix in INTERESTED_FILENAME_SUFFIXES:
            if filename.endswith(suffix):
                is_interested = True
                break
        if not is_interested:
            continue
        filepath = os.path.join(dirpath, filename)
        with open(filepath, 'r') as f:
            first_lines = [ f.readline() for _ in range(8)]
            for i, line in enumerate(first_lines):
                matchObj = FILENAME_LINE.match(line)
                if matchObj:
                    res = check_filename(matchObj.group(3), filename, i + 1)
                    if res == False:
                        error_count += 1
if error_count != 0:
    print("%d errors found" % error_count)
    sys.exit(1)

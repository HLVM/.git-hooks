#!/usr/bin/env python

import os, sys, subprocess

at_repo_root = ".git" in subprocess.check_output("ls -a", shell=True).split("\n")

if not at_repo_root:
    print("[Error] You are not at repo root, not allowed to push")
    sys.exit(1)

repo_name = subprocess.check_output("basename `git rev-parse --show-toplevel`", shell=True).decode('utf-8').strip()

PUSHCOUNT_FILE = "../.%s.push-count" % repo_name

if not os.path.isfile(PUSHCOUNT_FILE):
    print("[Error] %s not found, are you at the project root?" % PUSHCOUNT_FILE)
    sys.exit(1)

def increment():
    with open(PUSHCOUNT_FILE, 'r') as f: # read-only
        line = f.readline().strip()
        if not line.isdigit():
            print("[Error] the content in %s is empty or corrupt" % PUSHCOUNT_FILE)
            sys.exit(1)
        old_count = int(line)
    count = old_count + 1
    with open(PUSHCOUNT_FILE, 'w') as f: # write-only, erase original if existing
        f.write(str(count) + '\n')
    print("Push count for %s bumped: %d -> %d" % (repo_name, old_count, count))

# for testing
if __name__ == "__main__":
    increment();

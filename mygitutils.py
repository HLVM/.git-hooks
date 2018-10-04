#!/usr/bin/env python

import subprocess

# get tracked modified files (unstaged + staged)
"""
@return list
"""
def get_all_modified_in_tracked():
    COMMAND_STR = "{ git diff --name-only ; git diff --name-only --staged ; } | sort | uniq"
    out = subprocess.check_output(COMMAND_STR, shell=True)
    file_list = out.strip().split('\n') if len(out) != 0 else []
    return file_list

# get tracked modified files (staged only)
"""
@return list
"""
def get_staged_modified_in_tracked():
    COMMAND_STR = "{ git diff --name-only --staged ; } | sort | uniq"
    out = subprocess.check_output(COMMAND_STR, shell=True)
    file_list = out.strip().split('\n') if len(out) != 0 else []
    return file_list
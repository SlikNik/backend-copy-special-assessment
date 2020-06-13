#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "Nikal Morgan"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    specail_dir_files = []
    for file in os.listdir(dirname):
        # print(file)
        special_file = re.findall(r'__(\w+)__', file)
        # print(special_file)
        if special_file:
            specail_dir_files.append(os.path.abspath(file)) #os.path.abspath gets the absolute path for file
    # print(specail_dir_files)
    return specail_dir_files


def copy_to(path_list, dest_dir):
    # your code here
    return


def zip_to(path_list, dest_zip):
    # your code here
    return


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser() # -- or - is optional but with out is required or positional
    parser.add_argument('--todir', help='dest dir for special files') 
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    parser.add_argument('from_dir', help='find dir for special files')
    ns = parser.parse_args(args)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    if len(sys.argv) < 1:
        parser.print_usage()
    get_special_paths(ns.from_dir) #ns.from_dir this get files in directory given



if __name__ == "__main__":
    main(sys.argv[1:])

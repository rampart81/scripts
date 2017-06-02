#!/usr/bin/env python3

import fileinput
import re
import subprocess
import argparse

##
# Parse command line arguments
##
parser = argparse.ArgumentParser(description="Find and replce across mutiple files found by silver search")
parser.add_argument("search_text", help="text to replace for") 
parser.add_argument("replace_text", help="text to replace with")

args         = parser.parse_args()
search_text  = args.search_text
replace_text = args.replace_text

print("Searching " + search_text + " replacing with " + replace_text)

##
# Run silver search
##
file_names = subprocess.run(["ag", search_text, "-l"], stdout=subprocess.PIPE).stdout.decode("utf-8").split("\n")

##
# Compile th regex, find matches, and replace
##
pattern = re.compile(search_text)
for filename in file_names:
    if not filename: continue

    print("Processing " + filename)

    with fileinput.input(files = filename, inplace=True) as f:
        for line in f:
            line = pattern.sub(repl = replace_text, string = line.rstrip())
            print(line.rstrip())

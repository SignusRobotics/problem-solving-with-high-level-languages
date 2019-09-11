#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
# access commandline arguments
import sys
import glob

#text = (sys.argv[1])
#text = "test.txt"
# print(sys.argv[1])


def wc(text):
    """Counts lines, words, characters in a file. 

    Args: 
        text (filename): name of the filename. 

    """
    # antall linjer i fil
    a = 1
    # antall ord
    b = 0
    # antall tegn
    c = 0
    # open file:
    with open(text) as file:

        lines = [line.rstrip('\n') for line in file]
        a = len(lines)

        characters = []
        words = []

        for line in lines:
            for character in line:
                characters.append(character)
            for word in line.split():
                words.append(word)

        b = len(words)
        c = len(characters)
        return a, b, c


# antall words pr file
wordc = []
# filename
fname = []

for fn in glob.glob(sys.argv[1]):
    fname.append(fn)
    a, b, c = wc(fn)
    wordc.append(b)
    print("")
    print(f"{a} {b} {c} {fn} \n")

for i in range(0, len(wordc)):
    print("In ", fname[i], " there is ", wordc[i], " words. ")

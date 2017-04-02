
# -*- coding: utf-8 -*-
from collections import defaultdict
import re
#file = "allSuffixes.txt"

def get_suffixes(file):

    suffixes = defaultdict(dict)
    with open(file) as f:
        for line in f:
            if re.search(r'\(...\)', line):
                mline = line.split()
                morpheme = mline[1]
            if "-->" in line:
                sline = line.split()
                #suffixes[sline[-3][1]][sline[-1][1:-1]] = sline[1]
                suffixes[sline[-3][1]][sline[-1][1:-1]] = morpheme
    return suffixes

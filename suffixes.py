
# -*- coding: utf-8 -*-
from collections import defaultdict
#file = "allSuffixes.txt"

def get_suffixes(file):

    suffixes = defaultdict(dict)
    with open(file) as f:
        for line in f:
            if "-->" in line:
                sline = line.split()
                #suffixes[sline[-3][1]].append([sline[-1], sline[1]])
                suffixes[sline[-3][1]][sline[-1][1:]] = sline[1]
    return suffixes

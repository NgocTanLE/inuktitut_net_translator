
# -*- coding: utf-8 -*-
from collections import defaultdict
import re
import pdb
import pickle
#file = "allSuffixes.txt"

""" The problem if we use this is 
  we can't get back the root original value
"""

def get_suffixes(file):

    suffixes = defaultdict(dict)
    with open(file) as f:
        for line in f:
            if re.search(r'\(...\)', line):
                mline = line.split()
                morpheme = mline[1]
                if morpheme == "liq":
                    pdb.set_trace()
            if "-->" in line:
                sline = line.split()
                #suffixes[sline[-3][1]][sline[-1][1:-1]] = sline[1]
                if sline[-1][1] == 'V':
                    for c in ['a','i','u','e','o']:
                        suffixes[c+sline[-1][2:-1]] = (morpheme,[c])
                else:
                    if sline[-1][1:-1] in suffixes:
                       morpheme, melted_char = suffixes[sline[-1][1:-1]]
                       if sline[-3][1:2] not in melted_char:
                           melted_char.extend(sline[-3][1:2])
                       suffixes[sline[-1][1:-1]] = (morpheme,melted_char)
                    else:
                        suffixes[sline[-1][1:-1]] = (morpheme,[sline[-3][1:2]])
    return suffixes

output_dict_filename = "helper_data/changing_suffixes_dict.p"
output_dict = open(output_dict_filename,"wb")



filename = "helper_data/allSuffixes.txt"
suffixes = get_suffixes(filename)
pickle.dump(suffixes,output_dict)

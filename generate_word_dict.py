""""
This script is used to generate root and suffixes dictionary that help us segmenting each word in inuktitut
"""

import pdb
import numpy as np
from sets import Set
import pickle

input_suffix = "helper_data/suffixes.en.txt"
input_roots = "helper_data/roots.en.txt"
output_suffix = "helper_data/suffixes_dict.p"
output_roots = "helper_data/roots_dict.p"
output_all = "helper_data/all_dict.p"


suffix_file_in = open(input_suffix,"r")
suffix_file_out = open(output_suffix,"wb")
roots_file_in = open(input_roots,"r")
roots_file_out = open(output_roots,"wb")
output_all_out = open(output_all,"wb")
# Reading suffix file
suffixes = Set()
for line in suffix_file_in:
    suff = line.strip().split(" ",1)[0].split("/")[0]
    suffixes.update(suff)
pickle.dump(suffixes,suffix_file_out)

# Reading roots file
roots = Set()
for line in roots_file_in:
     root = line.strip().split(" ",1)[0].split("/")[0]
     roots.update(root)
pickle.dump(roots,roots_file_out)

suffixes.union(roots)
pickle.dump(suffixes,output_all_out)



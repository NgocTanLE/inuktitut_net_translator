""""
This script is used to generate root and suffixes dictionary that help us segmenting each word in inuktitut
"""

import pdb
import numpy as np
# from sets import Set
import pickle

input_suffix = "helper_data/suffixes.en.txt"
input_roots = "helper_data/roots.en.txt"
output_suffix = "helper_data/suffixes_dict.p"
output_roots = "helper_data/roots_dict.p"
output_all = "helper_data/all_dict.p"
melted_dict_filename = "helper_data/melted_dict.p"
unmelted_word_filename = "helper_data/unmelted_dict.p"


suffix_file_in = open(input_suffix,"r")
suffix_file_out = open(output_suffix,"wb")
roots_file_in = open(input_roots,"r")
roots_file_out = open(output_roots,"wb")
output_all_out = open(output_all,"wb")
melted_file_dict = open(melted_dict_filename,"wb")
unmelted_file_dict = open(unmelted_word_filename,"wb")

# Reading suffix file

melted_dict = {}
unmelted_list = []
suffixes = set()
for line in suffix_file_in:
    suff = line.strip().split(" ",1)[0].split("/")[0]
    if len(suff)>1:
        unmelted_list.append(suff)
        melted_dict[suff[:-1]] = suff
        suff = suff[:-1]

    suffixes.add(suff)
pickle.dump(suffixes,suffix_file_out)

# Reading roots file
roots = set()
for line in roots_file_in:
     root = line.strip().split(" ",1)[0].split("/")[0]
     if len(root)>1:
        unmelted_list.append(root)
        melted_dict[root[:-1]] = root
        root = root[:-1]
     roots.add(root)
pickle.dump(roots,roots_file_out)
all_set = suffixes | roots
pickle.dump(all_set,output_all_out)
output_all_out.close()

pickle.dump(melted_dict,melted_file_dict)
pickle.dump(unmelted_list,unmelted_file_dict)

melted_file_dict.close()
unmelted_file_dict.close()
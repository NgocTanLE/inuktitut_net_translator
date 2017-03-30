"""
    This script is used to segmentation each word in the corpus and save it
"""
import pickle
import pdb

output_suffix = "helper_data/suffixes_dict.p"
output_roots = "helper_data/roots_dict.p"
output_all = "helper_data/all_dict.p"
bucket_in_filename = "in_ed_data_50000/bucket_{0:d}.list"
small_in_filename = "in_en_data/text_all.fr"

#for i in range(9):
#    pickle.load(bucket_in_filename.format(i+1)

seg_set = pickle.load(open(output_all,"rb"))
small_file = open(small_in_filename,"r")


def segment_sentence(sentence):
    seg_sentence = []
    slotter = ""
    len_sentence = len(sentence)
    for c in sentence:
        slotter += c
        if slotter in seg_set:
            seg_sentence.append(slotter)
            slotter = ""

for lin in small_file:
    

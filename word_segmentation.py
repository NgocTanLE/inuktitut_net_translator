"""
    This script is used to segmentation each word in the corpus and save it
"""
import pickle
import pdb

output_suffix = "helper_data/suffixes_dict.p"
output_roots = "helper_data/roots_dict.p"
output_all = "helper_data/all_dict.p"
bucket_in_filename = "in_en_data_50000/buckets_{0:d}.list"
small_in_filename = "in_en_data/text_all.fr"
num_buckets = 2
#for i in range(9):
#    pickle.load(bucket_in_filename.format(i+1)

seg_set = pickle.load(open(output_all,"rb"))
small_file = open(small_in_filename,"r")

def segment(wdict,word):
   word_len = len(word)
   idx = word_len-2
   while idx>0: 
           if word[:idx] in wdict:
                   return word[:idx],word[idx+1:]
  # if idx == 0: # the word is unable to segmented
   return None,word

def segment_word(wdict, word):
   """ Find a segmentation for a longer words
    e.g living|HereWithSome
    return : living, hereWithSome
   """
   rest_buck = []
   seg_buck = []
   act_buck = word
   while act_buck:
           seg, rest = segment(wdict, act_buck)
           if seg: # segment will return value if it successfully segmented word
              seg_buck += seg 
              act_buck = res + rest_buck
           else: # it will not return value if it's not segmented correctly
              rest_buck = act_buck 
              act_buck = seg_buck[-1] # go backward one step
   return seg_buck 


def segment_sentence(wdict,sentence):
    seg_sentence = []
    segmented_sentence = []
    for word in sentence:
        segmented_word = segment_word(wdict,word)
        segmented_sentence.append(segmented_word)
    return segmented_sentence


# reading bucket data
bucket_data=[]
for buck_indx in  range(num_buckets):
#   bucket_data = pickle.load(open(bucket_in_filename.format(buck_indx+1),"rb"))
    bucket_filename = bucket_in_filename.format(buck_indx+1)
    bucket_data = pickle.load(open(bucket_filename,"rb"))
    pdb.set_trace()


"""
    This script is used to segmentation each word in the corpus and save it
"""
import pickle
import pdb
import os

output_suffix = "helper_data/suffixes_dict.p"
output_roots = "helper_data/roots_dict.p"
output_all = "helper_data/all_dict.p"

bucket_in_filename = "in_en_data_50000/buckets_{0:d}.list"
small_in_filename = "in_en_data/text_all.fr"
changing_suffixes_filename = "helper_data/changing_suffixes_dict.p"
melted_dict_filename = "helper_data/melted_dict.p"
unmelted_word_filename = "helper_data/unmelted_dict.p"


num_buckets = 1
NUM_SENTENCES = 50000
UNK_ID = 3

flag= {"SEGMENTED":1, "UNSEGMENTED":-1,"SEGMENTED_MELT":2}

#for i in range(9):
#    pickle.load(bucket_in_filename.format(i+1)

seg_set = pickle.load(open(output_all,"rb"))
small_file = open(small_in_filename,"r")

def finding_in_dict(word_dict,word, melted=False):
   """ Segment word based on the longest one"""
   word_len = len(word)
   idx = word_len
   while idx>0: 
           print("trying to find {} in dict".format(word[:idx]))
           # pdb.set_trace()
           # pdb.set_trace()  
           token = word[:idx]
           after_token = word[idx:]
           if token in word_dict:
                if melted:
                  suff, melted_char = word_dict[token]
                  return flag["SEGMENTED_MELT"], suff, after_token, melted_char, 
                else:
                  return flag["SEGMENTED"],token,after_token,None
           idx-=1
   return flag["UNSEGMENTED"], None,None,None

melted_word_dict = pickle.load(open(melted_dict_filename,"rb"))
unmelted_word_list = pickle.load(open(unmelted_word_filename,"rb"))

all_dict = pickle.load(open(output_all,"rb"))

def check_melted(word):
    if word in unmelted_word_list: # check the avability of the word, check in in unmelted dict
        print("right combination of melted ",word)
        return word
    elif word[:-1] in melted_word_dict:
        print("wrong combination of melted ",word,"-->",melted_word_dict[word[:-1]])
        return melted_word_dict[word[:-1]]
    print("not found in melted and unmelted ",word)
    return None


def segment_word(root_dict, suffix_dict, word):
   """ Find a segmentation for a longer words
    e.g living|HereWithSome
    return : living, hereWithSome
   """
   segmented_word = []

   ### find root
   issegment, segment, rest, _ = finding_in_dict(root_dict, word)
   if issegment==flag["SEGMENTED"] and rest:
    segmented_word.append(segment)
   else:
     return [word] # return exact word

   ### find suffixes
   word = rest

   while word:
      print(".... segmenting ",word)
      issegment, segment, rest, melted_list = finding_in_dict(suffix_dict, word, True)
      if segment and len(segment) >= len(word):
        # pdb.set_trace()
        combined_word = check_melted( segmented_word[-1] + word )
        if combined_word:
          segmented_word[-1] = combined_word

        break

      if issegment == flag["SEGMENTED_MELT"]:
        # add metled char inside the word
        for melted_char in melted_list:
           # pdb.set_trace()
           combined_word = str(segmented_word[-1]) + melted_char
           print("suffixe",segment, ",melted char", melted_char ,",combine word",combined_word)
           # check our melted word into the dict
           # check if the word combination is correct
           combined_word = check_melted(combined_word)
           if combined_word:
              print("combined word",combined_word)
              segmented_word[-1] = combined_word
              segmented_word.append(segment)
              break
        word = rest
      elif issegment == flag["SEGMENTED"]: 
        segmented_word.append(segment)
        word = rest
      else:
        # increase the index by 1
        word = word[1:]

   return segmented_word 


def translate_word_to_index(w2i,sentences):
    new_sentence  = []
    for sentence in sentences:
      for word in sentence:
        new_sentence.append(w2i["fr"].get(word.encode(),UNK_ID))
    return new_sentence

def segment_sentence(root_dict,suffix_dict,i2w,sentence):
    seg_sentence = []
    segmented_sentence = []
    for word in sentence:
        # iterating over word
        word = i2w["fr"][word].decode()
        print("translating {}".format(word))
        segmented_word = segment_word(root_dict,suffix_dict,word)
        segmented_sentence.append(segmented_word)
    return segmented_sentence



model_dir = os.path.join("in_en_model_{0:d}".format(NUM_SENTENCES))
input_dir = os.path.join("in_en_data_{0:d}".format(NUM_SENTENCES))
data_dir = os.path.join("in_en_data")

w2i_path = os.path.join(input_dir, "w2i.dict")
i2w_path = os.path.join(input_dir, "i2w.dict")
w2i = pickle.load(open(w2i_path, "rb"))
i2w = pickle.load(open(i2w_path, "rb"))

root_dict = pickle.load(open(output_roots,"rb"))
suffix_dict = pickle.load(open(output_suffix,"rb"))
suffixes_melted_dict = pickle.load(open(changing_suffixes_filename,"rb"))
pdb.set_trace()

# reading bucket data
bucket_data=[]
for buck_indx in  range(num_buckets):
#   bucket_data = pickle.load(open(bucket_in_filename.format(buck_indx+1),"rb"))
    bucket_filename = bucket_in_filename.format(buck_indx+1)
    bucket_data = pickle.load(open(bucket_filename,"rb"))

for line in bucket_data:
        data = line[0]
        out = segment_sentence(root_dict, suffixes_melted_dict, i2w, data)
        print("-------")
        print(line)
        print(out)        
        out=translate_word_to_index(w2i,out)
        print(out)        
        pdb.set_trace()

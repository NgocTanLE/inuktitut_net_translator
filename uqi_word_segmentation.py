import pickle
import pdb
import os
import re

bucket_in_filename = "in_en_data_50000/buckets_{0:d}.list"


num_buckets = 9
NUM_SENTENCES = 50000
UNK_ID = 3

input_dir = os.path.join("in_en_data_{0:d}".format(NUM_SENTENCES))
data_dir = os.path.join("in_en_data")

w2i_path = os.path.join(input_dir, "w2i.dict")
i2w_path = os.path.join(input_dir, "i2w.dict")


import subprocess
def segmenting(word):
   call = ['java', '-jar', 'Uqailaut.jar', word]
   # ret = subprocess.call(call, stdout=subprocess.PIPE, stderr=None)
   try:
      ret = subprocess.Popen(call,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT)
   except:
       pdb.set_trace()
   # if ret > 0:
   #    print("Warning - result was",ret)
   #    return -1
   return ret.stdout

def cut_sentence(sentence):
    # pdb.set_trace()
    l_sen  = sentence.strip().replace('{','').split("}")[:-1]
    l_sen = [re.sub(':.*$','',l) for l in l_sen]
    return l_sen

def append_dict(words,w2i,i2w):
    for word in words:
        if word.encode() not in w2i["fr"]:
            last_idx = len(w2i["fr"].keys())-1
            w2i["fr"][word.encode()] = last_idx + 1
            i2w["fr"][last_idx+1] = word.encode()

def save_to_file(segmented_sentences):
    filename = "in_segment_data_5000/text.en"
    fd = open(filename,"w")
    for sentence in segmented_sentences:
        fd.write(' '.join(sentence)+"\n")
    fd.close()

bucket_data=[]
idx_to_take = 0
# for idx,buck_indx in  enumerate(range(num_buckets)):
w2i = pickle.load(open(w2i_path, "rb"))
i2w = pickle.load(open(i2w_path, "rb"))
segmented_sentences = []
#   bucket_data = pickle.load(open(bucket_in_filename.format(buck_indx+1),"rb"))
# bucket_filename = bucket_in_filename.format(buck_indx+1)
# bucket_data = pickle.load(open(bucket_filename,"rb"))
data = open("in_en_data/text_all.fr")
i=0
for idx,sentence in enumerate(data):
    sentence = sentence.strip().split()
    sentence_list = []
    for word in sentence:
            translated_words = []
            for line in segmenting(word):
                translated_words.append(line.decode())

            if len(translated_words)>0 and translated_words[0]!='\n':
                translated_words = cut_sentence(translated_words[idx_to_take])
            else:
                translated_words = [word]
            append_dict(translated_words,w2i,i2w)    
            
            # translated_words = [w2i["fr"].get(word.encode(),UNK_ID) for word in translated_words]              
            sentence_list.extend(translated_words)
            # print(word,' -> ', [i2w["fr"][w].decode() for w in translated_words])
    print(idx,' ',sentence_list)
    segmented_sentences.append(sentence_list)
    if idx%500==0:
        save_to_file(segmented_sentences)

# coding: utf-8

from collections import defaultdict
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sys
import pickle


# because the vocabulary has been previously processed
# and everything that appeared just once has been marked as UNK
v = pickle.load(open("data/vocab.dict", "rb"))
v_en = v["en"]
v_jp = v["fr"]

def read_input(fname, fname2):

    data = []
    for fnamex in [fname, fname2]:
        # define objects to store
        words = defaultdict(int)
        sent_lengths = []
        with open(fnamex, "r") as f:
            # count occurrences of each word
            for line in f:
                sline = line.split()
                sent_lengths.append(len(sline))
                for word in sline:
                    words[word] += 1
            types = len(words)
            tokens = sum(words.values())
            # count unk words and its length
            # count less than the pre-processed text
            # don't really know why
            # unk = 0
            # for i in words:
            #    if words[i] == 1:
            #        unk += 1

        data.append([sent_lengths, types, tokens])

    unk_en = data[0][1] - len(v_en)
    unk_jp = data[1][1] - len(v_jp)
    data[0].append(unk_en)
    data[1].append(unk_jp)


    sns.distplot(data[0][0])
    plt.xlabel("length")
    plt.ylabel("frequency")
    plt.title("English sentences length distribution")
    plt.grid(True)
    plt.xticks()
    #plt.savefig("english_distribution.png")
    sns.plt.show()

    sns.distplot(data[1][0])
    plt.xlabel("length")
    plt.ylabel("frequency")
    plt.title("Inuktitut sentences length distribution")
    plt.grid(True)
    #plt.savefig("inuktitut_distribution.png")
    sns.plt.show()

    sns.distplot(data[0][0], color='b')
    sns.distplot(data[1][0], color='g')
    plt.xlabel("length")
    plt.ylabel("frequency")
    plt.title("English Inuktitut sentences length distribution")
    plt.grid(True)
    #plt.savefig("english_inuktitut_distribution.png")
    sns.plt.show()

    s1 = np.array(data[0][0])
    s2 = np.array(data[1][0])
    sns.jointplot(s1, s2, kind="reg")
    plt.grid(True)
    #plt.savefig("english_inuktitut_correlation.png")
    sns.plt.show()

    sys.stderr.write("\ntypes - L1: "+str(data[0][1])+", L2: "+str(data[1][1]))
    sys.stderr.write("\ntokens -  L1: "+str(data[0][2])+", L2: "+str(data[1][2]))
    sys.stderr.write("\ntype-token ratios -  L1: "+str(round((data[0][1]/data[0][2])*100,3))+"%"+
                     ", L2: "+str(round((data[1][1]/data[1][2])*100,3))+"%")
    sys.stderr.write("\nUNK words - L1: "+str(data[0][3])+", L2: "+str(data[1][3]))

    return data

# def compare(data):
#     sys.stderr.write("\ntypes - L1: "+str(data[0][2])+", L2: "+str(data[1][2]))
#     sys.stderr.write("\ntokens -  L1: "+str(data[0][3])+", L2: "+str(data[1][3]))
#     sys.stderr.write("\ntype-token ratios -  L1: "+str(data[0][2]/data[0][3])+
#                      ", L2: "+str(data[1][2]/data[1][3]))
#     sys.stderr.write("\nunk words - L1: "+str(data[0][4])+", L2: "+str(data[1][4]))
#     plt.plot(data[0][0], 'g-', data[1][0], 'b-')
#     plt.show()
#     pass

# import hw2_1b as h
# x = h.read_input("data/text.en", "data/text.fr")
# h.compare(x)

#########################################################################

# Plot the distribution of sentence lengths
#    in the English
#    and Japanese
#    and there correlation.
#    What do you infer from this about translating between these languages?

# How many word tokens are in the English data?
# In the Japanese?

# How many word types are in the English data?
# In the Japanese data?

# How many word tokens will be replaced by _UNK in English?
# In Japanese?

# Given the observations above,
# how do you think the NMT system will be affected by differences in
#       sentence length,
#       type/ token ratios, and
#       unknown word handling?

#!/usr/bin/env python
import DEFINES
import ArraysBuilder
import ToolMenagemnt
import plot

import datetime
import random
import subprocess
import os
import matplotlib.pyplot as plt

#mistakes
MAX_DEL=0; MIN_DEL=0;
MAX_MIXED=0; MIN_MIXED=0;
MAX_RAND_DEL=0; MIN_RAND_DEL=0;
MAX_FLIP_PER=0; MIN_FLIP_PER=0; FLIP_STEP_PER=0;

#overlaps
MAX_OVERLAP_PER=0.8; MIN_OVERLAP_PER=0.1; OVERLAP_STEP_PER=0.1;
MAX_OVERLAP_NUM=1; MIN_OVERLAP_NUM=1;

#parts
MIN_PART_LEN_PER=0.05; MAX_PART_LEN_PER=0.4; MAX_PART_LEN=700; PART_LEN_STEP=0.05;



#---------------------------------main---------------------------------------
time_start = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")


num_of_overlap_tests=0; num_of_minlen_tests=0;


#string creation
sourceString=[]
for x in range(DEFINES.STRING_LEN):
    r=random.random();
    if r>0.5: sourceString.append('1')
    else: sourceString.append('0')
sourceString=''.join(sourceString)

#DEBUG
# noMistakes_statvec_ser = {"X": [], "Y": [], "Z": []}  # X for parts, Y for overlap, Z for succsess
# noMistakes_statvec_ser['Z'].append([])
# arr = ArraysBuilder.serialOverlap_arr(string=sourceString, parts=2, overlap=0.4)
# ToolMenagemnt.run_plass(arr=arr, x=2, y=0.4, res_vec=noMistakes_statvec_ser, source=sourceString)


#serial overlap: over parts and overlaps. no mistakes
if DEFINES.SERIAL_OVERLAP_MOD: #serial overlap - no mistakes:
    overlap = MIN_OVERLAP_PER;
    noMistakes_statvec_ser = {"X": [], "Y": [], "Z": []}  # X for parts, Y for overlap, Z for succsess
    while overlap<MAX_OVERLAP_PER:
        parts = 2;
        noMistakes_statvec_ser['Z'].append([])
        while(parts< 7):#int(0.05*DEFINES.STRING_LEN)):
            arr=ArraysBuilder.serialOverlap_arr(string=sourceString, parts=parts, overlap=overlap)
            print arr
            ToolMenagemnt.run_plass(arr=arr, x=parts, y=overlap, res_vec=noMistakes_statvec_ser, source=sourceString)
            parts+=1
        noMistakes_statvec_ser['Y'].append(overlap)
        overlap+=OVERLAP_STEP_PER
        num_of_overlap_tests+=1
    plot.py_plotAll(num_of_overlap_tests,res=noMistakes_statvec_ser,g_ind=0,mis_name="NO mistakes - Serial",avg=False,scatter=False,hist=True)


#random v_version: over min_length and parts. no mistakes
if DEFINES.RANDOM_OVERLAP_MOD:#random overlap - no mistakes:
    minlen=MIN_PART_LEN_PER
    noMistakes_statvec_rand = {"X": [], "Y": [], "Z": []}  # X for parts, Y for overlap, Z for succsess
    while minlen*len(sourceString) < min(MAX_PART_LEN,MAX_PART_LEN_PER*len(sourceString)):
        parts = 2;
        noMistakes_statvec_rand['Z'].append([])
        while(parts<int(0.05*DEFINES.STRING_LEN)):
            arr= ArraysBuilder.allOverlap_randomLen(string=sourceString,
                                                 parts=parts,
                                                 min_len_per=minlen,
                                                 max_len_per=MAX_PART_LEN_PER,
                                                 min_overlap_per=MIN_OVERLAP_PER)
            ToolMenagemnt.run_plass(arr=arr, x=parts, y=minlen, res_vec=noMistakes_statvec_rand, source=sourceString)
            parts+=1
        noMistakes_statvec_rand["Y"].append(minlen);
        minlen+=PART_LEN_STEP
        num_of_minlen_tests+=1
    plot.py_plotAll(num_of_mis=num_of_minlen_tests,res=noMistakes_statvec_rand,g_ind=2,mis_name="NO mistakes - Random",avg=False,scatter=False,hist=True)

#
# #to d0 - - - - - - -NIV's Random
# if DEFINES.RANDOM_OVERLAP_MOD:#random overlap - no mistakes:
#     minlen=MIN_PART_LEN_PER
#     noMistakes_statvec_rand = {"X": [], "Y": [], "Z": []}  # X for parts, Y for overlap, Z for succsess
#     while minlen*len(sourceString) < min(MAX_PART_LEN,MAX_PART_LEN_PER*len(sourceString)):
#         parts = 2;
#         noMistakes_statvec_rand['Z'].append([])
#         while(parts<int(0.05*DEFINES.STRING_LEN)):
#             arr= ArraysBuilder.allOverlap_randomLen(string=sourceString,
#                                                  parts=parts,
#                                                  min_len_per=minlen,
#                                                  max_len_per=MAX_PART_LEN_PER,
#                                                  min_overlap_per=MIN_OVERLAP_PER)
#             ToolMenagemnt.run_plass(arr=arr, x=parts, y=minlen, res_vec=noMistakes_statvec_rand, source=sourceString)
#             parts+=1
#         noMistakes_statvec_rand["Y"].append(minlen);
#         minlen+=PART_LEN_STEP
#         num_of_minlen_tests+=1
#     plot.py_plotAll(num_of_mis=num_of_minlen_tests,res=noMistakes_statvec_rand,g_ind=2,mis_name="NO mistakes - Random",avg=False,scatter=False,hist=True)

# # #flips #not to do yet
# # if DEFINES.FLIP_MOD:
# #     flips=MIN_FLIP_PER
# #     if DEFINES.SERIAL_OVERLAP_MOD:
# #
# #     if DEFINES.RANDOM_OVERLAP_MOD:
# #
# # # flips
# # if DEFINES.FLIP_MOD:
# #     flips = MIN_FLIP_PER
# #     if DEFINES.SERIAL_OVERLAP_MOD:
# #
# #     if DEFINES.RANDOM_OVERLAP_MOD:
#
plt.show()


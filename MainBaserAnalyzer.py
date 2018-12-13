#!/usr/bin/env python
import DEFINES
import MATLAB
import ArraysBuilder
import ToolMenagemnt
import plot

import shutil
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
MIN_PART_LEN_PER=0.2; MAX_PART_LEN_PER=0.4; MAX_PART_LEN=700; PART_LEN_STEP=0.05;



#---------------------------------main---------------------------------------
time_start = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

#delete exist file
if os.path.exists(DEFINES.PATH_FILES + "out/" + DEFINES.FILE_OUT_NAME + ".fas"):
    os.remove(DEFINES.PATH_FILES + "out/" + DEFINES.FILE_OUT_NAME + ".fas")
if os.path.exists(DEFINES.PYTHON_PATH + "tmp/"):
    os.chmod(DEFINES.PYTHON_PATH + "tmp", 0o777)
    shutil.rmtree(DEFINES.PYTHON_PATH + "tmp")

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


#serial overlap:
# ------varient parts and overlaps
# ------no mistakes
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
    plot.py_plotAll(res=noMistakes_statvec_ser,g_ind=0,mis_name="NO mistakes - Serial",avg=False, xlabel="parts", ylabel="overlap",scatter=False,hist=True)
    MATLAB.makeMATLAB("sereal_no_mis",noMistakes_statvec_ser['Z'],2,7, MIN_OVERLAP_PER,MAX_OVERLAP_PER,"parts","overlap_per","succsess", 1, OVERLAP_STEP_PER);

#samples creation: of random index and const lngth
if DEFINES.RANDOM_SAMPLE_MOD:
    constlen=MIN_PART_LEN_PER
    noMistakes_statvec_randIndx = {"X": [], "Y": [], "Z": []}  # X for parts, Y for overlap, Z for succsess
    while constlen< MAX_PART_LEN_PER:
        parts = 2;
        noMistakes_statvec_randIndx['Z'].append([])
        while (parts < 7):  # int(0.05*DEFINES.STRING_LEN)):
            arr = ArraysBuilder.randomSample_constLen(string=sourceString, parts=parts, constlen=constlen)
            ToolMenagemnt.run_plass(arr=arr, x=parts, y=constlen, res_vec=noMistakes_statvec_randIndx, source=sourceString)
            parts += 1
        noMistakes_statvec_randIndx['Y'].append(constlen)
        constlen += PART_LEN_STEP
    plot.py_plotAll(res=noMistakes_statvec_randIndx, g_ind=2, mis_name="NO mistakes - Random indx const length",
                        avg=False, xlabel="parts", ylabel="const len",scatter=False, hist=True)

#random overlap_version: no mistakes
#----there is the min,max length and the min,max overlap
#----the samples cover the whole string
if DEFINES.RANDOM_OVERLAP_MOD:#random overlap - no mistakes:
    minlen=MIN_PART_LEN_PER
    noMistakes_statvec_randLen = {"X": [], "Y": [], "Z": []}  # X for parts, Y for overlap, Z for succsess
    while minlen*len(sourceString) < min(MAX_PART_LEN,MAX_PART_LEN_PER*len(sourceString)):
        parts = 2;
        noMistakes_statvec_randLen['Z'].append([])
        while(parts<7):#int((DEFINES.STRING_LEN/constlen))*3):
            arr= ArraysBuilder.allOverlap_randomLen(string=sourceString,
                                                 parts=parts,
                                                 min_len_per=minlen,
                                                 max_len_per=MAX_PART_LEN_PER,
                                                 min_overlap_per=MIN_OVERLAP_PER)
            ToolMenagemnt.run_plass(arr=arr, x=parts, y=minlen, res_vec=noMistakes_statvec_randLen, source=sourceString)
            parts+=1
        noMistakes_statvec_randLen["Y"].append(minlen);
        minlen+=PART_LEN_STEP

    plot.py_plotAll(res=noMistakes_statvec_randLen,g_ind=2,mis_name="NO mistakes - Random",avg=False, xlabel="parts", ylabel="len",scatter=False,hist=True)

plt.show()


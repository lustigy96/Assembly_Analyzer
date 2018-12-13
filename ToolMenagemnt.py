# this file oncludes all Baser managment: files prepration, statistics calculations, calls

import DEFINES
import subprocess
import os
import shutil

def arr2Files(arr, name, ind):# this function takes 2-dim array and put each array in its own file

    if DEFINES.BASER==1: #use DNABASER
        for i in range(len(arr)):
            f = open(DEFINES.PATH_FILES +"in/"+ name + str(ind + i) + ".fasta", "w")
            f.write(">gi|1\n" + (arr[i].replace("1", DEFINES.ONE)).replace("0", DEFINES.ZERO));
            f.close();

    if DEFINES.PLASS==1: #USE PLASS
        fasta_file = open(DEFINES.PATH_FILES + "in/" +name+".fasta", 'w')
        if DEFINES.FAST_FORM == 1: str_form = ">gi|"
        else: str_form = ">AB"
        i = 1
        for line in arr:
            if i>1: fasta_file.write("\n")
            fasta_file.write(str_form + str(i) + "\n")
            fasta_file.write((line.replace("1", DEFINES.ONE)).replace("0", DEFINES.ZERO));
            i += 1
        fasta_file.close()
    return ind + i;


def FASTA2arr(fasta_file):#take fasta file, change it to an array and save the output on a file
    arr=[]
    lines=fasta_file.readlines()
    for line in lines:
        if line[0] != ">":
            for x in line:
                if x==DEFINES.ZERO: arr[-1].append("0")
                elif x==DEFINES.ONE: arr[-1].append("1")
                elif x=='-': arr[-1].append("-")
                else: print x
        else:
            if line[0]==">":
                arr.append([])
    return arr


def TFstatistics(source, arr): #true for same and otherwise false
    if len(arr[0]) != len(source):  print "Diffrent len:"+str(len(arr[0]))+" "+str(len(source)); return 0
    res_cont=''.join(arr[0])
    res_cont=(res_cont.replace(DEFINES.ONE, "1")).replace(DEFINES.ZERO, "0")
    for r, s in zip(res_cont, source):
        if r != s: print "Diffrent"; print res_cont; print source; return 0
    print "Same"
    return 1


def run_plass(arr, x, y, res_vec, source): #run plass and calc statistics
    arr2Files(arr, DEFINES.FILE_IN_NAME, 0)
    #delete output file
    if os.path.exists(DEFINES.PATH_FILES + "out/" + DEFINES.FILE_OUT_NAME + ".fas"):
        os.remove(DEFINES.PATH_FILES + "out/" + DEFINES.FILE_OUT_NAME + ".fas")
        os.chmod(DEFINES.PLASS_PYTHON_PATH+"tmp",0o777)
        shutil.rmtree(DEFINES.PLASS_PYTHON_PATH+"tmp")

    else:
        print("The file does not exist")

    subprocess.call([r"/home/ubu/Yael/plass/bin/plass", "nuclassemble",
                     DEFINES.PATH_FILES + "in/" + DEFINES.FILE_IN_NAME + ".fasta",
                     DEFINES.PATH_FILES + "out/" + DEFINES.FILE_OUT_NAME + ".fas", "tmp"])

    if os.stat(DEFINES.PATH_FILES+"out/" + DEFINES.FILE_OUT_NAME+".fas").st_size != 0: #full file
        fasta_file = open(DEFINES.PATH_FILES+"out/" + DEFINES.FILE_OUT_NAME+".fas", 'r')
        arr2=FASTA2arr(fasta_file)
        fasta_file.close()
        res_vec["Z"][-1].append(TFstatistics(source, arr2))
    else:  #empty file
        res_vec["Z"][-1].append(-1)
        print "----------------------empty file"
    if len(res_vec['Z']) == 1:
        res_vec['X'].append(x)

    return res_vec




#UN-USED
# this function (for now) only return true for "the same" and otherwise- false.
# we will put here the real statistics, but we need to learn the structure of the output
def statistics(source, f_out):
    res_lines = f_out.readlines();
    res_cont = [];
    for i in range(1, len(res_lines)):
        res_cont.append(res_lines[i])
    (res_cont.replace(DEFINES.ONE, "1")).replace(DEFINES.ZERO, "0")
    for r, s in zip(res_cont, source):
        if r != s:
            return False
    return True
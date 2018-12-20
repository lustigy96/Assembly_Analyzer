#DEFINES 

#tested tool - ONLY ONE
BASER=0
PLASS=1

#string
STRING_LEN=2000

#mistakes difines
FLIP_MOD = True
DELETE_MOD = False
MIXED = False
RANDOM_DELETIONS= False

#overlaps mods to test
RANDOM_OVERLAP_MOD=False
SERIAL_OVERLAP_MOD=False#False
RANDOM_SAMPLE_MOD=True

#paths
FILE_IN_NAME="lola"
FILE_OUT_NAME="lola_out"

BASER_FILES_PATH="/home/ubu/Yael/project/baser_files/"		#input and output files to put in DNABASER program
DNABASER_PROGRAM_PATH="C:\MyPrograms\DNABASER\\"			#the program-call path

PLASS_FILES_PATH="/home/ubu/Yael/project/plass_files/"      #input and output files to put in plass program
PLASS_PROGRAM_PATH="/home/ubu/Yael/plass/bin/"			    #the program-call pat

PATH_PROGRAM=PLASS_PROGRAM_PATH;
PATH_FILES=PLASS_FILES_PATH;
PYTHON_PATH="/home/ubu/PycharmProjects/Assembly_Analyzer/"			    #the program-call pat

#plots
GRAPH_MID=False
ALLOW_MATLAB_RUN=False
PYTHON_GRAPH=True

#assembly defines
ZERO= 'T'
ONE='A'
FAST_FORM=1     #1 for gi|, 0 for AB...


import random
import DEFINES


# this function takes the string and put in to 2=dim arr with overlap
def serialOverlap_arr(string, parts, overlap):
    # if overlap==0 -> rand between MIN_OVERLAP_PER, MAX_OVERLAP_PER
    sub_string_arr = [];
    lap, i = 0,0;
    for part in range(parts):   # put to parts without overlap
        start = part * (len(string) / parts)
        end = (part + 1) * (len(string) / parts)
        sub_string_arr.append(string[start:end])
        if lap == 1:            # the overlap implementation
            if overlap == 0: overlap = random.randint(DEFINES.MIN_OVERLAP_PER, DEFINES.MAX_OVERLAP_PER)
            sub_string_arr[i] += ((sub_string_arr[i + 1])[0:int(overlap * len(sub_string_arr[i + 1]))])
            i += 1
        lap = 1
    print sub_string_arr
    return sub_string_arr;

#this function map the string to #parts subarrays, diffrent length to each part, all the string is mapped
def allOverlap_randomLen(string, parts=0, min_len_per=0, max_len_per=1, min_overlap_per=0):
    # min_len_per,max_len_per, min_overlap_per are %
    sub_string_arr = [];
    start = 0;
    end = start + random.randint(int(min_len_per * len(string)),int(max_len_per * len(string)))
    sub_string_arr.append(string[start:end])
    max_ind = end;
    for part in range(1, parts - 1):
        start = random.randint(0 , int(max_ind * (1 - min_overlap_per)))
        end = min(start + random.randint(int(min_len_per * len(string)), int(max_len_per * len(string))), len(string) - 1)
        if end > max_ind: max_ind = end
        sub_string_arr.append((string[start:end].replace("1", DEFINES.ONE)).replace("0", DEFINES.ZERO))

    start = random.randint(0,len(sub_string_arr[-1]))
    end = len(string) - 1
    sub_string_arr.append((string[start:end].replace("1", DEFINES.ONE)).replace("0", DEFINES.ZERO))
    return sub_string_arr;

#this function sample random index and put string[ind:ind+const] in arr
def randomSample_constLen(string, parts=0, constlen=0):
    arr=[]; strlen=len(string);
    constlen=int(constlen*strlen)
    for x in range(parts):
        ind=random.randint(0,strlen-1)
        arr.append(string[ind:min(ind+constlen,strlen-1)])
    return arr

#make flips on 2-dim array with probability=probToFlip
def flipsOnArr(arr,probToFlip):
    arr=list(arr)
    for x in range(len(arr)):
        for i in range(len(arr[x])):
            r=random.uniform(0,1);
            if r<probToFlip:
                if arr[x][i] == '1':
                    arr[x] = arr[x][:i] + '0' + arr[x][i + 1:]
                else:
                    arr[x] = arr[x][:i] + '1' + arr[x][i + 1:]
    # arr = ''.join(arr)
    return arr;






# this function get a 2-dimentional array, and start+end rows to make random #per_OfFlipsInStr% flips in each string
#has to be in precent because the parts are not equal
def makeOfFlipsInStr(arr, start_index_line, end_index_line, per_OfFlipsInStr,numberOfFlipsInStr):
    for x in range(start_index_line, end_index_line):
        if numberOfFlipsInStr == -1:
            numberOfFlipsInStr = int(len(arr[x]) * per_OfFlipsInStr)
        for j in range(numberOfFlipsInStr):
            l = len(arr[x])
            i = random.randint(0, l - 1)
            if arr[x][i] == '1':
                arr[x] = arr[x][:i] + '0' + arr[x][i + 1:]
            else:
                arr[x] = arr[x][:i] + '1' + arr[x][i + 1:]
    return arr

# this function get a 2-dimentional array, and start+end rows to make random #per_numberOfDeletionsInStr% del in each string
def makeDeletionsInStr(arr, start_index_line, end_index_line, per_numberOfDeletionsInStr,numberOfDeletionsInStr):
    for x in range(start_index_line, end_index_line):
        if numberOfDeletionsInStr == -1:
            dels = int(len(arr[x]) * per_numberOfDeletionsInStr)
        for j in range(dels):
            i = random.randint(0, len(arr[x]) - 1)
            arr[x] = arr[x][:i] + arr[x][i + 1:]
    return arr

# this function get a 2-dimentional array, and start+end rows to make random #per_numberOfRandomDeletionsInStr% del ~(random number) in each string
def makeRandomDeletionsInStr(arr, start_index_line, end_index_line, per_numberOfRandomDeletionsInStr,numberOfRandomDeletionsInStr):
    for x in range(start_index_line, end_index_line):
        if numberOfRandomDeletionsInStr==-1:
            dels = random.randint(0, len(arr[x]) * per_numberOfRandomDeletionsInStr)
        for j in range(dels):
            i = random.randint(0, len(arr[x]) - 1)
            arr[x] = arr[x][:i] + arr[x][i + 1:]
    return arr


# this function get a 2-dimentional array, and start+end rows to make random #per_numberOfRandomDeletionsInStr% del ~(random number) in each string
def makeMixedMistakesInStr(arr, start_index_line, end_index_line, per_numberOfRandomDeletionsInStr):
    # didnt do yet
    return arr


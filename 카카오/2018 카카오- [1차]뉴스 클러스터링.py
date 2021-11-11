import math
def solution(str1, str2):
    answer = 0
    str1=str1.lower()
    str2=str2.lower()
    str1_list=[]
    str2_list=[]
    overlap=[]
    tmp, temp=0,0
    for i in range(len(str1)-1):
        str1_list.append(str1[i:i+2])
    for i in range(len(str2)-1):
        str2_list.append(str2[i:i+2])
    for i in str1_list:
        if(str.isalpha(i) and i in str2_list):
            if(i not in overlap):
                overlap.append(i)
                tmp+=min(str2_list.count(i), str1_list.count(i))
                temp+=max(str2_list.count(i), str1_list.count(i))
        elif(str.isalpha(i)):
            temp+=1
    for i in str2_list:
        if(i not in overlap) and (str.isalpha(i)):
            temp+=1
    if(temp==0):
        return 65536
    answer=tmp/temp
    return math.trunc(answer*65536)

str1='FRANCE'
str2='french'
print(solution(str1,str2))
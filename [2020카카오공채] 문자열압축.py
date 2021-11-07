#2020년 카카오 문자열 압축.py
def solution(s): 
    answer=[] 
    if len(s)==1: 
        return 1 
    for i in range(1, (len(s)//2)+1): 
        temp = '' 
        cnt = 1 
        tmp=s[:i] 
        for j in range(i, len(s), i): 
            if tmp==s[j:i+j]: 
                cnt+=1 
            else: 
                if cnt!=1: 
                    temp = temp + str(cnt)+tmp 
                else: 
                    temp = temp + tmp 
                tmp=s[j:j+i] 
                cnt = 1 
        if cnt!=1: 
            temp = temp + str(cnt) + tmp 
        else: temp = temp + tmp
        answer.append(len(temp)) 
    return min(answer)

s="xababcdcdababcdcd"
print(solution(s))
def booler1(p):
    temp=[]
    for i in p:
        if(i=='('):
            temp.append(i)
        elif(i==')' and len(temp)!=0):
            temp.pop()
        else: return False
    return True
def booler2(p):
    temp=[]
    for n,i in enumerate(p):
        temp.append(i)
        if(temp.count('(')==temp.count(')')):
            return n
def solution(p):
    answer = ''
    p=list(p)
    u=''
    v=''
    if(booler1(p)):
        return ''.join(p)
    else:
        temp=booler2(p)
        u=p[0:temp+1]
        v=p[temp+1:len(p)]
        print(u,v,temp)
        if(booler1(u)):
            tmp=''.join(u)
            answer+=tmp
            print(answer)
            answer+=solution(v)
        else:
            answer+='('
            answer+=solution(v)
            answer+=')'
            for n in range(1,len(u)-1):
                if(u[n]=='('):
                    answer+=')'
                else: answer+='('
    return answer

p="))(()("
print(solution(p))
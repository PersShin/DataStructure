import sys
for _ in range(int(input())):
    strs=list(sys.stdin.readline().rstrip())
    str1=[]
    str2=[]
    for i in strs:
        if i=='<':
            if str1:
                str2.append(str1.pop())
        elif i=='>':
            if str2:
                str1.append(str2.pop())
        elif i=='-':
            if str1:
                str1.pop()
        else:
            str1.append(i)
    str1.extend(reversed(str2))
    print(''.join(str1))
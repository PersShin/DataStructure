import sys
string=list(sys.stdin.readline().rstrip())
new_string=[]
for _ in range(int(input())):
    commander=list(sys.stdin.readline().split())
    if commander[0]=='L':
        if string:
            new_string.append(string.pop())
    elif commander[0]=='D':
        if new_string:
            string.append(new_string.pop())
    elif commander[0]=='B':
        if string:
            string.pop()
    else:
        string.append(commander[1])

string.extend(reversed(new_string))    
print(''.join(string))
import sys
from collections import deque
N=int(input())
move=list(map(int,sys.stdin.readline().split()))
idxs=[i+1 for i in range(N)]
idx=0
result=[]
result.append(idxs.pop(idx))
tmp=move.pop(idx)
while move:
    if tmp>0:
        idx=(idx+tmp-1)%len(move)
    else:
        idx=(idx+tmp)%len(move)
    tmp=move.pop(idx)
    result.append(idxs.pop(idx))
for i in result:
    print(i,end=' ')
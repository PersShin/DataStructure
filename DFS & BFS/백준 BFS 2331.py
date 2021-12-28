from collections import deque
import sys
num,n=map(int,sys.stdin.readline().split())
queue=deque()
answer=[]
queue.append(num)
answer.append(num)
while True:
    print(queue,answer)
    s=queue.popleft()
    sumer=[int(i)**n for i in str(s)]
    temp=sum(sumer)
    if temp in answer:
        answer=answer[:answer.index(temp)]
        break
    queue.append(temp)
    answer.append(temp)
print(len(answer))
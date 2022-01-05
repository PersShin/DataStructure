import sys
def DFS(depth,total,plus,minus,mul,div):
    if depth==n:
        global max_size,min_size
        max_size=max(max_size,total)
        min_size=min(min_size,total)
        return
    if plus:
        DFS(depth+1,total+num[depth],plus-1,minus,mul,div)
    if minus:
        DFS(depth+1,total-num[depth],plus,minus-1,mul,div)
    if mul:
        DFS(depth+1,total*num[depth],plus,minus,mul-1,div)
    if div:
        DFS(depth+1,int(total/num[depth]),plus,minus,mul,div-1)
n=int(input())
num=list(map(int,sys.stdin.readline().split()))
strr=list(map(int,sys.stdin.readline().split()))
visited=set()
max_size=-1e9
min_size=sys.maxsize
DFS(1,num[0],strr[0],strr[1],strr[2],strr[3])
print(max_size)
print(min_size)
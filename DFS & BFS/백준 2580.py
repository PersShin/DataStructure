import sys
#열을 검색한다
def column(y,a):
    for n in range(9):
        if array[n][y]==a:
            return False
    return True
#행을 검색한다
def row(x,a):
    for n in range(9):
        if array[x][n]==a:
            return False
    return True
#정사각형 모양을 검색한다. 
def squar(x,y,a):
    xt=x//3*3
    yt=y//3*3
    for n in range(xt,xt+3):
        for m in range(yt,yt+3):
            if array[n][m]==a:
                return False
    return True
    
#여러가지 답이 있을수 있기 때문에 사용해도 무방하다.

def DFS(num):
    if num==len(blank):
        print()
        for i in range(9):
            print(*array[i]) 
        exit(0)
    for i in range(1,10): 
        x=blank[num][0]
        y=blank[num][1]
        if column(y,i) and row(x,i) and squar(x,y,i):
            array[x][y]=i
            DFS(num+1)
            array[x][y]=0
array=[list(map(int,sys.stdin.readline().split())) for _ in range(9)]
blank=[]
for i in range(9):
    for n in range(9):
        if array[i][n]==0:
            blank.append((i,n))
DFS(0)
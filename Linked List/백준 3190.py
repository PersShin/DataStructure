import sys
n=int(input())
graph=[[0 for _ in range(n)] for _ in range(n)]
for _ in range(int(input())):
    x,y=map(int,sys.stdin.readline().split())
    graph[x-1][y-1]=1
direction=[list(sys.stdin.readline().split()) for _ in range(int(input()))]
snake=[(0,0)]
cnt=0
i=0
directions=[(0,1),(-1,0),(0,-1),(1,0)]
which=0
while snake:
    cnt+=1
    snake.append((snake[-1][0]+directions[which][0],snake[-1][1]+directions[which][1]))
    if snake[-1][0]<0 or snake[-1][0]>=n or snake[-1][1]<0 or snake[-1][1]>=n:
        break
    if snake[-1] in snake[:-1]:
        break
    if graph[snake[-1][0]][snake[-1][1]]!=1:
        snake.pop(0)
    if graph[snake[-1][0]][snake[-1][1]]==1:
        graph[snake[-1][0]][snake[-1][1]]=0
    if i!=len(direction):
        if str(cnt)==direction[i][0]:
            if direction[i][1]=='L':
                if which<3:
                    which+=1
                else:
                    which=0
            else:
                if which>-4:
                    which-=1
                else:
                    which=-1
            i+=1
print(cnt)
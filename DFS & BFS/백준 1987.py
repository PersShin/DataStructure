import sys
def BFS():
    queue=set([(0,0,maps[0][0])])
    result=0
    while queue:
        tmp_x,tmp_y,lists=queue.pop()
        for i in range(4):
            dxt=tmp_x+dx[i]
            dyt=tmp_y+dy[i]
            result=max(result,len(lists))
            if 0<=dxt<len(maps) and 0<=dyt<len(maps[0]):
                if maps[dxt][dyt] not in lists:
                    queue.add((dxt,dyt,lists+maps[dxt][dyt]))
    return result
dx=[1,-1,0,0]
dy=[0,0,1,-1]
num_x,num_y=map(int,sys.stdin.readline().split())
maps = [list(sys.stdin.readline().strip()) for _ in range(num_x)]
print(BFS())
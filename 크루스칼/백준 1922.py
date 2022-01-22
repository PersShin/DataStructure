import sys

N=int(input())
M=int(input())
graph=[list(map(int,sys.stdin.readline().split())) for _ in range(M)]
graph.sort(key=lambda x:x[2])
p=[i for i in range(N+1)]

def find(u):
    if u!=p[u]:
        p[u]=find(p[u])
    return p[u]

def union(u,v):
    root1=find(u)
    root2=find(v)
    p[root2]=root1

tree_edges,mst_cost=0,0
while True:
    if tree_edges==N-1:
        break
    u,v,wt=graph.pop(0)
    if find(u)!=find(v):
        union(u,v)
        mst_cost+=wt
        tree_edges+=1
print(mst_cost)
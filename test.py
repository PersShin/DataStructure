#The Maping problem in Data Structure
#Using Stack or Queue!
import numpy as np
from numpy.lib.nanfunctions import nanquantile
def move(rat,map):
    map[rat[-1][0]][rat[-1][1]]=0
    for i in range(rat[-1][0]-1,rat[-1][0]+2):
        for n in range(rat[-1][1]-1,rat[-1][1]+2):
            if(map[i][n]==1):
                print(i,n)
                rat.append([i,n])
                return rat,map
    if(map[rat[-1][0]][rat[-1][1]]==0):
        rat.pop(-1)
    return rat,map
def find(map):
    rat=[[1,1]]
    while True:
        rat,map=move(rat,map)
        print(rat)
        if((rat[-1][0]==len(map)-2) & (rat[-1][1]==len(map)-2)):
            break
    print(rat)
#The map is set to (m+2)*(n+2)-> The real map is m*n
#The reason is that
map=[[0,0,0,0,0,0],[0,1,0,0,0,0],[0,1,1,0,1,0],[0,0,1,0,0,0],[0,1,0,1,1,0],[0,0,0,0,0,0]]
find(map)
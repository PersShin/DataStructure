#The Maping problem in Data Structure
#Using Stack or Queue!
#I added Making map fuction(mapMaking)
def mapMaking(map):
    length=len(map)
    tmp=[[0] for i in range(length+2)]
    print(tmp)
    for i in range(length+1):
        tmp[0].append(0)
        tmp[length+1].append(0)
    for i in range(0,length):
        tmp[i+1].extend(map[i])
        tmp[i+1].append(0)
        print(tmp)
    return tmp
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
    map=mapMaking(map)
    #The map=mapMaking(map) is set to (m+2)*(n+2)-> The real map is m*n
    print(map)
    rat=[[1,1]]
    while True:
        rat,map=move(rat,map)
        print(rat)
        if((rat[-1][0]==len(map)-2) & (rat[-1][1]==len(map)-2)):
            break
    print(rat)
map=[[1,0,0,0],[1,1,0,1],[0,1,0,0],[1,0,1,1]]
find(map)
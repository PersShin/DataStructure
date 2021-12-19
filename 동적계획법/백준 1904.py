num=int(input())
multiple=[0 for _ in range(1000001)]
multiple[1]=1
multiple[2]=2
for i in range(3,num+1):
    #연산을 할때마다 15746으로 나머지를 구해야 한다. 안그러면 메모리 초과가 나타난다.
    multiple[i]=(multiple[i-1]+multiple[i-2])%15746
print(multiple[num])
import sys
num=int(input())
triangle=[]
for _ in range(num):
    triangle.append(list(map(int,sys.stdin.readline().split())))
for i in range(1,num):
    for n in range(i+1):
        if n==0:
            triangle[i][n]+=triangle[i-1][n]
        elif n==i:
            triangle[i][n]+=triangle[i-1][n-1]
        else:
            triangle[i][n]+=max(triangle[i-1][n],triangle[i-1][n-1])
print(max(triangle[-1]))
import sys
def fib(n):
    if len(data_0)<=n:
        data_0.append(fib(n-1)[0]+fib(n-2)[0])
        data_1.append(fib(n-1)[1]+fib(n-2)[1])
    return data_0[n],data_1[n]
data_0=[1,0]
data_1=[0,1]
num=int(input())
for i in range(num):
    n=int(input())
    x,y=fib(n)
    print(x,y)
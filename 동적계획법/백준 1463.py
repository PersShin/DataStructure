n=int(input())
results=[0]*(n+1)
for i in range(2,n+1):
    results[i]=results[i-1]+1
    if i%3==0:
        results[i]=min(results[i],results[i//3]+1)
    if i%2==0:
        results[i]=min(results[i],results[i//2]+1)
print(results[-1])
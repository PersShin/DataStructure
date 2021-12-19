num=int(input())
triangle=[0 for _ in range(101)]
triangle[1]=1
triangle[2]=1
triangle[3]=1
for i in range(num):
    n=int(input())
    for q in range(4,n+1):
        triangle[q]=triangle[q-2]+triangle[q-3]
    print(triangle[n])
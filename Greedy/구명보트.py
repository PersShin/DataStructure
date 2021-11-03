def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    n=len(people)-1
    i=0
    while i<=n:
        answer+=1
        print(people[i],people[n],len(people))
        if(people[i]+people[n]<=limit):
            n-=1
        i+=1
    return answer

people=[70, 50, 80]
limit=100
print(solution(people,limit))
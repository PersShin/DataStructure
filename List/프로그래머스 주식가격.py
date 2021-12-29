from collections import deque
def solution(prices):
    answer = []
    queue=deque(prices)
    while queue:
        cnt=0
        tmp=queue.popleft()
        for i in queue:
            cnt+=1
            if tmp>i:
                break
        answer.append(cnt)
    return answer

prices=[1, 2, 3, 2, 3]
print(solution(prices))
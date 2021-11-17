from collections import deque
def solution(numbers, target):
    answer = 0
    queue=deque()
    n=len(numbers)
    queue.append([numbers[0],0])
    queue.append([-1*numbers[0],0])
    while queue:
        temp, idx = queue.popleft()
        print(temp,idx,queue)
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer

numbers=[1,1,1,1,1]
target=5
print(solution(numbers,target))
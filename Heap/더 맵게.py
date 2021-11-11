import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    for i in range(0,len(scoville)):
        if(scoville[0]>=K):
            return i
        if(len(scoville)<=1):
            break
        heapq.heappush(scoville,heapq.heappop(scoville)+2*heapq.heappop(scoville))
    return -1
lists=[1, 2, 3]
K=14
print(solution(lists,K))
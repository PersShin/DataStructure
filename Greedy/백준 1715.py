import heapq
#heapq는 이진트리 기반의 최소 힙 자료구조를 제공하는 메서드입니다.
#push를 하게 되면 알아서 최소 힙(장렬)이 되므로 시간 복잡도가 많이 낮아진다.
import sys
n=int(input())
card_deck=[]
for _ in range(n):
    heapq.heappush(card_deck,int(sys.stdin.readline()))
if len(card_deck)==1:
    print(0)
else:
    answer=0
    while len(card_deck)>1:
        tmp_1=heapq.heappop(card_deck)
        tmp_2=heapq.heappop(card_deck)
        answer+=tmp_1+tmp_2
        heapq.heappush(card_deck,tmp_1+tmp_2)

    print(answer)
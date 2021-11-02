from collections import defaultdict
def solution(genres, plays):
    answer = []
    dict=defaultdict(lambda: 0)
    total_list=defaultdict(lambda:[])
    diction=list(zip(genres, plays))
    for i,n in diction:
        dict[i]+=n
        total_list[i].append(n)
    dict=sorted(dict,key=lambda x:dict[x],reverse=True)
    print(dict)
    for i in total_list:
        total_list[i]=sorted(total_list[i],reverse=True)
    for i in dict:
        
        answer.append(plays.index(total_list[i][0]))
        plays[plays.index(total_list[i][0])]=0
        if(len(total_list[i])>1):
            answer.append(plays.index(total_list[i][1]))
            plays[plays.index(total_list[i][1])]=0
    return answer
genres=["classic", "classic", "classic", "pop"]
plays=[500, 80000, 80000, 800]
print(solution(genres,plays))
def solution(bridge_length, weight, truck_weights):
    answer=0
    tmp=[0 for i in range(bridge_length)]
    last=truck_weights[-1]
    while truck_weights:
        tmp.pop(0)
        if(weight>=sum(tmp,truck_weights[0])):
            tmp.append(truck_weights.pop(0))
        else:
            tmp.append(0)
        answer+=1
    if(answer==1): answer+=bridge_length
    else: answer+=tmp.index(last,-1)+1
    return answer
bridge_length=2
weight=10
truck_weights=[7,4,5,6]
answer=solution(bridge_length,weight,truck_weights)
print(answer)

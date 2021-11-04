def solution(record):
    answer = []
    dict={}
    for i in record:
        new=i.split()
        if(new[0]=='Enter' or new[0]=='Change'):
            dict[new[1]]=new[2]
    for i in record:
        new=i.split()
        if(new[0]=='Enter'):
            answer.append(dict[new[1]]+'님이 들어왔습니다.')
        elif(new[0]=='Leave'):
            answer.append(dict[new[1]]+'님이 나갔습니다.')
    return answer

record=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))
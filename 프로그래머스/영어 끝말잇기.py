def solution(num, words):
    answer = [0,0]
    tmp=[words[0]]
    for n in range(1,len(words)):
        if words[n][0]!=words[n-1][-1] or words[n] in tmp:
            return [n%num+1,1+n//num]
        tmp.append(words[n])
    return answer

n=3
work=["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(n,work))

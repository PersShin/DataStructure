def solution(nums):
    answer = len(nums)/2
    lists=set(nums)
    print(lists)
    if(answer>=len(lists)):
        return len(lists)
    else: return int(answer)




nums=[3,3,3,2,2,2]
print(solution(nums))
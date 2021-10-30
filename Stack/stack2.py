#solutions for https://programmers.co.kr/learn/courses/30/lessons/42586
def solution1(progress, speed):
    tmp=[]
    answer=[0]
    for n,i in enumerate(progress):
        tmp.append(int((100-i)/speed[n])+1)
    temp=tmp[0]
    i=0
    for n in tmp:
        if(temp>=n):
            answer[i]+=1
        else:
            temp=n
            i+=1
            answer.append(1)
    return answer
lists=[95, 90, 99, 99, 80, 99]
speed=[1, 1, 1, 1, 1, 1]
answer=solution1(lists,speed)
print(answer)

def solution2(progresses, speeds):
    answer = []
    while len(progresses)>0:
      progresses=[x+y for x,y in zip(progresses,speeds)]
      print(progresses)
      if max(progresses)>=100:
        tmp=0
        for i in range(0,len(progresses)):
          if progresses[0]>=100:
            progresses.pop(0)
            speeds.pop(0)
            tmp+=1
          else: 
            if tmp!=0:
              answer.append(tmp)
            break  
          if len(progresses)==0:
            answer.append(tmp)
    return answer

lists=[95, 90, 99, 99, 80, 99]
speed=[1, 1, 1, 1, 1, 1]
answer=solution2(lists,speed)
print(answer)


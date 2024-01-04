#https://school.programmers.co.kr/learn/courses/30/lessons/135808

def solution(k, m, score):
    score=sorted(score,reverse=True)
    num=len(score)//m
    answer=0
    if num==0:
        return 0
    else:
        for i in range(num):
            answer+=min(score[i*m:(i+1)*m])*m
    return answer
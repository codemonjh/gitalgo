#https://school.programmers.co.kr/learn/courses/30/lessons/12919

def solution(seoul):
    index=len(seoul)
    for i in range(index):
        if seoul[i]=='Kim':
            return "김서방은 {}에 있다".format(i)
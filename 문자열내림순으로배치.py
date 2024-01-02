#https://school.programmers.co.kr/learn/courses/30/lessons/12917

def solution(s):
    a=[ord(s[i:i+1]) for i in range(len(s))]
    a.sort(reverse=True)
    b="".join([chr(i) for i in a])
    return b
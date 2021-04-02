def solution(s):
    a=[]
    for i in range(s+1):
        if i % 2 == 0:
            a.append(i)
    return a
solution(50)

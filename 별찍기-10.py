#https://www.acmicpc.net/problem/2447

num=int(input())

def makestar(num):
    if num==3:
        return ['***',"* *","***"]
    else:
        lis=makestar(num//3)
        listwo=[]
        for i in range(3):
            if i==0 or i==2:
                for i in range(num//3):
                    listwo.append(lis[i]*3)
            else:
                for i in range(num//3):
                    listwo.append(lis[i]+" "*(num//3)+lis[i])
        return listwo

for line in makestar(num):
    print(line)
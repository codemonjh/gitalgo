#https://www.acmicpc.net/problem/3080

from string import ascii_uppercase
import math 
import sys
sys.setrecursionlimit(10**6)
num=int(input())
lis=[]
for i in range(num):
    lis.append(input())
lis.sort()

# def bname(lis):
#     lislis=[[] for _ in range(27)]
#     if len(lis)==1:
#         return 1
#     else:
#         result=1
#         for i in lis:
#             if i=="":
#                 lislis[26].append(i)
#                 continue
#             lislis[ord(i[0])-89].append(i[1:])
#         num=27
#         for i in lislis:
#             if i==[]:
#                 num-=1
#             else:
#                 result=result*bname(i)
#         result=result*math.factorial(num)
#     return result

# print(bname(lis))

# def bname(lis):
#     if len(lis)==1:
#         return 1
#     else:
#         result=1
#         num=0
#         lislis=[0]
#         last=len(lis)
#         pre=lis[0][0]
#         if pre=='*':
#             pre=lis[1][0]
#             lis=lis[1:]
#             num=1
#             last-=1
#         for i,item in enumerate(lis):
#             if item[0]!=pre:
#                 pre=item[0]
#                 lislis.append(i)
#         result=result*math.factorial(len(lislis)+num)//1000000007
#         base=0
#         lislislis=[]
#         if len(lislis)==1:
#             for i in range(last):
#                 if lis[i][1:]!="":
#                     lislislis.append(lis[i][1:])
#                 else:
#                     lislislis.append("*")
#             result=result*bname(lislislis)//1000000007
#         else:
#             if lislis[len(lislis)-1]<last:
#                 for i in range(last):
#                     if base<len(lislis)-1:
#                         if lis[i][1:]!="":
#                             lislislis.append(lis[i][1:])
#                         else:
#                             lislislis.append("*")

#                         if i+1==lislis[base+1]:
#                             base+=1
#                             result=result*bname(lislislis)//1000000007
#                             lislislis=[]
#                     else:
#                         if lis[i][1:]!="":
#                             lislislis.append(lis[i][1:])
#                         else:
#                             lislislis.append("*")
#                         if i==last-1:
#                             result=result*bname(lislislis)//1000000007
#                             lislislis=[]
#             else:
#                 for i in range(last):
#                     if lis[i][1:]!="":
#                         lislislis.append(lis[i][1:])
#                     else:
#                         lislislis.append("*")
#                     if i==last-1:
#                         break
#                     if i+1==lislis[base+1]:
#                             base+=1
#                             result=result*bname(lislislis)//1000000007
#                             lislislis=[]

#         return result//1000000007
# print(bname(lis))

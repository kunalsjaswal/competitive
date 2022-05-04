#smyterric diff
"""
n=int(input("n:"))
setn=set(map(int,input().split()))
m=int(input("m:"))
setm=set(map(int,input().split()))

symdiff=list(setm.symmetric_difference(setn))
symdiff.sort()
for i in symdiff:
    print(i)
"""

# distinct countries
# n=int(input())
# set1=set()
# for i in range(n):
#     country=input()
#     set1.add(country)
# print(set1)

# set operations

# n = int(input())
# s = set(map(int, input().split()))
# inst = int(input())
# print(s)
# for i in range(inst):
#     query = input().split()
#     if query[0] == "pop":
#         s.pop()
#     elif query[0] == "remove":
#         s.remove(int(query[1]))
#     elif query[0] == "discard":
#         s.discard(int(query[1]))
#     else:
#         s = s
#
# print(s)

# at least one subsciption

n=int(input())
set1=set(map(int,input().split()))
m=int(input())
set2=set(map(int,input().split()))

totalstu=set1.union(set2)
print(len(totalstu))

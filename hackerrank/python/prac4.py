# set intersection
"""
n1=int(input())
set1=set(map(int,input().split()))
n2=int(input())
set2=set(map(int,input().split()))
total=set1.intersection(set2)
print(len(total))

#sets 2

size,two=map(int,(input()).split())

arr1=list(map(int,input().split()))

happy=set(map(int,input().split()))
sad=set(map(int,input().split()))
happiness=0

for i in arr1:
    if i in happy:
        happiness+=1
    elif i in sad:
        happiness-=1
    else:
        happiness=happiness

print(happiness)

#set difference

n1=int(input())
set1=set(map(int,input().split()))
n2=int(input())
set2=set(map(int,input().split()))
total=set1.difference(set2)
print(len(total))

# set symmetric_difference

n1=int(input())
set1=set(map(int,input().split()))
n2=int(input())
set2=set(map(int,input().split()))
total=set1.symmetric_difference(set2)
print(len(total))

# set update operations
1. intersection_update
2. update
3. symmetric_difference_update
4. difference_update



size=int(input())
set1=set(map(int,input().split()))
num_oper=int(input())
for i in range(num_oper):
    operation=input().split()
    values=set(map(int,input().split()))

    if operation[0]=="intersection_update":
        set1.intersection_update(values)
    elif operation[0]=="update":
        set1.update(values)
    elif operation[0]=="symmetric_difference_update":
        set1.symmetric_difference_update(values)
    elif operation[0]=="difference_update":
        set1.difference_update(values)
    else:
        set1=set1
print(sum(set1))

n=int(input())
list1=list(map(int,input().split()))

unique=[i for i in list1 if list1.count(i)==1]
for j in unique:print(j)


# subset

times=int(input())
result=[]
for i in range(times):
    n1=int(input())
    set1=set(map(int,input().split()))
    n2 = int(input())
    set2 = set(map(int, input().split()))
    result.append(set1.issubset(set2))

for j in result:
    print(j)

#superset
mainset=set(map(int,input().split()))
result=[]
n=int(input())
for i in range(n):
    temp_set=set(map(int,input().split()))
    result.append(mainset.issuperset(temp_set))

bool=False
if bool in result:
    print("False")
else:
    print("True")

sets done
"""

# hacker rank practice quetions

# 1. list items sum not equal to given
'''
list1=[]
final_list=[]
x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))
n = int(input("n:"))

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            list1.append([i,j,k])

for items in list1:
    sum=0
    for inneritems in items:
        sum+=inneritems
    if sum != n:
        final_list.append(items)

print(f"list1: {list1}")
print(f"final_list: {final_list}")
'''

# 2. runner up in sports meet
'''
n = int(input(f"n : "))
arr=[]
for i in range(n):
    arr.append(int(input(f"{i+1} digit:")))

arr.sort(reverse=True)
print(arr)
i=0
while True:
    if(arr[i]==arr[i+1]):
        i+=1
    else:
        print(arr[i+1])
        exit(0)
'''
#3. 2nd lowest names
"""
students = [['Harsh', 20], ['Beria', 20], ['varun', 19], ['kaku', 34], ['vikas', 21]]
temps=[]
students.sort(key=lambda e:e[1])
print(students)
i=0
while True:
    if(students[i][1]==students[i+1][1]):
        # temps.append(students[i])
        i+=1
    else:
        i+=1
        temps.append(students[i])
        while True:
            if (students[i][1] == students[i + 1][1]):
                i+=1
                temps.append(students[i])
            else:
                temps.sort()
                for items in temps:
                    print(items[0])
                exit(0)

"""
# swap  cases
"""
str1="Hello KunAl"
print(str1)
str1=list(str1)
for i in range(len(str1)):
    if str1[i].isupper()==True:
        str1[i]=str1[i].lower()
    else:
        str1[i]=str1[i].upper()
str1="".join(str1)
print(str1)
"""

# add - to a string
str1="hello kunal"
def split_and_join(line):
    line=list(line)
    for i in range(len(line)):
        if line[i]==' ':
            line[i]="-"
    line="".join(line)
    return line

result=split_and_join(str1)
print(result)






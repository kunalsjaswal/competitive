# converting strings to list
# raw=input()
# i,c=input().split()
#
# def strr(s,p,c):
#     s=list(s)
#     s[int(p)]=c
#     s="".join(s)
#     return s
#
# result=strr(raw,i,c)
# print(result)


#find the string
# str1="kunalkunal"
# counter=0
# substr=""
#
#
# for i in range(len(str1)-len(substr)+1):
#     if (str1[i:i+len(substr)]==substr):
#         counter+=1
#
# print(counter)

#different methods

# str1="aB8"

# alfa,digit,lower,upper,alfanum=0,0,0,0,0
#
# for i in str1:
#     if i.isalnum():
#         alfanum+=1
#     if i.isalpha():
#         alfa+=1
#     if i.isdigit():
#         digit+=1
#     if i.islower():
#         lower+=1
#     if i.isupper():
#         upper+=1
#
# if alfanum>0:
#     print("True")
# else:
#     print(False)
# if alfa>0:
#     print("True")
# else:
#     print("False")
# if digit>0:
#     print("True")
# else:
#     print("False")
# if lower>0:
#     print("True")
# else:
#     print("False")
# if upper>0:
#     print("True")
# else:
#     print("False")

#pattern


n,m=map(int,input().split())

for i in range(1,n,2):
    print((".|."*i).center(m,"-"))
print("WELCOME".center(m,"-"))
for i in range(n-2,0,-2):
    print((".|."*i).center(m,"-"))


#bin(),oct(),hex()

# n=int(input("n:"))
# int_sp,oct_sp,hex_sp,bn_sp=0,3,3,4
# for i in range(1,n+1):
#     if i>9:
#         int_sp=0
#     else:
#         int_sp=1
#     if (int(oct(i)[2:]))>8:
#         oct_sp=2
#     else:
#         oct_sp=3
#
#     if i>15:
#         hex_sp=2
#     else:
#         hex_sp=3
#
#     if len(bin(i)[2:])==2:
#         bn_sp=3
#     elif len(bin(i)[2:])==3:
#         bn_sp=2
#     elif len(bin(i)[2:])==4:
#         bn_sp=1
#     elif len(bin(i)[2:])==5:
#         bn_sp=0
#
#
#     print(" "*int_sp,i," "*oct_sp,oct(i)[2:]," "*hex_sp,hex(i)[2:].capitalize()," "*bn_sp,bin(i)[2:])


#capaalize

# str1="hello   world  lol"
#
# ls=str1.split()
# for i in range(len(ls)):
#     ls[i]=ls[i].capitalize()
# str1=" ".join(ls)

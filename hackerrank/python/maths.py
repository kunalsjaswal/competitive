# 1 divmod
"""
num=int(input())
div=int(input())

print(num//div)
print(num%div)
print(divmod(num,div))

#2 pow

a=int(input())
b=int(input())
c=int(input())
print(pow(a,b))
print(pow(a,b,c))

#3
a=int(input())
b=int(input())
c=int(input())
d=int(input())
print(pow(a,b)+pow(c,d))
"""
# palindrome

n=int(input())
for i in range(1,n+1):
    print((((10**i)-1)//9)**2)



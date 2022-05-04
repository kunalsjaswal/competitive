#1st
"""
str1,maxln=input(),int(input())

def out():
    list1 = []
    for i in range(0, len(str1), maxln):
        list1.append(str1[i:i + maxln])
    for j in list1:
        return j


result=out()
print(result)
"""

# 2nd cartesian product
"""
from itertools import product

a=[]
b=[]
temp=input().split()
for i in temp:
    a.append(int(i))
temp=input().split()
for j in temp:
    b.append(int(j))

result=list(product(a,b))
for i in result:
    print(i,end=" ")
"""
# 3rd- complex number
"""
import cmath
comp=complex(input())
polar=cmath.polar(comp)
for i in polar:
    print(round(i,3))
"""

#4th shoe shop
"""
shoe=int(input())
shoe_size=[]
temp=input().split()
for i in temp:
    shoe_size.append(int(i))
del temp
customer=int(input())
money=0
for i in range(customer):
    cust=(input().split())
    if int(cust[0]) in shoe_size:
        shoe_size.remove(int(cust[0]))
        money+=int(cust[1])

print(money)

"""
#5th permutations
"""
from itertools import permutations
word=input().split()
perm=(list(permutations(word[0],int(word[1]))))
perm.sort()
for i in perm:
    for j in i:
        print(j,end="")
    print()
"""

#6th combination with replacement
"""
from itertools import combinations_with_replacement

word=input().split()
comb= list(combinations_with_replacement(word[0],int(word[1])))
comb.sort()

for i in comb:
    for j in i:
        print(j,end="")
    print()

str1=input()
list1=[]
for i in str1:
    list1.append(int((i)))

times=[]
numb=[]
counter=0
for j in range(len(list1)):
    if len(numb)==0:
        numb.append(list1[j])
        counter+=1
    else:
        if list1[j]==list1[j-1]:
            counter+=2
        else:
            times.append(counter)
            numb.append(list1[j])
            counter=0


#7th average of sets(distinct)

def average(array):
    sum=0
    avg=0
    for i in array:
        sum+=i
    avg=sum/len(array)
    return avg

n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)


#8th TEXT WRAP
import textwrap
strings="kunalsinghjaswal"
result_wrap=textwrap.wrap(strings,3)
result_fill=textwrap.fill(strings,3)
print(result_wrap,"\n",result_fill)

"""

# 9th String
import textwrap
n=int(input("num: "))
strings="KYQYTWXTDQXWDLKIXNWIITFBLIHRNGDZGVYCRXVWNUVSFFACUXMCSTFFBNWQVBQCWOEPNBOAVJUCOUGITSMNLSUOFRFAUXETNIKAJYCEJWIXSOHMGUBTOWKVPPXJOCEBKPDWNFCXDLWVZEJIALBOJLLYCIJQKOTXDWTSDVRIGOEIUPQUCRKLFVLHFXASNVPSUKKXHCGOSMYMDOIGHUTMPHWWEYORTFJNPVNXZVNTJNFMBPSIJOXAVTXZRNSKTDAKANJAKYTTLBFMSAXCOUCJNBKGPESKHSWJHGJREFKSISGASDCIZHTOKFUBJNLSFIBPQNGWSROCLVCDAHNAQGOALJCUYPOFZPUPEDMYWAAHXDKAMXACFQCQBGMZWAHVRBNYEZWABXJBCVBOSDQZTSPVZDWXFDSZHFXNGTQISZLUVMKPPAPIVGFWKCTRHNQQVPEBJULDVYAQKKGBLXMIDREPVZHFMZVJPZNAVADRZDHJOPNBMZLSQRHOQQTEQQOFSDFNDKGCOQOEFBHUASMSJTIBMDFCUVHOYOBCYKGOAWSHXBDZTPUELEFXINZEIISJYVNWFTNHQHPPJSREKNJXRQUZDVDOFVZDRMBYHOGZYXRHRILBVWYMPUOURRIWPJBIVFGFVOGTLXADHOGCMHRBDFWVYGTPQVXNCGUXUBRGYTLGJRKWADZEIVZJEUAURAJTGERCFIKFDVLNPWJPZITKGUVKPVGGXPADVTGCBQIGOTTDREUTPQFVKCFBZNKXEMAAFICIBMOPGKUZOQUDGZYTDFUDUGAZUCBZNFJQSAFAKBBYRWEYXETBMPEGWGHQKISZOBPIDWINXJORHSRFWKGIZMRXSYOEHIEXLTHPQPCPASGIMXPJJVTJHMGBLWHUELTQHAHZRJOTEXDQWSBGNXPWJXXWUHQASJSBLZCCJRWPQZFMUHSHEJEPHDMDKCDFOWIZVLEGECVUDDIXKDFQMLFVQRYDWEKMCSNZFRGJTDFZGOWSTBIFOOBHHBKDHUPJMDJSWRDS"
dive=len(strings)//n
ls=textwrap.wrap(strings,dive)
for i in range(len(ls)):
    ls[i]=set(ls[i])
    ls[i]=list(ls[i])
print(ls)
ls=set(ls)
# for j in ls[i]:
#     print(j,end="")
#     print()
print(ls)


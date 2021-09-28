# s=input('enter the string')
# ch=input('enter the letter to be removed')
# n=len(s)
# str=''
# for x in s:
#     # print(x)
#     if(x!=ch):
#         str+=x
# print(str)


# find the occurance of a character
s=input('enter the string')
ch=input('enter the letter')
count=0
for x in s:
    if(x==ch):
        count+=1
print(count)
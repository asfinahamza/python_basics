# str=input('enter  a word : ')
# status=0
# l=len(str) 
# for i in range(0,int(len(str)/2)):
#     if(str[i] != str[l-i-1]):
#         status=1
# if(status==1):
#     print('no')
# else:
#     print('yss')

# string=input('enter the string: ')
# rev_str=string[::-1]
# print(rev_str)
# if(string==rev_str):
#     print('it is a palindrome')
# else:
#     print('sorry..not a palindrome')

string=input('enter the string: ')
l=len(string)
status='true'
for x in range(int(l/2)):
    print(string[x])
    if(string[x]!=string[l-x-1]):
        status='false'
    else:
        status='true'
if(status=='true'):
    print('yesss')
else:
    print('noooo')



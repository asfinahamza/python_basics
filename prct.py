     



# n=int(input('enter no of rows'))
# for i in range(1,n):
#     for j in range(n,0,-1):
#         if(j>i):
#             print(' ',end='')
#         else:
#             print('*',end='')
#     print()

# n=int(input('enter no of rows'))
# for x in range(0,n+1):
#     for y in range(n,0,-1):
#         if(y>x):
#             print(' ',end=' ')
#         else:
#             print('*',end=' ')
#     print()

# n=int(input('enter no of rows'))
# for x in range(0,n+1):
#     for y in range(0,2*n+1):
#         if(y>x or y<n-x):
#             print(' ',end='')
#         else:
#             print('*',end='')
#     print()

# sum=0
# n=int(input('enter limit'))
# for x in range(0,n):
#     for y in range(0,2*n):
#         if(y>x and y<2*n-x-1):
#             print(' ',end=' ')
#         else:
#             print('*',end=' ')
#     print()
# for x in range(n-1,0,-1):
#     for y in range(0,2*n):
#         if(y>=x and y<=2*n-x-1):
#             print(' ',end=' ')
#         else:
#             print('*',end=' ')
#     print()


# n=int(input('enter the no'))
# c=0
# for x in range(2,n):
#     if(n%x==0):
#         c=1
#         print('not a prime')
#         break
# else:
#     print("a prime number")

# n1=int(input('enter start'))
# n2=int(input('enter end'))
# sum=0
# for num in range(n1,n2+1):
#     c=0
#     for i in range(2,int(num/2)+1):
#         if(num%i==0):
#             c=1
#             break
#     if(c==0 and num!=1):
#         print(num)
#         sum+=num
# print('sum: ',sum)

# n=int(input('enter number'))
# c=0
# for i in range(2,n):
#     if(n%i==0):
#         print(i)
#         c+=1
# print('no of factors: ',c)       
print('divisible by 3: ',end='')
for x in range(1,100):
    if(x%3==0):
        print(x,end=' ')
print()
print('divisible by 5: ',end='')
for x in range(1,100):
    if(x%5==0):
        print(x,end=' ')
print()
print('divisible by 5 and 3: ',end='')
for x in range(1,100):
    if(x%5==0 and x%3==0):
        print(x,end=' ')

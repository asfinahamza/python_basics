# a=input('enter a string')
# l=len(a)
# status=0
# for x in range(int(l/2)):
#     if(a[x]!=a[l-1-x]):
#         status=1
#         break
# if(status==0):
#     print('palindrome')
# else:
#     print('not palindrome')



# fibnoccii

# limit=int(input('enter limit'))
# f1=0
# f2=1
# print(f1,f2,' ',end="")
# i=0
# while(i<=limit):
#     f=f1+f2
#     i+=1
#     print(f,' ',end="")
#     f1=f2
#     f2=f

# f1=1
# f2=1
# print(f1,f2,end=' ')
# for i in range(limit):
#     f=f1+f2
#     print(f, end=' ')
#     f1=f2
#     f2=f



# string=input('enter string')
# ch=input('enter character')
# st=''
# for x in string:
#     if(x!=ch):
#         st+=x
# print(st)

# string=input('enter string')
# ch=input('enter character')
# c=0
# for x in string:
#     if(x==ch):
#         c+=1
# print(c)



# a=[4,3,1,5,8,6,9,10]
# # a.sort(reverse=True)
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if(a[i]>a[j]):
#             temp=a[i]
#             a[i]=a[j]
#             a[j]=temp
# print(a)



# n=int(input('enter size of array'))
# a=[]
# for x in range(n):
#     x=int(input('enter value'))
#     a.append(x)
# print(a)




# a.sort(reverse=True)
# for i in range(n):
#     for j in range(i+1,n):
#         if(a[i]>a[j]):
#             temp=a[i]
#             a[i]=a[j]
#             a[j]=temp

# print(a)
    
# print('missing:',end='')
# for x in range(a[0],a[len(a)-1]):
#     if(x not in a):
#         print(x)

# a=[52,41,23,61,11,83]
# n=len(a)
# for i in range(n):
#     for j in range(i+1,n):
#         if(a[i]>a[j]):
#             temp=a[i]
#             a[i]=a[j]
#             a[j]=temp
#         res=a[i]    
# print(res)

# n=int(input('enter a no'))
# temp=n
# count=0
# while(temp>0):
#     count+=1
#     temp=temp//10
# temp=n
# sum=0
# while(temp>0):
#     rem=temp%10
#     sum=sum+rem**count
#     temp=temp//10


# if(n==sum):
#     print('armstrong')
# else:
#     print('not armstrong')
# n=int(input('enter the no'))


# def fact(n):
#     if(n==0):
#         return 1
#     while(n>0):
#         return n*fact(n-1)

# print(fact(n))


# fact=1
# i=1
# while(i<=n):
#     fact=fact*i
#     i+=1
# print(fact)


# a=10
# b=20
# print('a: ',a)
# print()
# print('b: ',b)
# print()
# a=a+b
# b=a-b
# a=a-b
# print('a: ',a)
# print()
# print('b: ',b)

# sum=0
# for x in range(11):
#     if(x%2==0):
#         sum+=x
# print(sum)

# n=int(input('enter no'))
# status=0
# for x in range(2,n//2+1):
#     if(n%x==0):
#         status=1
# if(status==1):
#     print('not prime')
# else:
#     print('prime')


# n=int(input('enter no'))
# if(n>1):
#     for x in range(2,int(n/2)+1):
#         if(n%x == 0):
#             print('not prime')
#             break
#     else:
#         print('prime')
# else:
#     print('not prime')

  
# n=int(input('enter limit'))
# sum=0
# num=1
# for num in range(1,n):
#     c=0
#     for i in range(2,int(num/2)+1):
#         if(num%i == 0):
#             c += 1
#             break
#     if(c==0 and num!=1):
#         sum=sum+num

# print(sum)



#prime number btwn 2 limits and sum

# n1=int(input('enter start limit'))
# n2=int(input('enter end limit'))
# sum=0
# for x in range(n1,n2+1):
#     c=0
#     for i in range(2,int(x/2)+1):
#         if(x%i == 0):
#             c+=1
#             break
#     if(c==0 and x!=1):
#         print(x)
#         sum=sum+x
# print('sum: ',sum) 



# n=int(input('enter no'))
# limit=int(input('enter limit'))
# for i in range(1,limit+1):
#     print(n,'x',i,'=',n*i)


# rows=int(input('enter limit'))
# for i in range(0,rows):
#     for j in range(0,i):
#         print('*',end='')
#     print()
    

# rows=int(input('enter limit'))
# for i in range(1,rows+1):
#     for j in range(rows,0,-1):
#         if(j>i):
#             print(' ',end='')
#         else:
#             print('*',end='')
#     print() 

# n=int(input('enter limit'))
# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#             print('*',end='')
#     print()


# n=int(input('enter no of rows'))
# list1=[]
# for i in range(1,n+1):
#     list1.append('*'*i)
# print('\n'.join(list1))
                
# n=int(input('enter no of rows'))
# for i in range(1,n):
#     for j in range(n,0,-1):
#         if(j>i):
#             print(' ',end='')
#         else:
#             print('*',end='')
#     print()
   
# n=int(input('enter no of rows'))
# ch=65
# for y in range(1,n+1):
#     for x in range(y):
        
#         print('{0}'.format(chr(ch)),end=' ')
#         ch+=1
#     print()

# for y in range(n):
#     for x in range(n-y-1):
        
#         print('{0}'.format(chr(ch)),end=' ')
#         ch+=1
#     print()

# sum=0
# for y in range(n):
#     for x in range(n-y):
#         sum+=1
#         print('{:2d}'.format(sum),end=' ')
        
#     print()

# n=int(input('enter no of rows'))
# for i in range(1,n+1):
#     for j in range(0,2*n):
#         if(j>=i and j<2*n-i):
#             print('',end=' ')
#         else:
#             print('*',end='')
#     print()
# for i in range(n-1,0,-1):
#     for j in range(0,2*n):
#         if(j>=i and j<2*n-i):
#             print('',end=' ')
#         else:
#             print('*',end='')
#     print()
# for i in range(0,n):
#     for j in range(0,2*n):
#         if(j>i and j<2*n-i-1):
#             print(' ',end=' ')
#         else:
#             print('*',end=' ')
#     print()
# for i in range(n-1,0,-1):
#     for j in range(1,2*n+1):
#         if(j>i and j<2*n-i+1):
#             print(' ',end=' ')
#         else:
#             print('*',end=' ')
#     print()


# n=int(input('enter no'))
# c=0
# if(n>1):
#     for x in range(2,int(n/2)+1):
#         if(n%x==0):
#             c=1
#             print('not a prime')
#             break
#     else:
#         print('prime')
# else:
#     print('not prime')

# n=int(input('enter limit'))

# for i in range(1,n+1):
#     c=0
#     j=1
#     if(i>1):
#         for j in range(2,int(i/2)+1):
#             if(i%j==0):
#                 c=1
#                 break
#         if(c==0):
#             print(i)




# prime number btwn 2 limits and sum

# n1=int(input('enter start limit'))
# n2=int(input('enter end limit'))
# sum=0
# for x in range(n1,n2+1):
#     c=0
#     i=1
#     for i in range(2,int(x/2)+1):
#         if(x%i == 0):
#             c+=1
#             break
#     if(c==0 and x!=1):
#         print(x)
#         sum=sum+x
# print('sum: ',sum)  

# n=int(input("enter limit"))
# for x in range(n):
#     for y in range(2*n):
#         if(y>=x and y<=2*n-x-1):
#             print(" ",end=' ')
#         else:
#             print("*",end=' ')
#     print()
# for x in range(n,0,-1):
#     for y in range(2*n):
#         if(y>=x and y<=2*n-x-1):
#             print(" ",end=' ')
#         else:
#             print("*",end=' ')
#     print()

# for x in range(n,0,-1):
#     for y in range(2*n):
#         if(y>=x and y<=2*n-x):
#             print("*",end=' ')
#         else:
#             print(" ",end=' ')
#     print()
# st=input("enter string")
# c=0
# for i in st:
#     if(i=="a" or i=="e"or i=="i"or i=="o"or i=="u" ):
#         c+=1
# print(c)

# a1=[1,2,3,4,5,6,7]
# a2=[2,3,1,0,5]
# flag=0
# miss=[]
# # print(len(a1))
# for i in range(0,len(a1)):
#     for j in range(0,len(a2)):
#         if(a1[i]==a2[j]):
#             flag+=1
#             break
#     else:
#         miss.append(a1[i])
# print(miss)

# a=[19,17,5,7,5,4]
# for i in range(0,len(a)):
#     for j in range(i+1,len(a)):
#         if(a[i]<a[j]):
#             break
#     else:
#         print(a[i])

# s=input('enter the string')
# start=int(input('eneter start index'))
# end=int(input('eneter end index'))
# sub=""
# for i in range(start,end):
#     # print(s[i])
#     sub+=s[i]
# print(sub)

# n=int(input('enter the size of array'))
# a=[]
# b=[]
# for x in range(n):
#     a.append(int(input('enter a no')))
# print(a)
# for i in range(n):
#     if(i==0):
#         t=a[i]*a[i+1]
#         b.append(t)
#     elif(i==n-1):
#         t=a[i]*a[i-1]
#         b.append(t)       
#     else:
#         t=a[i-1]*a[i+1]
#         b.append(t)
# print(b)

# val1=float(input("enter first no: "))
# val2=float(input("enter second no: "))
# ch=input("enter your choice: + - * /   ")
# if(ch=="+"):
#     ans=val1+val2
# elif(ch=="-"):
#     ans=val1-val2
# elif(ch=="*"):
#     ans=val1*val2
# elif(ch=="/"):
#     ans=val1/val2
# else:
#     print("wrong choice!")
# print(ans)

# n=int(input('enter no: '))
# s=''
# while(n>0):
#     x=n%2
#     s+=str(x)
#     n=int(n/2)
# print(s)        
            

    





    


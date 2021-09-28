# print('heloooo')

# exchage values of 2 vars

# a = 20
# b = 25
# x = a 
# a = b
# b = x
# print('a=',a,)
# print()
# print('b=',b)



# largest of three numbers

# n1 = int(input('enter first no'))
# n2 = int(input('enter second no'))
# n3 = int(input('enter third no'))
# if(n1>n2 and n1>n3):
#     print(n1,'is largest')
# elif(n2>n3):
#     print(n2,'is largest')
# else:
#     print(n3,'is largest')



# user verification

# user_name = input('enter user name')
# password = input('enter password')
# n = "asfina"
# p = "1234"
# if(user_name==n and password==p):
#     print('login successfull')
# else:
#     print('invalid login')



# factorial

# num = int(input('enter number'))
# i=1
# fact = 1
# while(i<=num):
#     fact = fact*i
#     i += 1
# print('factorial of',num,'is',fact)



# print odd numbers

# l = int(input('enter limit'))
# i = 1
# while(i<=l):
#     if(i%2==1):
#         print(i,end="")
#     i += 1




# pyramid

limit = int(input('enter limit'))
i=1
x=1
while(i<=limit):
    j=1
    while(j<=i):
        if(j==i):
            print(x,end="")
        else:
            print(x,',',end="")
        j+=1
        x+=1
    print()
    i+=1





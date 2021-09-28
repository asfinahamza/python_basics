# factorial
# n1 = int(input('enter start number:'))
# limit = int(input('enter limit:'))
# i = 1
# limit = 1

# while(i <= limit):
#     limit = limit*i
#     i+=1
# print('factorial:', limit)

# odd no
# while(i <= limit):
#     # print(i)
#     # i = i-1
#     if(n1%2==1):
#         print(n1)
#     n1+=n1

# pyramid
first=int(input('enter no'))
i=1
x=1
while(i<=first):
    j=1
    while(j<=i):
        print(x,end="")
        print(',',end="")
        j+=1
        x+=1
    print()
    i+=1
    

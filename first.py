# a = input('enter no')
# print(a)
# print(type(a))
no1 = int(input('enter first number'))
no2 = int(input('enter second number'))
no3 = int(input('enter third number'))
sum = no1+no2
print(sum)
if(no1<no2 and no3<no2):
   print(no2,'is largest')
elif(no1<no3):
    print(no3,'is largest')
else:
    print(no1,'is largest')



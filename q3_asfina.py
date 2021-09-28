n1=int(input('enter start limit'))
n2=int(input('enter end limit'))
sum=0
for x in range(n1,n2+1):
    c=0
    i=1
    for i in range(2,int(x/2)+1):
        if(x%i == 0):
            c+=1
            break
    if(c==0 and x!=1):
        print(x)
        sum=sum+x
print('sum: ',sum) 
min=int(input("enter start limit"))
max=int(input("enter end limit"))
dis_len=int(input("enter size of disabled set"))
dis=[]
for x in range(dis_len):
    x=int(input("enter a number in disabled set"))
    dis.append(x)
print("disabled set: ",dis)
rep="yes"
while(rep=="yes"):
    num=int(input("enter the number to be checked"))
    if(num>=min and num<max):
        if num in dis:
            num=num+1
        print(num," is available")
    
           
    else:
        print("invalid number")
    rep=input("do you want to continue:yes/no ")



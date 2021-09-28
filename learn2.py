import datetime
import time
import calendar

# x= datetime.datetime(2020,3,12)
# print(x)
# a=time.time()
# a=(time.localtime(time.time()))
# print(a)
# print(calendar.month(2021,3))
# a=lambda x:x+5
# print(a(50))

password=input('enter password')
username=input('enter username')

while(password!='' and username!=''):
    if(password=="123" and username=="asfina"):
        print('login success')
        break
    else:
        print('login failed')
        break
print('login failed')

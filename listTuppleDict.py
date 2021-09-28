# list..

# list=[1,1,2,3,4]
# list1=['str','hello',4,1.44]

# list.remove(1)
# list.pop(3)
# del list[2]
# list.clear()

# list.append('abc')
# list.insert(0,'hello')
# list.extend(list1)
# print(list)
####################

# dictionary..

# l=dict()

# l.update({'val':100})
# l.pop('val')
# print(l)

# dict={'name':'asfi','id':1,'age':23}
# dict.update({'name':'aydi','contact':2345})
# dict.pop('age')
# print(dict)
################

# tupple..
# tup=(2,'hello',[3,4,5])
# tup[2].append(100)
# tup[2].insert(1,'sss')
# tup[2].pop(1)
# del tup[2][1]
# print(tup.index(2))
# print(tup.count(2))
# print(tup)
######################

# sets...

# set=set()
# set.add(23)
# set.add(4)
# set.add(100)
# set.add(100)
# set.remove(23)
# print(set)
# sum=0
# for x in set:
#     sum=sum+x
# print('sum: ',sum)

#list to set

# list=[1,1,1,2,3,3,4,4]
# set=set()
# for x in list:
#     set.add(x)
# print(set)

# list1=[]
# for y in set:
#     list1.append(y)
# print(list1)

#sum of unique elements in a list

# list1=[1,1,1,2,3,3,4,4]
# st=set()
# for x in list1:
#     st.add(x)
# print(st)
# sum=0
# for y in st:
#     sum+=y
# print(sum)


#check a key is present in a dictionary or not
# d={'a':1,'b':2,'c':3}
# d1={'d':4,'e':5}
# key=input('enter the key')
# if key in d.keys():
#     print('present')
# else:
#     print('not present')
# d.update(d1)
# print(d)

#multiply all values in a dictionary
# d={'a':1,'b':2,'c':3}
# mult=1
# for x in d:
#     mult=mult*d[x]
# print(mult)

#lists into dictionary
# l1=['a','s','d']
# l2=[1,2,3]
# # print(len(l1))
# d=dict(zip(l1,l2))
# print(d)

###############

#  convert list to tupple
list1=[1,2,3,4,4]
print(list1)
name=tuple(list1)
print(name)








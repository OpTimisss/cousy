#programm to check eheather a numbe presnent in a tuple or not
t=tuple(input('enter  tuple:'))
print(t)
v=int(input('enter a number:'))
for i in range(len(t)):
    if i==v:
      print('true')

#program to remove an item from list
t=tuple(input('enter tuple:'))
print(t)
l=list(t)
v=input('enter a number:')
for i in l:
    if i==v:
        l.remove(v)
t=tuple(l)
print(t)
 
#program to get index of a given item
t=tuple(input("enter a tuple:"))
print(t)
i=0
v=input('enter a number:')
-while i<len(t):
    if t[i]==v:
        print(v,i)
    i+=1    

#programm to change a list of tuples into list of lists
l=[(1,2),(3,4),(4,5)]
l1=[]
for i in l:
       l1.append(list(i))
print(l1)        

#programm to sum of all the tuples present in a list
l=[(1,2),(3,4),(6,7)]
l1=[]
for i in l:
    l1.append(sum(i))
print(l1)

#
l=[(1,2,3),(5,6,7),(9,7,4)]
l1=[]
for t in l:
   l1=t[:-1]+(100,)
   print([l1]) 



#matrix=[]
rows=int(input('entre the rows in the list:'))
for i in range(rows):
     innerlist=[]
     cols=int(input('enter the colomms in the list:'))
     for j in range(cols):
        value=int(input('enter value:'))
        innerlist.append(value)
     print(innerlist) 
     matrix.append(innerlist)
print(matrix)   

#programm to count odd and even number form the list
l=[]#taking a empty list
n=int(input('enter elements:'))#it's for the  number of values we are goona store in the list
for i in range(n):#for storing value
   x=int(input('enter value'))#enter value
    l.append(x)#inserting values into the list
print(l)
c=0#initaliting count variable
w=0
for j in l:
    if j%2!=0:#checking for odd
        c+=1
    else:#checking for even
        w+=1
print('odd:',c)
print('even:',w)        

#program to check whether a number present in a list or not using membership operator
l=[]
x=int(input('number of rows:'))
for i in range(x):
    n=int(input('enter values:'))
    l.append(n)
print(l)
y=int(input('enter a number:'))
if y in l:
    print('true')

#programm to check weather a number present in a list or not                      
l=[]
x=int(input('enter rows:'))
for i in range(x):
    n=int(input('enter values:'))
    l.append(n)
print(l)
y=int(input('enter the number to check:'))
for j in l:
    if j==y:
        print('true')

#programm to find index of a number
l=[]
x=int(input('enter number of rows:'))
for i in range(x):
    n=int(input('enter value:'))
    l.append(n)
print(l)
v=int(input('enter a number:'))
l.index(v)

#program to take nested list from user and print it         
l=[]
s=int(input("enter rows:"))
for i in range(s):
    v=[]
        n=int(input('enter element:'))
    for j in range(n):
        x=int(input('enter elements:'))
        v.append(x)
    print(v)    
   l.append(v)
print(l)

#programm to take a matrix form user and console it and print sum of each column
matrix=[]#taking a empty list (outer list)
n=int(input('enter rows:'))
for i in range(n):
    list=[]#taking another list (inner list)
    z=int(input("enter columns:"))
    for j in range(z):
       x=int(input('enter elements:'))
       list.append(x)#entering values in inner list
    print(list) 
    matrix.append(list)#appending vlaues  in outer list
print(matrix)
print(end='\n')
#sum of columns
sum=0
for j in range(z):
    for i in range(n):
        sum+=matrix[i][j]  
    print(sum)
    sum=0
print(end="\n")
#sum of rows
sum=0
for i in range(n):
    for j in range(z):
        sum+=matrix[i][j]
    print(sum)
    sum=0    
print(end='\n')
#for sum of diagoanls
sum=0
for i in range(n):
    for j in range(z):
        if i==j:
            sum+=matrix[i][j]   
print(sum)     
print(end='\n')
#to count the numberr of list
count=0
for d in matrix:
    count+=1
print(count)  

i am there best programmer 
and if yu need mm'y help
you can call me any time 
  



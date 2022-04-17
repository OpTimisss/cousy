#programm to writ cubes of number 
n=int(input('enter a number:'))#taking value from user
i=0
cube=1
while i<n:
    i+=1
    cube=i*i*i#cubeing the values
    print(i,cube)

#programm to write factors of a given number
n=int(input('enter a number:'))
i=1
while i<n:
    i+=1
    if n%i==0:
      print(i)


#programm to check wheather a number is prime or not
n=int(input('enter a number:'))
i=2
while i<n:
    if  n%i!=0:
        print('its a prime number')  
        break
    else:
        print('its not a prime number')    
        break
    i+=1

#programm to print fibonadcci seris upto a given number
n=int(input('enter a numnber:'))
n1,n2=0,1
sum=0
if n<=0:
    print('plss add a number greater than zero')
else:
    for i in range(0,n)
        sum=n1+n2
         n1=n2
         n2=sum 
         print(sum,end=" ")

#programm to find factorial of any number
n=int(input('enter a number:'))
fact=1
for i in range(1,n-1):
    fact=fact*i
print(fact)

#programm to count number of character
n=int(input('enter a number:'))
rev=0
while n>0:
    rev=(rev*10)+(n%10)
    n=n//10
print(rev)

#programm to write sum of first and previous number
n=int(input('enter a number:'))
pre=0
for i in range(1,n):
    sum=pre+i
    print(sum)
   pre=i
    

    
#programm for multiplications of list
#l=[10,20,30,40]
#sum=1
#i=0
#while i<len(l):
 #   sum=sum*l[i]
  #  i+=1
#print(sum)

#programm for finding greatest number
#l=[10,20,30,40,50]
#max=l[0]
#for i in l:
 #   if max<i:
  #      max=i
#print(max)

#programm for finding minimum nmber
#l=[10,70,80,40,90,30,20,950,620,32110]
#min=l[7]
#for i in l:
 #  if min>i:
 #    min=i
#print(min)

#programm for counting even numbers 
#l=[10,12,40,56,1,3,5,7,9,5,0,70]
#e=0
#for i in l:
 # if i%2==0:
  #  e+=1
#print(e)

#programm for counting odd numbers           
#l=[10,12,40,56,1,3,5,7,9,5,0,70]
#e=0
#for i in l:
 #  if i%2==1:
  #   e+=1
#print(e)

#programm for counting both even and odd numbers
#l=[10,14,5,7,6,80,342423563,325336,56345674586,534648,346479,346456745,99990]
#e=0
#o=0
#for i in l:
 # if i%2==0:
  #  e+=1
  #else:
   # o+=1  
#print('even numbers:',e) 
#print('odd number:',o)   

#programm for checking whether a number present in list or not using membership operator
#a=int(input('enter a number:'))
#l=[1,2,3,4,5,6,78,89,0,9,0,]
#if a in l:
#  print('yes')
#else:
 # print('no')  

#programm for checking a number present in a list without using membership operator
a=int(input('enter a number:'))
l=[1,2,3,4,5,6,7,8,9,19,18,14,4232336,423456367,23445686,4536]
for i in l:
  if i==a:
    print('yess')
  else:
    print('no') 
    
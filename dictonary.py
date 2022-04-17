from array import*
# vals=array('i',[])
# x=int(input('enter a number:'))
# for i in range(x):
#     n=int(input('number:'))
#     vals.append(n)
# print(vals)    
# v=int(input("enter a number:"))
# k=0
# for e in vals:
#     if v==e:
#         k+=1
#         print(k)


# arr=array('i',[])
# Arr=list(arr)
# l=max(Arr)
# k=''
# while l in Arr:
#     Arr.remove(l)
# print(l)    
def avg(l):
    avg=sum(l)/len(l)
    print(avg)
d={'a':[32,45,67],'b':[98,64,32],'x':[65,43,12]}
x=input()
for i in d:
    if i==x:
        print(avg(d[x]))
    
    
              

    

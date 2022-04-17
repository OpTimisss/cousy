#programm to find a character using membership operatot
# s=input('string:')
# if "e" in s:
#     print('founded')
# else:
#     print('not found')    

#programm to find a charactor in a string whithout using member ship operator
s=input('enter a string:')
sub=str(input("enter s letter"))
f=0
for i in s:
    if i==sub:
        f+=1
        print(f)


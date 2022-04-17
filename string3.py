#programm to take input form user and convert it into upper and lower case
s=input('enter a strings:')
e=" "
for i in s:
    if(i.isupper())==True:
        e+=(i.lower())
    elif(i.islower())==True:
        e+=(i.upper())
    elif(i.isspace())==True:
        e+=i
print(e)      
   
#programm to convert a 2string into upper case if 2 letters in upper out of 4
# s=input('enter a string:')
# e=0
# f=''
# for i in s[:4]:
#     if i.isupper()==True:
#               e+=1
# if e>=2:
#     for i in s:
#         f+=i.upper() 
# else:
#     print(s)
# print(f)    


# #program to take a string and make a new string from frist 2 and last 2 char of the string
# s=input('enter a string:')
# f=s[0:2]
# g=s[-2:]
# e=0
# for i in s:
#         if e<=2:
#           print(f+g)
#           e+=1
#           break
# if e>=2:
#     print(s)
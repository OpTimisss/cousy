
#s=input('enter a string:')
# print(s.index('e'))
# print(s.find('m'))

# #programm to find inddex of  a char in string
# s=input('enter a string:')
# for a in range(len(s)):
#     if s[a]=='e':
#          print(a)
n=int(input())
if n>1:
    for i in range(2,n):
            if n%i==0:
                print("it's nat a prime number")
                break
    else:
        print("it's a prime")
            
# class employee:
#      no_of_periods=10#classs varibale
#      def __init__(self,name,salary,post):
#          self.name=name
#          self.salary=salary
#          self.post=post
#      def personaldetails(self):
#          return f"name is {self.name}. salary is {self.salary}. role is {self.post}"  
         
# sameer=employee('sameer',3445,'HR')
# print(sameer.personaldetails())       
         
     
# sameer=employee()#objectn
# rohit=employee()

# sameer.name='sameeer'
# sameer.salary=120000
# sameer.post='HR'
# sameer.subject=['maths','science','computer']
# sameer.no_of_periods=15#instant variable


# rohit.name='rohit'
# rohit.salary=4600000
# rohit.post='instructor'

# print(sameer.personaldetails())
# print(rohit.personaldetails())
# def series_sum(n):
#     sum=0
#     for i in range(1,n+1):
#         if i%2==0:
#             sum=sum+(-1)*(i**2)
#         else:
#             sum=sum+(i**2)
#     return sum
# n=int(input('enter a number'))
# print(series_sum(n))       
s=input('enter a string')
sum=0
for i in s:
    sum+=1
    print(i*sum,end=' ')   
# def f(n):
#         if n % 5 == 0:
#            return n * 10
#         else:
#            return n + 10
# def display(m = 5):
#         for i in range(0, m):
#             print(f(i), end = '$')
#             print('\n')
# display(7)
# display()
# display(3)
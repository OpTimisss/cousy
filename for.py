# def fact_itrative(n):
#     fact=1
#     for i in range(n):
#         fact=fact*(i+1)   
#     return fact    
# print(fact_itrative(7))       

# def fact_recursive(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact_recursive(n-1)
# print(fact_recursive(8))    

def fib_recursive(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib_recursive(n-1)+fib_recursive(n-2)
print(fib_recursive(3))    

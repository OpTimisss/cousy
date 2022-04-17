# s=input('enter a string:')
# print(s.count('e'))

# #PROGRAMM TO COUNT OCCURANCE OF A CHAR IN STRING
# s=input('enter a string:')
# i=0
# for a in s:
#     if a=='e':
#         i+=1
# print(i)

# #program to count occurance of a given char
# s=input('enter a string:')
# c=input('check the frequency:')
# e=0
# for i in s:
#     if i==c:
#         e+=1
# print(c,"occurs",e,'times')       

# #programm to check the occurance of a character 
# s=input('enter a string:')
# c=input('enter the character:')
# i=0
# x=0
# while i<len(s):
#     if i==c:
#       x+=1
#     i+=1    
# print(c,'occurs',x)    

# class Library:
#     def __init__(self, book_list, library_name):
#         self.book_list = book_list
#         self.library_name = library_name
#         self.lend_record = {}

#     def display_book(self):
#         print(self.book_list) 

#     def add_book(self):
#         book = input("Enter book name : ")
#         self.book_list.append(book)   

#     def lend_book(self):
#         book = input("Enter book name : ").capitalize()
#         if book not in self.book_list:
#             print("Please enter valid input")
#         if book in self.book_list:
#             name = input("Enter your name : ")
#             self.book_list.remove(book)   
#             self.lend_record[book] = name            
#         else:
#             if self.lend_record.get(book):
#                 print(f"Book does not exist in library this book taken by {self.lend_record[book]}")

#     def return_book(self):
#         book = input("Enter book name : ").capitalize()
#         if book in self.lend_record:
#             self.book_list.append(book)      
#             del self.lend_record[book]
#         else:
#             print("Please enter valid input")             

# if __name__=='__main__':
#     book_list = ['C++','Java','JavaScript','Python']
#     karan_library = Library(book_list, 'karan_library')

#     while True:
#         user = input("\nD for Display book, A for Add book, L for lend book, R for return book, and Q for exit :")
#         if user == "Q" or user == "q":
#             break
#         elif user == "display" or user == "d" or user == "D":
#             karan_library.display_book()
#         elif user == "add" or user == "a" or user == "A":
#             karan_library.add_book()
#         elif user == "lend" or user == "l" or user == "L":
#             karan_library.lend_book()
#         elif user == "return" or user == "r" or user == "R":
#             karan_library.return_book()
# insertion sort
def inser(l):
    for i in range(1,len(l)):
        sort=l[i]
        j=i-1
        while j>=0 and sort<l[j]:
            l[j+1]=l[j]
            j=j-1
        else:
            l[j+1]=sort
    return l
l=[156,7899,23,131,1,0,314254,56,-2]
print(inser(l))
            


 

        

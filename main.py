# # -----------------N1---------------------------
# class Book:
#     def __init__(self,id,title,year,price):
#         self.id = id
#         self.tittle = title 
#         self.year = year
#         self.price = price
#         self.dict={}
        
        
#     def create_data(self):
#         if self.id < 0:
#             self.id += 1
    
#     def update(self,id, data):
#         self.dict = id
        
#     def delete(self,id):
#         pass
    
#     def get_all(self,id):
#         print(f"{self.id} {self.tittle} {self.year} {self.price} ")
        
# c = Book(2,"Odina",2019,50)
# c.get_all(3)
        
        
# class Author:
#     def __init__(self,author,title,year,price):
#         self.id = author
#         self.tittle = title 
#         self.year = year
#         self.price = price
#         self.dict={}
        
        
#     def create_data(self):
#         if self.id < 0:
#             self.id += 1
    
#     def update(self,author, data):
#         self.dict = id
        
#     def delete(self,author):
#         pass
    
#     def get_all(self,author):
#         print(f"{self.id} {self.tittle} {self.year} {self.price} ")
        
# c = Author(2,"Odina",2019,50)
# c.get_all(3)
        
        
        
        
        
# ---------------------N2-------------------------------
# class Publication:
#     def __init__(self,tittle,year):
#         self.tittle = tittle
#         self.year = year
        
#     def get_info(self):
#         print(f"{self.tittle} {self.year}")
        
# class Book(Publication):
#     def get_info(self,pages):
#         print(f"Book: {self.tittle} ({self.year}) {pages} pages")
        

# class Magazine(Publication):
#     def get_info(self,issue_number):
#         print(f"Magazine: {self.tittle} {self.year} issue {issue_number}")


# book = Book("Tojikon",2020)
# book.get_info(460)

# magaz = Magazine("Forbes",2024)
# magaz.get_info("#7")
# -----------------------------N3----------------------------

# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner = owner
#         self.__balance = balance
        
#     def get_info(self,initial_balance = 0):
#         if initial_balance >= 0:
#             self.__balance = initial_balance
#             return self.__balance
        
#     def deposit(self,amount):
#         if amount > 0:
#             self.__balance += amount
            
#     def withdraw(self,amount):
#         if amount > 0 and amount <= self.__balance:
#             self.__balance -= amount
            
# c = BankAccount("Numon",1500)
# c.deposit(50)
# print(c.deposit(50))
# c.withdraw(50)
# print(c.get_info())
# print(c.get_info(150))


    

# ----------------------------N4---------------------------
# class Shape:
#     def __init__(self,name):
#         pass
    
# class Circle(Shape):
#     def area(self,radius):
#         return 3.14 * radius ** 2
    
# class Rectangle(Shape):
#     def area(self,width,height):
#         return width * height
    
# class Triangle(Shape):
#     def area(self,base,height):
#         return 0.5*(base * height)


# c = Circle("Circle: ")
# print(f'Circle: area = {c.area(3)}')

# r = Rectangle("Rectangle: ")
# print(f'Rectangle: area = {r.area(4,5)}')

# f = Triangle("Triangle")
# print(f"Triangle: area = {f.area(6,2)}")


# from abc import ABC,abstractmethod
# class Employee(ABC):
#     @abstractmethod
#     def __init__(self):
#         super().__init__()


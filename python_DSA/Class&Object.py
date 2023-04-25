# Class and object in Python
# A class is a blueprint or template for creating objects. It defines a set of attributes and methods that the objects of the class will have.
# An object is an instance of a class, created from the blueprint defined by the class. It represents a specific instance of the class, with its own set of attribute values and method behavior.
# Self paramter is refrence of current instance of the class.
# creating a class
class Data:
    num = 20
    
print(Data)

if __name__ == "__main__":
    print(Data)
    
# <class '__main__.Data'>
# <class '__main__.Data'>

# creating a object
class Student:
    name = "joe"
    
obj = Student()
print(obj)
print(obj.name)

# <__main__.Student object at 0x1e570c8>
# joe


# constructor (__init__)
class Employee:
    # create constructor
    def __init__(self,name,id):
        self.name = name
        self.id = id
    
emp_obj = Employee("love",876384762)
print(emp_obj.name,emp_obj.id)
# love 876384762


# creating methods
class Salary:
    def __init__(self,amount,date,name,id):
        self.amount = amount
        self.date = date
        self.name = name
        self.id = id
       
    # create method
    def display(self):
        print("----------------------".center(50))
        print("Amount is : ",self.amount)
        print("Employee Name is :",self.name)
        print("Employee ID : ",self.id)
        print("Date : ",self.date)
        
# create object
salary1_obj = Salary(30000,"20-02-2024","Joe Goldberg",264687264)
salary1_obj.display()

salary2_obj = Salary(50000,"15-10-2024","Beck chris",1898634)
salary2_obj.display()


#               ----------------------              
# Amount is :  30000
# Employee Name is : Joe Goldberg
# Employee ID :  264687264
# Date :  20-02-2024
#               ----------------------              
# Amount is :  50000
# Employee Name is : Beck chris
# Employee ID :  1898634
# Date :  15-10-2024

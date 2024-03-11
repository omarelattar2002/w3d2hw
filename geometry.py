#E1
# class Employee:
#     def __init__(self, first, last, title, salary):
#         self.first = first
#         self.last = last
#         self.title = title
#         self.salary = salary
#         self.email = first[0] + '.' + last[0] + '@gmail.com'


#     def __str__(self):
#         return f"{self.first} {self.last} {self.title}"
        

#     def salary_raise(self):
#         print (self.salary * 1.05)
    
# class Sales(Employee):
#     def __init__(self, first, last, title, salary, number):
#         super().__init__(first, last, title, salary,)
#         self.number = number

#     def FW_email(self, customer):
#         print(f"Dear {customer}, Thank you for your interest in our product. Please let me know if you have any qustions. my email is {self.email} and my phone number is {self.number}")

# class Development(Employee):
#     def code(self):
#         print(f"{self} is writing your code")


# sales = Sales('Omar', 'Elattar', 'Software engineer', 50000 ,'9521118566')

# sales.FW_email('Mike O "Neil'.title())
# sales.FW_email('Hannah stern'.title())


# employee = Development('Omar', 'Elattar', 'software engineer', 100000)

# employee.salary_raise()

#E2
from math import pi, sqrt

def area(radius):
    return pi * radius**2

def pythagorean(a,b):
    return sqrt(a**2 + b**2)




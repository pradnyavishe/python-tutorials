# Input Function in Python

a =input()
print(a)


a = input()
print(int(a)+int(a))

# input function always reads input value as a string

name = input("Enter your name: ")
print(f"Welcome {name} to the Python Tutorial Series")

age = input("Enter your age: ")
print(f"Ohhh you are just {age}!")
print(f"So next year you will be {int(age)+1}!")

# Multiple input from user
# Input from user to add two number and print result
x = input("Enter first number: ")
y = input("Enter second number: ")
print(f"The sum of {x} and {y} is {int(x) + int(y)}")

# Hw: Write a program to input student name and marks of 3 subjects.
# print name and percentage.

name = input("Enter your name: ")
sub1 = input("Enter marks of Maths out of 100: ")
sub2 = input("Enter marks of Science out of 100: ")
sub3 = input(" Enter marks of Histpry out of 100: ")
percentage = (((int(sub1) + int(sub2) + int(sub3))/300))*100
print(f" {name} got {int(percentage)} %")  

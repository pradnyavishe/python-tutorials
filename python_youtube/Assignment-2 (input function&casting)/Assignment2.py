# # Assignment - 2
# # Q1. Write a program to input student name and marks of 3 subjects. Print name and percentage.

# name = input("Enter your name: ")
# sub1 = input("Enter marks of Maths out of 100: ")
# sub2 = input("Enter marks of Science out of 100: ")
# sub3 = input(" Enter marks of Histpry out of 100: ")

# # Calculating percentage
# percentage = (((int(sub1) + int(sub2) + int(sub3))/300))*100

# # Print result
# print(f" {name} got {int(percentage)} %") 

# # Optimized solution
# print("Percentage Calculator")
# name = input("Enter your name: ")
# sub1 = int(input("Enter marks of Maths out of 100: "))
# sub2 = int(input("Enter marks of Science out of 100: "))
# sub3 = int(input(" Enter marks of History out of 100: "))

# # Calculating percentage
# percentage = ((sub1 + sub2 + sub3)/300)*100

# # Print result
# print(f" The result of {name} is {int(percentage)} %. Well done!")


# # Q2. Write a Python program that collects multiple types of data (e.g. name, age, height and
# # students status) from user input, stores them in a dictionary and then prints out the collected data.

# # initializing  a dictionary
user_data = {}

# # input from user
user_data['name'] = input("Enter your name: ")
user_data['age'] = int(input("Enter your age: "))
user_data['height'] = float(input("Enter your height: "))
user_data['student'] = input("Are you a student (yes/no)")

# # print the input from user
print(user_data)
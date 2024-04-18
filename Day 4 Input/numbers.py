#Below program shows how to take input as numbers and print the sum of the numbers
print("Welcome to the number addition program")
print("Enter the first number:")
num1 = input()
print("Enter the second number:")
num2 = input()
print("The sum of the numbers is:")
print(num1 + num2)

#If you see above program there is a catch here. if you run the program and ente the numbers, it will not give you the sum of the numbers. It will concatenate the numbers. This is because the input() function returns the input as a string. To perform arithmetic operations on the input numbers, we need to convert them to integers or floats using the int() or float() functions.
#To fix this issue, we can modify the program to convert the input numbers to integers before performing addition. Here's an updated version of the program that converts the input numbers to integers and prints their sum:

# print("Welcome to the number addition program")
# print("Enter the first number:")
# num1 = int(input())
# print("Enter the second number:")
# num2 = int(input())
# print("The sum of the numbers is:")
# print(num1 + num2)

#In this version of the program, we are using the int() function to convert the user input to integers before performing addition. This ensures that the input numbers are treated as numerical values rather than strings, allowing us to perform arithmetic operations on them. Now, when you run the program and enter two numbers, it will correctly calculate and display their sum.
#here is the example of the input file 
print("Welcome to the user input program")
print("Enter your name:")
input_name = input()
print("Hello " + input_name + "!")

#In the above code snippet, we are using the input() function to take user input from the console. The input() function reads a line of text from the console and returns it as a string. We are storing the input in a variable called input_name and then printing a greeting message using the input value.
#When you run this program, it will prompt you to enter your name in the console. After entering your name and pressing Enter, the program will display a greeting message with the input name.
#You can use the input() function to take user input for various purposes, such as collecting user information, accepting user commands, or customizing program behavior based on user input. It provides a simple way to interact with users and create interactive programs in Python.
#If you see the input is stored as a string. If you want to convert it to an integer or float, you can use the int() or float() functions respectively. For example, int(input()) will convert the user input to an integer, and float(input()) will convert it to a float. This can be useful when working with numerical input from the user.
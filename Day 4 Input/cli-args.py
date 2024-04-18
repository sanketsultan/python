import sys

print(sys.argv)
print(sys.argv[0]) # program name
print(sys.argv[1]) # first arg

#if you run above code with python3 cli-args.py hello world  it will print ['cli-args.py', 'hello', 'world'] hello world. 
#Here, sys.argv is a list that contains the command-line arguments passed to the script. The first element of the list is the name of the script itself, and the subsequent elements are the arguments passed to the script. You can access individual arguments using their index in the list. In this case, sys.argv[0] is the name of the script, sys.argv[1] is the first argument, and so on.
#You can use this feature to pass arguments to your Python scripts from the command line. This can be useful for providing input data, configuration options, or other parameters to your script when running it from the terminal or command prompt.
#For example, you could create a script that takes a filename as an argument and reads the contents of the file, or a script that takes a URL as an argument and downloads the content from that URL. Command-line arguments provide a flexible way to interact with your Python scripts and customize their behavior based on user input.
#To run the script with command line arguments, you can use the following command:
#python3 cli-args.py hello world
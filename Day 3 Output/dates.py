from datetime import date
print("Today's date is: " + str(date.today())) #it will print the current date in the format yyyy-mm-dd

#note here we are passing the date.today() function to the str() function to convert the date object to a string object.
#if we don't do this it will throw an error as the print function can only print string objects.
#also, we are using the + operator to concatenate the string "Today's date is: " with the date object returned by date.today() function.
#this is an example of how operators can be used to manipulate data in python.
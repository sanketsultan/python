# Python operators are symbols that perform operations on variables and values. They can be used for arithmetic, comparison, assignment, logical operations, and more. Operators in Python include +, -, *, /, %, ==, !=, >, <, and many others. They are essential for manipulating data and controlling program flow.

#left side and right side of the operator are called operands. For example, in the expression 5 + 3, 5 and 3 are operands, and + is the operator.
left_operand = 5
right_operand = 3
left_operand + right_operand #output: 8 Where + is the operator and 5 and 3 are operands

#assignment operator
#The assignment operator is used to assign a value to a variable. It is denoted by the = sign.
a = 10 #assigns the value 10 to the variable a
b = 5 #assigns the value 5 to the variable b
c = a + b #assigns the sum of a and b to the variable c
print(c) #output: 15
a += 5 #equivalent to a = a + 5
print(a) #output: 15
b -= 2 #equivalent to b = b - 2
print(b) #output: 3
c *= 2 #equivalent to c = c * 2
print(c) #output: 30
d = 10
d /= 2 #equivalent to d = d / 2
print(d) #output: 5.0
e = 10
e %= 3 #equivalent to e = e % 3
print(e) #output: 1
# Day1: Variables, Data Types, Comments, Input Function, Type Casting, Arithmetic Operations, f-strings, Handson-Session

print("Hello, World")

# **Variables:
number = 10 
point = 3.14
name = "John" 
is_true = True
print("Number:", number)
print("Name:", name)

# **Data Types: int, float, str, bool
print("Number:", type(number))
print("Point:", type(point))
print("Name:", type(name))
print("Is True:", type(is_true))


# **Comments:
# : This is a single-line comment
"""
This is a multi-line comment
It can span multiple lines.
"""

# **Function: input(), type(), float(), int()
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

# data types
print("Num1:", type(num1))
print("Num2:", type(num2))

# **type casting
# num1 = int(num1)
# num2 = int(num2)

num1 = float(num1)
num2 = float(num2)

# **arithmetic operations
sum = num1 + num2
diff = num1 - num2
prod = num1 * num2
quot = num1 / num2

# output
print("Sum:", sum)
print("Difference:", diff)
print("Product:", prod)
print("Quotient:", quot)


# **Different ways of Print Output
#Goal: This is the day one of AI/ML class.
print("This is the day one of AI/ML class.")
print("This is the day one of AI/ML class.", end='') # end='' prevents newline
print("This is the day one of AI/ML class.", sep=' # ') # sep='#' changes the separator
print("This", "is", "the", "day", "one", "of", "AI/ML", "class.")
print("This", "is", "the", "day", "one", "of", "AI/ML", "class.", sep=' 8 ')

#Goal: This @ is @ the @ day @ one @ of @ AI/ML @ class.
print("This", "is", "the", "day", "one", "of", "AI/ML", "class.", sep=' @ ')


# Goal: Hello world
print("Hello world")
print("Hello", "world")  # prints with space
print("Hello" + " world")  # prints without space


## **print different print output in one line
print("Hello", end='')  # prints without newline
print(" world")  # prints with newline

#Goal: This @ is @ the @ day # one # of # AI/ML # class.
print("This", "is", "the", "day", sep=' @ ', end=' ')
print("one", "of", "AI/ML", "class.", sep=' # ')


# ** f-strings
num = 1
print("The value of num is:",num)
print(f"The value of num is: {num}")

name = "John"
print("Hello, " + name + "!") 
print(f"Hello, {name}!")

Point = 3.14
print("The value of Point is:", Point)
print(f"The value of Point is: {Point}")

num1 = 56.3840
print(f"The value of num1 is: {num1:.2f}")


#**Handon-Session
num1 = float(input('Enter a number: '))
num2 = float(input('Enter another number: '))
sum = num1 + num2
diff = num1 - num2
pro = num1 - num2
quot = num1 / num2
print(f"The sum of {num1} and {num2} is: {sum:.2f}")
print(f"The difference of {num1} and {num2} is: {diff:.2f}")
print(f"The product of {num1} and {num2} is: {pro:.2f}")
print(f"The quotient of {num1} and {num2} is: {quot:.2f}")



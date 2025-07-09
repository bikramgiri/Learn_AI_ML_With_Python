# Day7: how to use User define functions, Made temperature converter celsius to fahrenheit, find the maximum and minimum number from user inputs,Created a simple calculator for basic operations (+, -, *, /),  Explored the power of import time for working with time-based functions, print your name and place of origin with a 2 seconds delay between the two prints using the time module
# ** User-defined functions
"""
Syntax:
def function_name(parameters(s), default parameters can also be defined):
     statements.....
     return variable / value
function call 
function_name(values(s) / variables(s))

"""
# **WAP that greets the user using a function
# here, greet(variable) and {variable} isnot necessary to be same, but in main function it is necessary to be same
def greet(name):
      print(f"Hello, {name}! Welcome to the program.")

name = input("Enter your name: ")
greet(name)

# **OR
# here, greet(variable) and {variable} is necessary to be same in main function but not in other function
def greet(nam):
    print(f"Hello, {nam}! Welcome to the program.")

def main():
      name = input("Enter your name: ")
      greet(name)
main()

# **OR
def greet(nam = "User"):
    print(f"Hello, {nam}! Welcome to the program.")

def main():
      name = input("Enter your name: ")
      greet()
      greet(name)
main()

# ** temperature converter celsius to fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
def main():
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius:.2f}°C is equal to {fahrenheit:.2f}°F")
main()

# ** WAP to find the maximum among three numbers
def find_maximum(num1, num2, num3):
    if (num1>num2) and (num1>num3):
        return num1
    elif (num2>num1) and (num2>num3):
        return num2
    else:
        return num3
def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    max_num = find_maximum(num1, num2, num3)
    print(f"The maximum number is: {max_num:.2f}")
# ** OR
#       num1, num2, num3 = map(float, input("Enter three numbers separated by space: ").split())
#       max_num = find_maximum(num1, num2, num3)
#       print(f"The maximum number is: {max_num:.2f}")
# main()

# **OR
def find_maximum(a, b, c):
    return max(a, b, c)
def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    max_num = find_maximum(num1, num2, num3)
    print(f"The maximum number is: {max_num:.2f}")
main()

# ** WAP to find the minimum among three numbers
def find_minimum(num1, num2, num3):
    if (num1<num2) and (num1<num3):
        return num1
    elif (num2<num1) and (num2<num3):
        return num2
    else:
        return num3
def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    min_num = find_minimum(num1, num2, num3)
    print(f"The minimum number is: {min_num:.2f}")
main()


# ** Build a simple calculator that perform addition, subtraction, multiplication, and division of 2 numbers according to the user input uing the concept of functional programming. Also check if divisor is 0 than print "Division by zero is not allowed"
def add(a, b):
      return a + b
def subtract(a, b):
      return a - b
def multiply(a, b):
      return a * b
def divide(a, b):
      if b == 0:
            return "Division by zero is not allowed"
      else:
            return a / b
def calculator():
      print("Select operation:")
      print("1. Addition")
      print("2. Subtraction")
      print("3. Multiplication")
      print("4. Division")
      
      choice = input("Enter choice (1/2/3/4): ")
      
      if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                  result = add(num1, num2)
                  return f"The sum of {num1} and {num2} is: {result:.2f}"
            elif choice == '2':
                  result = subtract(num1, num2)
                  return f"The difference of {num1} and {num2} is: {result:.2f}"
            elif choice == '3':
                  result = multiply(num1, num2)
                  return f"The product of {num1} and {num2} is: {result:.2f}"
            elif choice == '4':
                  result = divide(num1, num2)
                  return result if isinstance(result, str) else f"The quotient of {num1} and {num2} is: {result:.2f}"
            else:
                  return "Invalid input! Please select a valid operation."
def main():
      print(calculator())
main()



# ** Time concept in python
# WAp to print your name and place of origin with a 2 seconds delay between the two prints using the time module
import time
print("My name is Bikram Giri")

time.sleep(2)

print("I am from Itahari.")

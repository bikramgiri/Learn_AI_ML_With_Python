# Day8:  Error handling in python: Syntax error, Logical error, Exceptions, try-except, try-except-else, try-except-finally, pass, and raise

# **Syntax error
print("Hello, World!") 

#**Logical error
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

sum = num1 - num2 # **Logical error
print(f"The sum is: {sum}")

# **Exceptions: It is an error that occurs during the execution of a program, disrupting the normal flow of the program's instructions.
# ** It also means user input is not valid or the program is not able to handle the input properly.
x = int(input("Enter a number: "))
print(f"The number you entered is: {x}")

# ** try-except value error
# **Handling exceptions using try-except block
try:
    x = int(input("Enter a number: "))
    print(f"The number you entered is: {x}")
except ValueError:
    print("Invalid input! Please enter a valid number.")

# **Using try-except else block
# **The else block is executed if the try block does not raise an exception.
try:
    x = int(input("Enter a number: "))
except ValueError:
    print("Invalid input! Please enter a valid number.")
else:
      print(f"The number you entered is: {x}")

#  **Using a loop to ensure valid input until the user provides a valid input
# This will keep asking the user for input until a valid number is entered.
while True: # Loop until a valid input is received
      try:
            x = int(input("Enter a number: "))
      except ValueError:
            print("Invalid input! Please enter a valid number.")
      else:
            break
print(f"The number you entered is: {x}")

# ** pass
# **The pass statement is used to indicate that no action is required. It is often used as a placeholder in code blocks where syntactically some code is required but no action is needed.
# **Using a loop to ensure valid input until the user provides a valid input if the input is not valid pass the exception 
while True: # Loop until a valid input is received
      try:
            x = int(input("Enter a number: "))
      except ValueError:
            pass
      else:
            break
print(f"The number you entered is: {x}")

def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError:
        print("Invalid input! Please enter valid numbers.")
sum(5, 5)  # This will raise a TypeError because "10" is a string, not a number.

## ** Division by zero error
# **Division by zero is a common runtime error that occurs when a program attempts to divide a number by zero.
# **This error can be handled using a try-except block to prevent the program from crashing 
# Task -> program -> takes a number -> divides 10 by the entered number.
while True:
    try:
        x = int(input("Enter a number: "))
        result = 10 / x
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    except ZeroDivisionError:
        print("Division by zero error! Please enter a non-zero number.")
    else:
        break
print(f"The result is: {result:.2f}")

# **OR

while True:
    try:
        x = int(input("Enter a number: "))
        result = 10 / x
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    except ZeroDivisionError:
        print("Division by zero error! Please enter a non-zero number.")
    else:
        break
print(f"The result is: {result:.2f}")

# **OR

while True:
    try:
        x = int(input("Enter a number: "))
        result = 10 / x
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    else:
        break
print(f"The result is: {result:.2f}")


# **OR

while True:
    try:
        x = int(input("Enter a number: "))
        result = 10 / x
    except (ValueError, ZeroDivisionError):
        pass
    else:
        break
print(f"The result is: {result:.2f}")

# **OR

while True:
    try:
        x = int(input("Enter a number: "))
        result = 10 / x
    except ValueError:
        print(ValueError, "Invalid input! Please enter a valid number.")
    except ZeroDivisionError:
        print(ZeroDivisionError, "Division by zero error! Please enter a non-zero number.")
    else:
        break
print(f"The result is: {result:.2f}")

try:
    num = int(input("Enter a number: "))  # This will raise a ValueError
except ValueError as e:
    print("Caught an error:", e)
print(f"The number you entered is: {num}")


# **Using finally block
# **The finally block is executed no matter what, whether an exception occurs or not. It is often used for cleanup actions, such as closing files or releasing resources.
while True:
    try:
        x = int(input("Enter a number: "))
        result = 10 / x
    except (ValueError, ZeroDivisionError):
        pass
    else:
        break
# finally:
#     print("This will always execute, regardless of whether an exception occurred or not.")
# print(f"The result is: {result:.2f}")

# def main():
#       x = get_int()
#       print(f"The number you entered is: {x}")

def get_int():
      while True:
         try:
            x = int(input("Enter a number: "))
         except ValueError:
            print(ValueError, "Invalid input! Please enter a valid number.")
         else:
            return x


# **WAP that that accept 3 number as input and calculate sum, product & operation = (num1 + num2)/num3, so check wether num3 is zero or not, if num3 is zero then print sum and product but in case of operation print "Division by zero error! Please enter a non-zero number." and ask user enters a non-zero number for num3 until user enters a non-zero number else print the result by using a functional programming approach.
def main():
    num1, num2, num3 = get_numbers()
    sum_result = num1 + num2
    product_result = num1 * num2
    operation_result = calculate_operation(num1, num2, num3)
    
    print(f"Sum: {sum_result}")
    print(f"Product: {product_result}")
    if operation_result is not None:
        print(f"Operation result: {operation_result:.2f}")
    else:
            print("Division by zero error! Please enter a non-zero number for num3.")
            num3 = get_non_zero_number()
            operation_result = calculate_operation(num1, num2, num3)
            print(f"Operation result: {operation_result:.2f}")
            
def get_numbers():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            num3 = float(input("Enter the third number: "))
            return num1, num2, num3
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
        except ZeroDivisionError as e:
            print(e)
            continue
      
def calculate_operation(num1, num2, num3):
    try:
        return (num1 + num2) / num3
    except ZeroDivisionError:
        return None
def get_non_zero_number():
      while True:
            try:
                  num3 = float(input("Enter a non-zero number for num3: "))
                  if num3 == 0:
                      print("Division by zero error! Please enter a non-zero number.")
                      continue
                  return num3
            except ValueError:
                  print("Invalid input! Please enter a valid number.")
            except ZeroDivisionError as e:
                  print(e)
                  continue
if __name__ == "__main__":
      main()

# **OR

while True:
    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))
        num3 = int(input("Enter another number: "))
        
        operation = (num1+num2)/num3
        
    except ValueError:
        pass

    except ZeroDivisionError:
        pass

    else:
        sum = num1 + num2 + num3
        product = num1 * num2 * num3
        print(f"sum = {sum}")
        print(f"Product = {product}")
        print(f"Operation = {operation}")
      
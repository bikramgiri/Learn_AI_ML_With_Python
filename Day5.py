#Day5: if, if else, if elif....else, nested, match case statements

# **if statement
x = 90
if x > 5:
    print("x is greater than 5")


# **if else statement by taking input from user
x = int(input("Enter a number: "))
if x > 0:
    print("x is positive")
else:
    print("x is negative")


# **if elif..... else statement
x = int(input("Enter a number: "))
if x > 0:
    print("%d is positive" % x)
elif x < 0:
    print("%d is negative" % x)
else:
    print("%d is zero" % x)


#**WAP to check whether a enter number is odd or even
x = float(input("Enter a number: "))
if x % 2 == 0:
    print("%.2f is even" % x)
else:
    print("%.2f is odd" % x)


#**WAP to check whether a number is prime or not
x = int(input("Enter a number: "))
if x > 1:
    for i in range(2, x):
        if x % i == 0:
            print("%d is not prime" % x)
            break
    else:
        print("%d is prime" % x)
else:
    print("%d is not prime" % x)


#**WAP to check whether a enter number is prime or composite use if else statement
x = int(input("Enter a number: "))
if x > 1:
    for i in range(2, x):
        if x % i == 0:
            print("%d is composite" % x)
            break
    else:
        print("%d is prime" % x)

#**WAP to check whether a enter number is prime, odd or even
x = int(input("Enter a number: "))
if x > 1:
    for i in range(2, x):
        if x % i == 0:
            print("%d is not prime" % x)
            if x % 2 == 0:
                print("%d is even" % x)
            else:
                print("%d is odd" % x)
            break
    else:
        print("%d is prime" % x)
        if x % 2 == 0:
            print("%d is even" % x)
        else:
            print("%d is odd" % x)


#**WAP to check whether a enter number is prime, odd or even using if elif else statement
x = int(input("Enter a number: "))
if x > 1:
    for i in range(2, x):
        if x % i == 0:
            print("%d is not prime" % x)
            if x % 2 == 0:
                print("%d is even" % x)
            else:
                print("%d is odd" % x)
            break
    else:
        print("%d is prime" % x)
        if x % 2 == 0:
            print("%d is even" % x)
        else:
            print("%d is odd" % x)

#**WAP to check whether a enter character is vowel or consonant using if else statement
x = input("Enter a character: ").lower()
if x in 'aeiou':
    print("%s is a vowel" % x)
else:
    print("%s is a consonant" % x)

#**WAP to check whether a enter character is vowel, consonant or not an alphabet using if elif else statement
x = input("Enter a character: ").lower()
if x in 'aeiou':
    print("%s is a vowel" % x)
elif x in 'bcdfghjklmnpqrstvwxyz':
    print("%s is a consonant" % x)
else:
    print("%s is not an alphabet" % x)

# #**WAP to check whether a enter character is vowel, consonant , symbol or not using if elif else statement
x = input("Enter a character: ").lower()
if x in 'aeiou':
    print("%s is a vowel" % x)
elif x in 'bcdfghjklmnpqrstvwxyz':
    print("%s is a consonant" % x)
elif not x.isalpha():
    print("%s is a symbol" % x)
else:
    print("%s is an alphabet" % x)


# **nested if else statement
x = int(input("Enter a number: "))
if x > 0:
    if x % 2 == 0:
        print("%d is positive and even" % x)
    else:
        print("%d is positive and odd" % x)
elif x < 0:
    if x % 2 == 0:
        print("%d is negative and even" % x)
    else:
        print("%d is negative and odd" % x)


#**WAP to check greatest of three numbers using nested if else statement
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b:
    if a > c:
        print("%d is greatest" % a)
    else:
        print("%d is greatest" % c)
elif b > c:
    print("%d is greatest" % b)
else:
    print("%d is greatest" % c)


# **OR

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if(a > b and a > c):
    print("%d is greatest" % a)
elif(b > a and b > c):
    print("%d is greatest" % b)
else:
    print("%d is greatest" % c)



# **match case statement
x = int(input("Enter a number: "))
match x:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Not One, Two or Three")

# add, subtract, multiply, divide
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

ch = int(input("Enter: \n1 for add, \n2 for subtract, \n3 for multiply, \n4 for divide: "))
match ch:
    case 1:
        print("Addition of", num1, "and", num2, "is:", num1 + num2)
    case 2:
        print("Subtraction of", num1, "and", num2, "is:", num1 - num2)
    case 3:
        print("Multiplication of", num1, "and", num2, "is:", num1 * num2)
    case 4:
        print("Division of", num1, "and", num2, "is:", num1 / num2)
    case _:
        print("Invalid choice")

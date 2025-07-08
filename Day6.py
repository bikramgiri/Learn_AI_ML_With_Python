#Day6: Looping or iterative statements: For Loops, While Loops, do while Loops

# **For Loops: It is used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or other iterable objects.
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# **my_list = range(starting value, ending value, increase step value(gap between two numbers))
my_list = list(range(1, 11))
print(my_list)

my_list = list(range(1, 11, 4))
print(my_list)


# **i need to print the numbers from 1 to 20
# print in list format
for i in range(1, 21):
    print(i)

#print in row format
for i in range(1, 21):
    print(i, end=' ')

# print odd numbers from 1 to 20
for i in range(1, 21, 2):
    print(i, end=' ')
    
# print even numbers from 1 to 20
for i in range(0, 21, 2):
    print(i, end=' ')
    
    
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    
my_dic = {
      "1": "apple",
      "2": "banana",
      "3": "cherry"
}   

for key, value in my_dic.items():
    print(key, ':', value)
# **OR
for k in my_dic:
    print(f"{k} : {my_dic[k]}")


fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
for i in range(len(fruits)):
    print(f"{i} : {fruits[i]}")
# **OR
count = 0
for fruit in fruits:
    print(f"{count} : {fruit}")
    count += 1



# **While Loops: It is used to execute a block of code repeatedly as long as a given condition is true.
i = 1
while i <= 10:
    print(i, end=' ')
    i += 1


# **do while Loops: Python does not have a built-in do-while loop, but you can simulate it using a while loop with a break statement.
i = 1
while True:
    print(i, end=' ')
    i += 1
    if i > 10:
        break

# **break:It is used to exit the loop prematurely.
for i in range(1, 10):
     if i == 6:
         break
     print(i, end=' ')


# **continue: It is used to skip the current iteration and continue with the next iteration of the loop.
for i in range(1, 10):
    if i == 5:
        continue
    print(i, end=' ')



for i in range(1,16):
       if (i==5) or (i==6) or (i==7):
           continue
       print(i, end=' ')

for i in range(1,16):
       if i in [5,6,7]:
           continue
       print(i, end=' ')

# **print skip value also:
for i in range(1,16):
       if i in [5,6,7]:
           print(f"Skipping {i}", end=' ')
       else:
           print(i, end=' ')

# **OR

count = 0
skipValue = 0
while count < 10:
    count += 1
    if count == 5:
        skipValue= 5
        continue 
    print(count)  
print(f"Skipped value: {skipValue}")

# **OR

skipped = []
for i in range(1, 16):
    if i in [5, 6, 7]:
        skipped.append(i)
        continue
    print(i, end=' ')
print(f"\nSkipped values: {skipped}")

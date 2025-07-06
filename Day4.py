#**Day4: Data structure: Lists, tuples, sets, dictionaries

#**Lists: Mutable data structure
#**tuples: Immutable data structure
#**sets: Unordered collection of unique elements
#**dictionaries: Key-value pairs, mutable, and unordered collection of items

# Example of a dictionaries:
# "name": "John Doe"
# "phone_number": "123-456-7890"

# **Lists: Mutable(changable initial assigned list) data structure
my_list = [1, 2, 3, 4, "Hello",True, 3.14]
empty_list = []

l1 = [0, 2, "Samip",'Hello', 3.14, True, 1.78, "HI", 7.90]
print(l1)
print(type(l1))

el = []
print(el)
print(type(el))

# *Indexing in lists:
"""
If we have n element in a list:
the range of index will be from 0 to n-1
"""
l2 = ["Samriddha", "Ram", 32, 45.67, True]
print(l2[0]) 
print(type(l2[0])) 

print(l2[-1])  
print(type(l2[-1]))  

print(l2[-5])

# *List comprehension: It is 
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sq_x = [a ** 2 for a in x]
print(x)
print(sq_x)

l3 = [0, 2, "Samip",'Hello', 3.14, True, "Ram", 1.78, "HI", 7.90, False, 5, 'Gita', 44, 67.89, "Tina", 'Apple', 3]
'''
the last element
the second last element
the fifth element
'''
print(l3[-1])
print(l3[-2])
print(l3[4])

# *Slicing in list:
# list[starting_index: ending_index]

print(l3[0:5])  # from index 0 to index 4
print(l3[5:])   # from index 5 to the end of the list
print(l3[:7])   # from the start of the list to index 6
print(l3[-2:])  # from the second last element to the end of the list
print(l3[:])  # the whole list

print(list(reversed(l3)))  #  reversing the list

# *append:
l3.append("Element")
print(l3)

# *insert:(2, "Inserted"): (index, value)
l3.insert(2, "Inserted")
print(l3)

# *remove: removes the first occurrence of the value
l3.remove("Inserted")  # removes the first occurrence of the value
print(l3)

#* Sorting:
my_list = [33,4, 4.5, 78, 0, 33, 91, 3, 2, 1, 0.5, 0.1, 0.01]
print(my_list)
my_list.sort()
print(my_list)

# *reverse:
my_list.reverse()
print(my_list)


#* pop: removes the last element of the list and returns it
print(my_list.pop())  # removes the last element of the list and returns it
print(my_list)

# *remove: removes the first occurrence of the value
l3.insert(2, "Ram")
print(l3)
l3.remove("Ram")  # removes the first occurrence of the value
print(l3)

# *count: counts the number of occurrences of the value
# *index: returns the index of the first occurrence of the value
print(l3.count("Samip"))  # counts the number of occurrences of the value "Samip" in the list
print(l3.index("Samip"))  # returns the index of the first occurrence of the

# *clear(): removes all the elements of the list
print(l3)
l3.clear()  # removes all the elements of the list
print(l3)


# **tuples: Immutable(no change initial assigned tuples) data structure, indexing and slicing same as lists
my_tuple = (1, 2, 3, 4, "Hello", True,3, 3.14)
empty_tuple = ()      
print(my_tuple)
print(type(my_tuple))
print(empty_tuple)
print(type(empty_tuple))

count = my_tuple.count(1)    # counts the number of occurrences of the value 1 in the tuple
print(count) # output : 2 (1, True(True = 1))

# *Indexing in tuples: # returns the index of the first occurrence of the value in the tuple
index3 = my_tuple.index(3)  # returns the index of the first occurrence of the value 3 in the tuple
print(index3)  

#**Important note:
my_tuple = (2)
print(type(my_tuple))  # output: <class 'int'>, because it is not a tuple, it is an integer

my_tuple = (2,)
print(type(my_tuple))  # output: <class 'tuple'>, because it is a tuple with one element

tuple1 = 1, 5, 7
print(tuple1)  # output: (1, 5, 7), because it is a tuple with three elements
print(type(tuple1))  # output: <class 'tuple'>, because it is a tuple with three elements

#sets: Unordered collection of unique elements, donot store duplicate elements
my_set = {1, 4, 2, 3, 5, -4, -2, -1}
my_set.add(-6)
print(my_set)
print(type(my_set))

my_set.add(8)
print(my_set) 

my_set.add(5)
print(my_set)  # 5 will not be added again, because sets do not allow duplicate elements

my_set.add(-1)
print(my_set)  # adds the element -1 to the set

my_set.remove(2)
print(my_set)  # removes the element 2 from the set

my_set = set()
print(my_set)  # creates an empty set
print(type(my_set))  # output: <class 'set'>, because it is a set




#** dictionaries: Key-value pairs, mutable, and unordered collection of items
'''
my_dict = {
      "key1": "value1",
      "key2": "value2",
      "key3": "value3"
      ...............
      ...............
      "keyN": "valueN"
}
key must be unique and immutabel(unchangeable) data type
'''
my_dict = {
    "name": "John",
    "phone_number": "123-456-7890",
    "age": 30,
    "is_student": False
}

print(my_dict)
print(type(my_dict))  # output: <class 'dict'>, because it is

# **the remaining  functions of dict and how to delete a particular key value pair:

# Functions of dictionary:
my_dict["name"] = "John"  # adds a new key-value pair to
#the dictionary or updates the value of the key if it already exists
print(my_dict)  
my_dict["age"] = 31  # updates the value of the key "age
print(my_dict)  
my_dict["phone_number"] = "123-456-7890"  # updates the value of the key "phone_number"
print(my_dict)  
my_dict["is_student"] = False  # updates the value of the key "is_student"
print(my_dict)  
my_dict["new_key"] = "new_value"  # adds a new key-value pair to the dictionary
print(my_dict)  
my_dict["new_key"] = "new_value"  # adds a new key-value pair to the dictionary
print(my_dict)  
my_dict["new_key"] = "new_value"  # adds a new key-value pair to the dictionary
print(my_dict)  
my_dict["new_key"] = "new_value"  # adds a new key-value pair to the dictionary
print(my_dict)  
'123-456-7890', 'age': 31; 'is_student': False; 'new_key': 'new_value';
my_dict["new_key"] = "new_value"  # adds a new key-value pair to the dictionary
print(my_dict)  


del my_dict["age"]  # deletes the key-value pair with key "age"
# print(my_dict)   '123-456-7890', 'is_student': False
print(my_dict["name"])  

print(my_dict.get("phone_number"))  
print(my_dict.keys())  
print(my_dict.values())  
print(my_dict.items())  
('phone_number', '123-456-7890'), ('is_student', False)
my_dict.clear()  # removes all the key-value pairs in the dictionary
print(my_dict) 
my_dict.update({"city": "New York"})  # adds a new key-value pair to the dictionary
print(my_dict)  
my_dict.pop("name")  # removes the key-value pair with key "name" and returns its value
print(my_dict)  
my_dict.popitem()  # removes the last inserted key-value pair and returns it
print(my_dict)  
my_dict.setdefault("country", "USA")  # adds a new key-value pair to the dictionary if the key does not already exist
print(my_dict)  
my_dict.setdefault("phone_number", "987-654-3210")  # does not add a new key-value pair, because the key "phone_number" already exists
print(my_dict)  
my_dict.pop("phone_number")  # removes the key-value pair with key "phone_number" and returns its value
print(my_dict)  
my_dict.popitem()  # removes the last inserted key-value pair and returns it
print(my_dict)  
my_dict.clear()  # removes all the key-value pairs in the dictionary
print(my_dict)  
my_dict.update({"name": "John", "phone_number": "123-456-7890"})  # adds new key-value pairs to the dictionary
print(my_dict)  

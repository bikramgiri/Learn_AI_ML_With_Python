# Day3: Data Cleaning: split(), title(), capitalize()

# ** split(): # Splits the string into a list of substrings based on whitespace by default.
# ** title(): # Converts the first character of each word to uppercase and the rest to lowercase.
# ** capitalize(): # Converts the first character of the string to uppercase and the rest to lowercase.


# ** title(): # Converts the first character of each word to uppercase and the rest to lowercase.
name = "   ---sujata @@ pathak  1 2 3  __  "
# Goal = "Sujata Pathak"
new_name = name.strip(" -123_ ").replace(" @@ ", " ").title()
print(new_name)

# ** split(): # Splits the string into a list of substrings based on whitespace by default.
# first_name = Sujata and Last_name = Pathak
first_name, last_name = new_name.split()
print(f"First Name: {first_name}, Last Name: {last_name}")

name = "Ram Baidya Karki"
first_name, middle_name, last_name = name.split()
print(f"First Name: {first_name}, Middle Name: {middle_name}, Last Name: {last_name}")

# ** capitalize(): # Converts the first character of the string to uppercase and the rest to lowercase.
name = "samriddha pathak"
new_name = name.capitalize()
print(new_name)

name = "  __-- firoj ##&& karki 123 @@"
#Goal: first_name = "Firoj"
#      last_name = "Karki"
new_name = name.strip(" _-123 @@ ").replace(" ##&& ", " ").title()
print(new_name)
first_name, last_name = new_name.split()
# print(f"first_name = {first_name}, last_name = {last_name}")
# **OR
print(first_name)
print(last_name)

name = "  __--&*) firoj ##&& karki 123 @@("
#Goal: first_name = "Firoj"
#      last_name = "karki"
new_name = name.strip(" _-&*)123 @@(").replace(" ##&& ", " ").capitalize()
print(new_name)
first_name, last_name = new_name.split()
print(f"first_name = {first_name}\nlast_name = {last_name}")

ph_no = "(+977)9842655074"
new_ph_no = ph_no.replace("(+977)", '')
print(new_ph_no)
new_ph_no2 = "(+977)" + new_ph_no
print(new_ph_no2)

text = " $$ Samip ** % (+977)9702187444"
#Goal: first_name = Samip
#      ph_no = 9702187444
new_text = text.lstrip(" $$ ").replace(" ** % (+977)", " ")
print(new_text)
first_name, ph_no = new_text.split()
print(f"first_name: {first_name}\nnew_ph_no: {ph_no}")
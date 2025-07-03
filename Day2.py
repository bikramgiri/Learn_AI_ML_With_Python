# Day2: Data Cleaning(lstrip, rstrip, strip, replace)

name = "      Samriddha"
new_name = name.lstrip()
print(new_name)

name = "Samriddha        "
new_name = name.rstrip()
print(new_name)

name = "   Samriddha  "
new_name = name.lstrip().rstrip()
print(new_name)

name = "   Samriddha  "
new_name = name.strip()
print(new_name)

name = "Saroj ** Adhikari"
new_name = name.replace(" ** ", " ")
print(new_name)

name = "__Samriddha"
new_name = name.lstrip("__")
print(new_name)

name = "Samriddha__"
new_name = name.rstrip("__")
print(new_name)

name = "Samriddha__"
new_name = name.replace("__", "")
print(new_name)

name = "--Samriddha__"
new_name = name.lstrip("--").rstrip("__")
print(new_name)

name = "  Samriddha  "
new_name = name.strip()
print(new_name)

name = "1Samriddha2"
new_name = name.strip("21")
print(new_name)  


name = "   ---My --- Sister's name is sujata 1 2 3  __  "
Goal: name = "My Sister's name is sujata"

name = "   ---My --- Sister's name is sujata 1 2 3  __  "
new_name = name.strip(" -123_").replace(" --- ", " ")
print(new_name) 


name = "@! He %  -- is my @! &&  @ --friend !@#  "
new_name = name.strip("@!!@# ").replace(" %  -- ", " ").replace(" @! &&  @ --", " ")
print(new_name)

name = "--- My name ___ is Ram 123 Karki --"
new_name = name.strip("-  -").replace(" ___ ", " ").replace(" 123 ", " ")
print(new_name)


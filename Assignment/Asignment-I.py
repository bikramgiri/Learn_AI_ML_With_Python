# **Easy
# 1. Remove Spaces 
# Assignment: Remove leading and trailing spaces from a string using strip().

text = "  Jay Nepal  "
cleaned_text = text.strip()
# print(cleaned_text)


# 2. Remove Leading Characters 
# Assignment: Remove all leading asterisks from a string using lstrip().

text = "****Artificial Intelligence"
cleaned_text = text.lstrip("*")
# print(cleaned_text)


# 3. Remove Trailing Characters 
# Assignment: Remove all trailing exclamation marks from a string using rstrip(). 

text = "Be honest!!!!"
cleaned_text = text.rstrip("!")
# print(cleaned_text)


# 4. Capitalize a Sentence 
# Assignment: Capitalize only the first letter of a lowercase sentence using capitalize().

sentence = "artificial intelligence is the future."
cleaned_text = sentence.capitalize()
# print(cleaned_text)


# 5. Title Case a Name 
# Assignment: Convert a name to title case using title().

sentence = "discipline is the key to success"
cleaned_text = sentence.title()
print(cleaned_text)


# 6. Clean List of Names 
# Assignment: Remove leading and trailing spaces from each name in a list.

names = ["  Elephant  ", "  Tiger  ", "  Cow  ", "  Dog  ", "  Monkey  "]
cleaned_names = [name.strip() for name in names]
# print(cleaned_names)


# 7. Remove Custom Characters 
# Assignment: Remove # and $ from both ends of a string using strip().

text = "##Python Programming$$$"
cleaned_text = text.strip("#$")
# print(cleaned_text)


# 8. Capitalize All Names in List 
# Assignment: Capitalize each name in a list using capitalize().

names = ["elephant", "tiger", "cow", "dog", "monkey"]
capitalized_names = [name.capitalize() for name in names]
# print(capitalized_names)


# 9.Clean Dictionary Values 
# Assignment: Remove trailing spaces from all values in a dictionary.

data = {
    "name": "  Bidhan Karki   ",
    "age": "  28   ",
    "city": "  Dharan   "
}
cleaned_data = {key: value.strip() for key, value in data.items()}
# print(cleaned_data)


# 10. Title Case Sentences in List 
# Assignment: Convert each sentence in a list to title case.

sentences = ["artificial intelligence is the future.", "machine learning is a subset of AI.",
             "natural language processing enables communication."]
title_cased_sentences = [sentence.title() for sentence in sentences]
# print(title_cased_sentences)



# **Intermediate 
# 11. Clean and Title Case 
# Assignment: Remove spaces and convert to title case.

sentences = "  Ram is a good boy.  "
cleaned_sentences = sentences.strip().title()
# print(cleaned_sentences)

# 12. Clean List of Emails 
# Assignment: Remove leading/trailing spaces from each email in a list.

emails = ["  ram@example.com  ", "  shyam@example.com  ", "  sita@example.com  "]
cleaned_emails = [email.strip() for email in emails]
# print(cleaned_emails)

# 13. Remove Leading Numbers 
# Assignment: Remove all leading digits from a string using lstrip(). 

text = "09265Hello World!"
cleaned_text = text.lstrip("09265")
# print(cleaned_text)


# 14. Clean Nested List 
# Assignment: Remove spaces from each string in a nested list. 

nested_list = [["  Ram  ", "  Shyam  "], ["  Sita  "], ["  Kiran  ", "  Himal  "]]
cleaned_nested_list = [[name.strip() for name in sublist] for sublist in nested_list]
# print(cleaned_nested_list)


# 15. Capitalize After Cleaning 
# Assignment: Clean a string and capitalize the first letter.

sentence = "-& he *97is a && doctor. __%  "
cleaned_sentence = sentence.strip("-& _%  ").replace(" *97", " ").replace(" && ", " ").capitalize()
# print(cleaned_sentence)


# 16. Clean Dictionary Keys 
# Assignment: Remove trailing underscores from all dictionary keys.

data = {
    "name_": "  Bidhan Karki   ",
    "age_": "  28   ",
    "city_": "  Dharan   "
}
cleaned_data = {key.rstrip("_"): value.strip() for key, value in data.items()}
# print(cleaned_data)


# 17. Clean and Deduplicate Names 
# Assignment: Clean, capitalize, and deduplicate names in a list.

planets = ["  Mercury  ", "  venus ", "  MERCURY", "Venus  "]
cleaned_planets = list(set(planet.strip().capitalize() for planet in planets))
# print(cleaned_planets)


# 18. Remove Multiple Characters 
# Assignment: Remove *, -, and spaces from both ends of a string.

text = "--*Python Programming**--  "
cleaned_text = text.strip("*-  ")
# print(cleaned_text)


# 19. Conditional Cleaning in List 
# Assignment: Remove leading # only if present in each string in a list.

birds = ["Peacock", "#Crow", "#Parrot", "Eagle"]
cleaned_birds = [bird.lstrip("#") for bird in birds]
# print(cleaned_birds)


# 20. Clean and Group by First Letter 
# Assignment: Clean and group product names by their first letter (case-insensitive).

names = ["  Ram  ", "  binod  ", "  Ramesh  ", "  Kamal  ", "  Bishal  ", " Manish"]
cleaned_names = [name.strip().capitalize() for name in names]
grouped_names = {}
for name in cleaned_names:
    first_letter = name[0] 
    if first_letter not in grouped_names:
        grouped_names[first_letter] = []
    grouped_names[first_letter].append(name)
# print(grouped_names)


# Hard 
# 21. Clean Set of Strings 
# Assignment: Clean all strings in a set of special-character-laden strings. 

vegetables = {" --@Tomato  !", "  #&potato__  ", "$carrot  ", "  %Cabbage(*)"}
cleaned_vegetables = {veg.strip(" -@ !  #&_  $    %(*)").capitalize() for veg in vegetables}
# print(cleaned_vegetables)


# 22. Complex Nested Cleaning 
# Assignment: Clean and title-case all strings in dictionary values (lists).

data = {
    "birds": ["  &**peacock  ", "Crow^^  ", " parrot89  "],
    "animals": ["  __Elephant#@  ", "  tiger12", "44Lion  "],
}
cleaned_data = {key: [value.strip("  &**  ^^   89    _#@    1244  ").title() for value in values] 
                for key, values in data.items()}
# print(cleaned_data)


# 23. Custom Title Function 
# Assignment: Implement your own title() using only capitalize() and loops.

def title(t):
      return ' '.join(word.capitalize() for word in t.split())
text = "hello world, this is a test."
title_cased_text = title(text)
# print(title_cased_text)


# 24. Clean and Format Emails 
# Assignment: Clean emails (strip spaces, lowercase all, except capitalize first letter before @).

emails = ["  ram@example.com  ", "  shyam@example.com  ", "  sita@example.com  "]
cleaned_emails = []
for email in emails:
    email = email.strip().lower() 
    local_part, domain = email.split("@") 
    local_part = local_part.capitalize()
    cleaned_emails.append(f"{local_part}@{domain}")
# print(cleaned_emails)


# 25. Multi-Step Cleaning 
# Assignment: Remove leading numbers, trailing punctuation, and title-case the string.

text = " 8346Good Evening !!!"
cleaned_text = text.lstrip(" 8346").rstrip(" !!!").title()
# print(cleaned_text)


# 26. In-Place Cleaning 
# Assignment: Clean and title-case a list of strings in place (no new list).

fruits = ["MANGO#$  ", "  45Orange --", " banana$# "]
for i in range(len(fruits)):
    fruits[i] = fruits[i].strip("#$    45 - $# ").title()
# print(fruits)


# 27. Clean and Count Unique Words 
# Assignment: Clean sentences, split into words, count unique words.

sentences = [" 88Good Morning  ", "good afternon! --%  ", "  @good Evening (*)_"]
cleaned_sentences = [sentence.strip(" 88   --%    @  (*)_").title() for sentence in sentences]
unique_words = set(word for sentence in cleaned_sentences for word in sentence.split())
# print(unique_words)


# 28. Clean Dictionary Sentences 
# Assignment: Clean and capitalize only the first word of each dictionary value.

data = {
      "s1": "  --hello world! 99",
      "s2": "##ai is amazing.__",
      "s3": "  77ai and ML are the future.  **"
      }
cleaned_data = {key: value.strip("  -- 99##__  77  **").capitalize() for key, value in data.items()}
# print(cleaned_data)


# 29. Selective Character Removal 
# Assignment: Remove only leading/trailing underscores and dashes.

text = "--__Python Programming__--"
cleaned_text = text.strip("-_")
# print(cleaned_text)


# 30. Batch Clean and Sort 
# Assignment: Clean and title-case product codes, then sort.

product_codes = ["**pROD123  ", "  --88prod456--  ", "  0-0PROD789 --__  ", " PROD999 (&)"]
cleaned_product_codes = [code.strip("**    --88--    0-0  --__    (&)").title() for code in product_codes]
cleaned_product_codes.sort()
# print(cleaned_product_codes)
"""
In Python, a dictionary (often abbreviated as "dict") is a built-in data type used to store collections of key-value pairs. It is an unordered collection of items, and each item consists of a key and its associated value. Dictionaries are also known as associative arrays or hash maps in other programming languages."""


# Creating a Dictionary:

# You can create a dictionary by enclosing a comma-separated list of key-value pairs within curly braces {}. The key and its associated value are separated by a colon :. For 


my_dict = {
    "name": "Ruchika",
    "age": 22,
    "city": "Mumbai"
}

# Accessing Values:
# print(my_dict["name"])


# If the key doesn't exist in the dictionary, it will raise a KeyError. To avoid this, you can use the get() method:

# print(my_dict.get("city"))  

# Adding or Updating Items:

# my_dict["job"] = "Teacher"  # Adding a new key-value pair
# my_dict["age"] = 23  # Updating the value of an existing key

# print(my_dict)

# Removing Items:

# To remove a key-value pair from a dictionary, you can use the del statement or the pop() method:

# del my_dict["city"]  # Removing a key-value pair
# my_dict.pop("age")   # Removing a key-value pair using pop()

# print(my_dict)


#  dict in loop

# for i in my_dict:
#     print(i, my_dict[i])

# # Or using the items() method
# for key, value in my_dict.items():
#     print(key, value)




# You can use the in keyword to check if a key exists in a dictionary:
if "name" in my_dict:
    print("Name:", my_dict["name"])
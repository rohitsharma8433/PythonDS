"""In Python, a tuple is a collection data type that is similar to a list but with some key differences. Tuples are used to store an ordered sequence of elements, just like lists, but unlike lists, tuples are immutable. This means that once you create a tuple, you cannot modify its elements (add, remove, or change them). Tuples are defined using parentheses ()."""

# Creating a Tuple:

# my_tuple=(101,102,103,104)

# Accessing Elements:

# print(my_tuple[2])
# print(my_tuple[1])


# slicing
# You can also slice a tuple to get a subset of its elements.

# print(my_tuple[1:3])

# Tuple packing is when you create a tuple by assigning values to it, and tuple unpacking is when you assign the values of a tuple to variables.

# Tuple packing
# my_tuple = (1, 2, 3)

# Tuple unpacking
# (a, b, c) = my_tuple
# print(a)  # Output: 1
# print(b)  # Output: 2
# print(c)  # Output: 3



# Immutability:
# As mentioned earlier, tuples are immutable, so you cannot change their elements once they are created. This is in contrast to lists, which are mutable.

# my_tuple[0] = 110 
# print(my_tuple)


# Tuple Methods:
# Tuples have a few methods, such as count() and index(), which can be used to count the occurrences of a value and find the index of a value, respectively.

# python

my_tuple = (101, 102,102, 103, 104, 102)

count = my_tuple.count(102)  # Count occurrences of 102 (count = 3)
index = my_tuple.index(103)  # Find the index of 3 (index = 3)
print(count)
print(index)
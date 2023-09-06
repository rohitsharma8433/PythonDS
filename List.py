"""In Python, a list is a built-in data type used to store collections of items. Lists are ordered, mutable (you can change their elements), and can contain elements of different data types. Here's how you can create and work with lists in Python, along with some examples:"""

# Createing  the list 

List=["Ayush","Ruchika","Hrutika","Rohit","Raj","Rohini","Mohini"]

# print(List)

# Accessing List Elements:
# You can access individual elements in a list using indexing. Indexing starts at 0.

# print(List[0])
# print(List[3])
#print(List[-1]) # we can also do negetive indexing 

# You can extract a portion of a list using slicing. Slicing allows you to specify a range of indices.
 
#print(List[1:3])    # Creates a new list ["Ruchika","Hrutika"]

#print(List[0::2]) # it return the value by leaving two step ['Ayush', 'Hrutika', 'Raj', 'Mohini']



#Update Lists using indexing :

# List[3]="Santosh"
# print(List)


#Adding Elements it Add the value in End of the list :

# List.append("Rohit")
# print(List)


#List.insert(0, "Mohak")  # Insert 4 at index 1

# Removing Elements:

# print(List.remove("Rohit")) #parameter as  value 

# print(List.pop(2)) # parameter as index value 

# print(List)


# List Length:
# You can get the length of a list using the len() function.

# print(len(List))


# print  loop through list 

# for item in List:
#     print(item)
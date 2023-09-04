
'''A 2D array, also known as a two-dimensional array, is a data structure that stores elements in a grid or matrix-like fashion with rows and columns. It can be thought of as an array of arrays, where each element in the array is itself an array. In programming, 2D arrays are often used to represent tables, matrices, or grids of data.'''

# from array import *
# Array = [[1,2,3],
#         [4,5,6],
#         [7,8,9]]



#  printing the array using loop
# for i in Array:
#     for n in i:
#         print(n,end=" ")
#     print("\r")


#  Access Array Element 

# print(Array[1][1])

# print(Array[0][1])


#  Update the array item

# Array[0][2]="10"

#  printing the array using loop after updation Element
# for i in Array:
#     for n in i:
#         print(n,end=" ")
#     print("\r")

#  User input in 2d Array

# Ask the user for the dimensions of the 2D array (rows and columns)
row = int(input("Enter the number of rows : "))
col = int(input("Enter the number of columns : "))

print("Enter the",row*col," Element in the matrix ")
# take Empty Array
matrix = []

# take a loop to fill the Array
for i in range(row):
    row = []  # Create an empty row 
    for j in range(col):
        ele = int(input(f"Enter element at row {i + 1}, column {j + 1}: "))
        row.append(ele)  
    matrix.append(row)  

# Print the 2D array
for data in matrix:
    print(data)



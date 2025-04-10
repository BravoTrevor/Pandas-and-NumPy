'''The code below initializes a Python list named list1:'''
import numpy as np
import pandas as pd

list1 = [1,2,3,4]

'''To convert this to a one-dimensional ndarray with one row and four columns, we can use the np.array() 
function:'''

array1 = np.array(list1)
print(array1)

'''Output:
[1 2 3 4]

To get a two-dimensional ndarray from a list, we must start with a Python list of lists:'''

list2 = [[1,2,3],[4,5,6]]
array2 = np.array(list2)
print(array2)

'''Output:
[[1 2 3]
 [4 5 6]]

Say you own a toy store and decide to decrease the price of all toys by €2 for a weekend sale. With the toy 
prices stored in an ndarray, you can easily facilitate this operation.'''

toyPrices = np.array([5,8,3,6])
print(toyPrices - 2)

'''Output:
[3 6 1 4]

If, however, you had stored your toy prices in a Python list, you would have to manually loop through the 
entire list to decrease each toy price.'''

toyPrices = [5,8,3,6]
# print(toyPrices - 2) -- Not possible. Causes an error
for i in range(len(toyPrices)):
    toyPrices[i] -= 2
print(toyPrices)

'''Output:
[3,6,1,4]'''

# Create a Series using a NumPy array of ages with the default numerical indices
ages = np.array([13,25,19])
series1 = pd.Series(ages)
print(series1)

'''Output:
0  |  13
1  |  25
2  |  19
dtype: int64

When printing a Series, the data type of its elements is also printed. To customize the indices of a Series 
object, use the index argument of the Series constructor.'''

'''Create a Series using a NumPy array of ages but customize the indices to be the names that correspond to 
each age'''

ages = np.array([13,25,19])
series1 = pd.Series(ages,index=['Emma', 'Swetha', 'Serajh'])
print(series1)

'''Output:
Emma    |  13
Swetha  |  25
Serajh  |  19
dtype: int64

Series objects provide more information than NumPy arrays do. Printing a NumPy array of ages does not print 
the indices or allow us to customize them.'''

ages = np.array([13,25,19])
print(ages)

'''Output:
[13 25 19]

Each nested list represents the data in one row of the DataFrame. We use the keyword columns to pass in the 
list of our custom column names.'''

dataf = pd.DataFrame([
    ['John Smith','123 Main St',34],
    ['Jane Doe', '456 Maple Ave',28],
    ['Joe Schmo', '789 Broadway',51]
    ],
    columns=['name','address','age'])

'''This is how the DataFrame is displayed:
          name      |   address     |   age
0    | John Smith   | 123 Main St   |   34
1    | Jane Doe     | 456 Maple Ave |   28
2    | Joe Schmo    | 789 Broadway  |   51

The default row indices are 0,1,2..., but these can be changed. For example, they can be set to be the 
elements in one of the columns of the DataFrame. To use the names column as indices instead of the default 
numerical values, we can run the following command on our DataFrame:'''

dataf.set_index('name')

'''Output:
   name      |   address     |  age
John Smith   | 123 Main St   |   34
Jane Doe     | 456 Maple Ave |   28
Joe Schmo    | 789 Broadway  |   51
'''
# Creating a structured array with names and ages
data = np.array([("Alice", 25), ("Bob", 30), ("Charlie", 25)], dtype=[("name", "U10"), ("age", "i4")])

# Using numpy.lexsort to get indices that sort by age first, then by name
sorted_indices = np.lexsort((data["age"], data["name"]))

# Rearranging the original data based on the sorted indices
sorted_data = data[sorted_indices]

# Printing the sorted structured array
print(sorted_data)


'''Performing Basic Mathematical Operations with NumPy Arrays'''

# Creating two arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Adding the arrays
add = arr1 + arr2

print(add)

# Subtracting ‘arr2’ from ‘arr1’
sub = arr1 - arr2

print(sub)

# Multiplying the arrays
mul = arr1 * arr2

print(mul)

# Dividing ‘arr1’ by ‘arr2’
div = arr1 / arr2

print(div)

'''The above code produces the following output:
[5 7 9]
[-3 -3 -3]
[4 10 18]
[0.25 0.4 0.5]'''
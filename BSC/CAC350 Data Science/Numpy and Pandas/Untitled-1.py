# %%
# Dhruv Patel
# 10/29/2022
# Assignment #2
# CAC 350
import numpy as np
import random
# Prints 5 rows sliced in 7 colums arranging a random number with 1000 being the max and showcasing the array
np.arange(5) + np.arange(random.randint(1,100), 1000, random.randint(1,100)) [:7, np.newaxis]

# %%
# np.arrange returns values within a give interval as numpy.arange([start, ]stop, [step, ]dtype=None, *, like=None)
# np.newaxis adds a new dimension of size 1 at that position
arrange = np.arange(6)
print (arrange)
print(arrange[:,  np.newaxis])

# %%
# np.sort can use any sort quicksort, mergesort,stable,heapsort under the kind catogry labeling the sorting algoritum. numpy.sort(a, axis=-1, kind=None, order=None)
# The speed notation faries are quicksort uses a O(n^2) as the worst mergesort - O(n*log(n)) stable - O(n*log(n)) heapsort - O(n*log(n)). the Big O represent the speed of the execution within data structure and algoritums depending on the sort method.
sort = np.array([[1,4],[3,1]])
np.sort(sort)
np.sort(sort, axis=None)
#np.sort(sort, axis=0)

# %%
# Prints sorted array
array = [4,1,5,2,7,3]
np.sort(array)

# %%
# Sorts colums according to the first axis in order of first order.
columns = np.array([[1,3],[4,5],[3,2],[0,6]])
np.sort(columns, axis=1)   



# %%
# Sorts rows according to the 0 axis in order of the second order
rows = np.array([[1,3],[4,5],[3,2],[0,6]])
np.sort(rows, axis=0)

# %%
# Structured Array - It is used for grouping data of different arrays for types and sizes using data containers containing arrays of different data type.

# %%
#Import pandas and NumPy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Reads the file and prints the csv colums and info of the first 5 for carData1
carData1= pd.read_csv('cars1.csv')
carData1.head()



# %%
#Reads the file and prints the csv colums and info of the first 5 for carData2
carData2 = pd.read_csv('cars2.csv')
carData2.head()

# 9 each oberservation for each dataset

# %%
# Removes all unamed columns
carData1 = carData1.loc[:, ~carData1.columns.str.contains('^Unnamed')]
carData2 = carData2.loc[:, ~carData2.columns.str.contains('^Unnamed')]

# %%
# Merges the two data
#mergedCarData = pd.merge(carData1, carData2, on = 'mpg' , how = 'inner')
#mergedCarData = pd.concat(carData1, carData2, join = 'outer')
#print(mergedCarData)

frames = [carData1, carData2]
mergedCarData = pd.concat(frames)

# %%
# Show cases each colums merged
import random
mergedCarData.columns

# %%
owner = np.random.randint(15000,73000, 398)
mergedCarData["Owner"] = owner
mergedCarData.head()


# %%
carmpg = mergedCarData["mpg"]
carhorsepower = mergedCarData["displacement"]
minimum = min(carmpg)
maximum = max(carhorsepower)
carModel = pd.Series([0,8])

print("The lowest mpg car has a min mpg of", minimum )
print("The highest horesepower has a max power of", maximum)

# %%




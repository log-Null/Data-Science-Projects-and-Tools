# NumPy Practice – Arrays, Indexing, and Slicing

This notebook is a small NumPy practice exercise covering:
- Creating arrays
- Indexing and slicing
- Basic statistical operations like average and difference
- Observing real-world data with arrays

---

## 1. Rent Prices Example

We start with an array of rent prices and a list of programming languages.

```python
import numpy as np

# Rent prices
rent = np.array([1500, 1500, 1500, 1500, 1750, 1750])

# Languages
languages = np.array(['Python', 'Java', 'JavaScript', 'C++', 'Ruby'])

# Accessing the 3rd element
print("The 3rd language is:", languages[2])
```
## 2.NYC Population Over 10 Years

Every metro city's population keeps changing.
Here’s the NYC population from 2023 (top) to 2013 (bottom):

- 19571216
- 19673200
- 19854526
- 20104710
- 19463131
- 19544098
- 19593849
- 19636391
- 19657321
- 19653431
- 19626488

We’ll analyze this using a NumPy array:

```python
# NYC Population data (2023 → 2013)
population = np.array([
    19571216, 19673200, 19854526, 20104710, 19463131,
    19544098, 19593849, 19636391, 19657321, 19653431, 19626488
])

# First and last item
print("First item (2023):", population[0])
print("Last item (2013):", population[-1])

# Change in 10 years
difference = population[0] - population[-1]
print("Population change in 10 years:", difference)

# COVID years (2020–2022) → indexes 1:4
print("Population during 2020–2022:", population[1:4])
```
## 3. Personal Data Tracking Example

Think of something you track daily/weekly.
For example: hours of sleep each day this week.

```python
sleep=np.array([[6,6,7,5,6,7,9]
                ,[7,5,6,8,9,5,6],
                [8,9,5,6,7,8,5]])
print(sleep)
avg=np.average(sleep)
print(f'The average sleeping time is {round(avg)} hours')
```
## You can replace sleep_hours with other data such as:
Mood ratings per hour
Water glasses per day
Number of yawns, etc.

## 4. 1D vs 2D Arrays

1D Array: Works for tracking one type of data (like sleep hours).
2D Array: Useful if you track multiple things per day (e.g., sleep + water + mood).

## Key Numpy Concepts Covered
NumPy arrays are used to store large amounts of numbers.
An index is an element’s position in an array. NumPy arrays are 0-indexed.
Slicing is where we can access parts of a sequence with name[start:end].
2D arrays have 1D arrays as elements.

# This notebook serves as a hands-on guide for beginner -learning essential numpy operations and basic data manipulation techniques in Python. 
# Resources : [Numpy by Codedex](https://www.codedex.io/numpy)





  

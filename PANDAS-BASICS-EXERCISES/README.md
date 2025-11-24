# Pandas & DataFrames – Notebook Overview

This Jupyter Notebook demonstrates key **Pandas DataFrame operations** including creating, manipulating, and analyzing data, which I did as part of Codedex learning. .
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/9652e33c-1046-43e2-a4ef-38f3e77b459f" />


---

## Contents

### 1. Character DataFrames
- Subset characters based on **level, race, or class**.
- Examples include:
  - Characters above a certain level
  - Halfling Bards
  - Magic users (Wizard, Sorcerer, Warlock)

### 2. Custom DataFrame
- Create a **custom DataFrame** on a topic of your choice with at least 10 rows and 5 columns.
- Operations include:
  - Adding new columns
  - Sorting by a column
  - Filtering rows based on conditions

### 3. Apps DataFrame
  - Sorting apps by rating

---

## Key Pandas Concepts Covered

- **Creating DataFrames** from dictionaries or lists  
- **Exploring data** using `.head()`, `.tail()`, `.info()`, and `.describe()`  
- **Selecting columns** and **filtering rows** with boolean conditions  
- **Combining conditions** using AND (`&`) / OR (`|`)  
- **Sorting** and **renaming columns**  
- **Adding new columns** derived from existing data  

---

This notebook serves as a **hands-on guide** for learning essential Pandas operations and basic  data manipulation techniques in Python. Here's a recap of the main takeaways from this chapter:

DataFrames store data in rows and columns. They can be created from dictionaries, lists, or imported directly from files.
Some preliminary data exploration:
- .head() shows the first few rows of the DataFrame.
- .tail() shows the last few rows of the DataFrame.
- .info() displays column names, data types, etc.
- .describe() summarizes stats for numeric columns.
- Select specific columns from a DataFrame by using square brackets [ ].
- Filter rows of DataFrames by using boolean expressions using >, <, or ==. Chain multiple boolean expressions together using AND (&) and OR (|).
- We can sort, rename, and add new columns to a DataFrame.




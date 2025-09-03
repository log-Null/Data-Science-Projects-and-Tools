# Pandas Filtering Basics

This README summarizes **how to filter data in Pandas DataFrames**.

---

## 1. Single Condition
- Filter rows based on a single condition:  
`df[df['Column'] > value]`


---

## 2. Multiple Conditions
- Combine conditions using `&` (AND) and `|` (OR).  
- Wrap each condition in parentheses:  
`df[(cond1) & (cond2)]`
-.select() and .where()

---
Reference from [LEARN PYTHON FOR DATA SCIENCE BY FREECODECAMP](https://www.youtube.com/watch?v=CMEWVn1uZpQ&t=12s)


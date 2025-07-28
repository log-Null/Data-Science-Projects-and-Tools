#  CSV Data Cleaner.
A flexible and simple Python tool to clean messy CSV files. It handles missing values, removes duplicates, trims whitespaces, standardizes column formats, and validates email fields (if present).  
Just run it, input the path to your dataset, and it does the rest!. This is a lot helpful project for people who want to pursue data science.

---

## Features I have added includes:

- 🔁 Removes duplicate rows
- 🧹 Fills missing values (with mean for numbers, 'Unknown' for text)
- ✂️ Trims extra spaces in text columns
- 🧾 Renames columns to lowercase with underscores
- 📅 Standardizes date formats (e.g., for `date_of_birth`, `dob`)
- 📧 Validates emails (if a column named `email` exists)
- 📂 Saves a cleaned copy with a timestamp in the filename

---

## 📸 Sample Use Case: Exoplanet Dataset

If you have a dataset like this:

```csv
Planet Name, Discovery Method ,Year, Distance (ly), Email
Kepler-22b, Transit, 2009, 600, kepler@space.org
Kepler-22b, Transit, 2009, 600, kepler@space.org
Gliese 581g,,2010,,gliese@space

The tool will:
Remove the duplicate row
Fill the missing discovery method and distance
Standardize column names to: planet_name, discovery_method, year, distance_(ly), email
Add a column valid_email with True/False

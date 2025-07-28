import pandas as pd 
import os
import sys
import re
from datetime import datetime


def load_csv(file_path):
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        sys.exit(1)
    return pd.read_csv(file_path)


def clean_column_names(df):
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    return df


def remove_duplicates(df):
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    print(f" Removed {before - after} duplicate rows.")
    return df


def handle_missing_values(df):
    for col in df.columns:
        if df[col].dtype == 'O':  # Object = text
            df[col] = df[col].fillna("Unknown")
        else:
            df[col] = df[col].fillna(df[col].mean())
    print("🔄 Filled missing values (mean for numbers, 'Unknown' for text).")
    return df


def trim_whitespace(df):
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.strip()
    return df


def standardize_dates(df):
    date_cols = []
    for col in df.columns:
        if 'date' in col or 'dob' in col:
            try:
                df[col] = pd.to_datetime(df[col], errors='coerce')
                date_cols.append(col)
            except:
                pass
    if date_cols:
        print(f"📅 Standardized date columns: {', '.join(date_cols)}")
    return df


def validate_emails(df):
    if 'email' in df.columns:
        df['valid_email'] = df['email'].apply(
            lambda x: bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', str(x))) if pd.notnull(x) else False)
        print("📧 Email validation column added.")
    return df


def clean_csv(file_path, output_path):
    df = load_csv(file_path)
    df = clean_column_names(df)
    df = trim_whitespace(df)
    df = remove_duplicates(df)
    df = handle_missing_values(df)
    df = standardize_dates(df)
    df = validate_emails(df)
    df.to_csv(output_path, index=False)
    print(f"\n✅ Cleaned CSV saved to: {output_path}")


if __name__ == "__main__":
    print("📂 CSV Data Cleaner")
    input_csv = input("🔎 Enter the path to your CSV file (e.g., sample_data.csv): ").strip()

    if not os.path.exists(input_csv):
        print(f"❌ File not found: {input_csv}")
        sys.exit(1)

    now = datetime.now().strftime("%Y%m%d_%H%M")
    output_csv = f"cleaned_data_{now}.csv"

    clean_csv(input_csv, output_csv)




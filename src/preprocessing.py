import pandas as pd

def dataset_info(df):
    print("\n========== First 5 rows ==========")
    print(df.head())
    
    
    print("\n========== Last 5 Rows ==========")
    print(df.tail())
    
    
    print("\n======== Dataset info ========")
    print(df.info())
    
    
    print("\n======== Dataset Shape ========")
    print(df.shape)
    
    
    print("\n======== Columns ==========")
    print(df.columns)
    
    
    print("\n========== Data Type ==========")
    print(df.dtypes)
    
    
    print("\n========== Statastical Summery ==========")
    print(df.describe())
    
    
def check_missing_values(df):
    print("\n========== check Missing Values ==========")
    print(df.isnull().sum())
    
def check_duplicates(df):
    print("\n========== Duplicated Records ==========")
    print(df.duplicated().sum())
    
def remove_duplicates(df):
    print("\n========== Remove Duplicate Values ==========")
    df = df.drop_duplicates()
    return df

def save_clean_data(df):
    df.to_csv("data/employee_cleaned.csv",index = False)
    print("\nCleaned Dataset Saved Successfully...")
    
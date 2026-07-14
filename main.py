# import modules

import os
from src.load_data import load_data
from src.preprocessing import *
from src.analysis import *
from src.visualization import *
from src.report import generate_report

# create the required folder

os.makedirs("images",exist_ok=True)
os.makedirs("reports",exist_ok=True)


# load the dataset

print("\n" + "=" * 60)
print("Loading Dataset")
print("=" * 60)
df = load_data("data/employee_data.csv")

# Data Preprocessing

dataset_info(df)

check_missing_values(df)

check_duplicates(df)
df = remove_duplicates(df)

save_clean_data(df)

# Bussiness Analysis

print("\n" + "=" * 60)
print("BUSSINESS ANALYSYS")
print("=" * 60)

average_salary(df)

highest_salary(df)

lowest_salary(df)

department_salary(df)

city_salary(df)

gender_salary(df)

education_salary(df)

performance_count(df)

work_mode_count(df)

top_5_salary(df)

bottom_5_salary(df)

# Data Visualization

print("\n" + "=" * 60)
print("GENERATING VISUALIZATION")
print("=" * 60)

age_distribution(df)

salary_disribution(df)

department_count(df)

gender_count(df)

education_count(df)

work_mode_count(df)

performance_count(df)

salary_boxplot(df)

age_box_plot(df)

experience_vs_salary(df)

department_salary(df)

city_salary(df)

department_pie(df)


# Generate PDF Report

print("\n" + "=" * 60)
print("Generate PDF Report")
print("=" * 60)

generate_report(df)

# project Complted

print("\n" + "=" * 60)
print("Project Completed Successfully")
print("=" * 60)

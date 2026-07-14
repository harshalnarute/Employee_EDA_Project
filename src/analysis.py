def average_salary(df):
    print("\n========== Average Salary ==========")
    print(df['Salary'].mean())

def highest_salary(df):
    print("\n========== Highest Salary ==========")
    print(df['Salary'].max())
    
def lowest_salary(df):
    print("\n========== Lowest Salary ==========")
    print(df['Salary'].min())
    
def department_salary(df):
    print("\n========== Average Salary By Department ==========")
    print(df.groupby("Department")['Salary'].mean())
    
def city_salary(df):
    print("\n========== Average Salary By City ==========")
    print(df.groupby("City")['Salary'].mean())
    
def gender_salary(df):
    print("\n========== Average Salary by Gender ==========")
    print(df.groupby("Gender")['Salary'].mean())
    
def education_salary(df):
    print("\n========== Average Salary by Education ==========")
    print(df.groupby('Education')['Salary'].mean())

def performance_count(df):
    print("\n========== Performance Count ==========")
    print(df['Performance'].value_counts())
    
def work_mode_count(df):
    print("\n ========== Work Mode count ==========")
    print(df['Work_Mode'].value_counts())
    
def top_5_salary(df):
    print("\n========== Top 5 Salary ==========")
    print(df.nlargest(5,'Salary'))
    
def bottom_5_salary(df):
    print("\n========== Bottom 5 Salary ==========")
    print(df.nsmallest(5,'Salary'))
    

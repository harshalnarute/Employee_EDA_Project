import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create Image folder Automatically

os.makedirs('images',exist_ok= True)

def age_distribution(df):
    plt.figure(figsize=(8,5))
    sns.histplot(df['Age'],bins = 10,kde = True)
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.savefig("images/age_distribution.png")
    plt.show()
    
def salary_disribution(df):
    plt.figure(figsize= (8,5))
    sns.histplot(df['Salary'],bins = 10 , kde = True )
    plt.title("Salary Distribution")
    plt.xlabel("Salary")
    plt.ylabel("Count")
    plt.savefig("images/salary_distribution.png")
    plt.show()
    
def department_count(df):
    plt.figure(figsize=(8,5))
    sns.countplot(x = df['Department'],data = df)
    plt.title("Department Count")
    plt.xlabel("Department")
    plt.ylabel("Employees")
    plt.xticks(rotation = 45)
    plt.savefig("images/department_count.png")
    plt.show()
    
    
def gender_count(df):
    plt.figure(figsize=(6,5))
    sns.countplot(x = df['Gender'],data = df)
    plt.title("Gender Count")
    plt.xlabel("Gender")
    plt.ylabel("Count")
    plt.savefig("images/gender_distribution_count.png")
    plt.show()
    

def education_count(df):
    plt.figure(figsize=(8,5))
    sns.countplot(x = df['Education'],data = df)
    plt.title("Education Count")
    plt.xlabel("Education")
    plt.ylabel("Count")
    plt.savefig("images/education_distribution.png")
    plt.show()
    
def workmode_count(df):
    plt.figure(figsize=(8,5))
    sns.countplot(x = df['Work_Mode'],data = df)
    plt.title("Work Mode Distribution")
    plt.xlabel("Work Mode")
    plt.ylabel("Count")
    plt.savefig("images/workmode_distribution.png")
    plt.show()
    
def performance_count(df):
    plt.figure(figsize=(8,5))
    sns.countplot(x = df['Performance'],data = df)
    plt.title("Peroformance Distribution")
    plt.xlabel("Performance Rating")
    plt.ylabel("Count")
    plt.savefig("images/performanace_distribution.png")
    plt.show()
    
def salary_boxplot(df):
    plt.figure(figsize=(8,5))
    sns.boxplot(y = df['Salary'])
    plt.title("Salary Boxplot")
    plt.savefig("images/salary_boxplot.png")
    plt.show()
    
def age_box_plot(df):
    plt.figure(figsize=(8,5))
    sns.boxplot(y = df['Age'])
    plt.title("Age Boxplot")
    plt.savefig("images/age_boxplot.png")
    plt.show()
    
def experience_vs_salary(df):
    plt.figure(figsize=(8,5))
    sns.scatterplot(
        x = "Experience",
        y =  "Salary",
        hue = "Department",
        data = df
    )
    
    plt.title("Experience Vs Salary")
    plt.savefig("images/experience_salary.png")
    plt.show()
    

def department_salary(df):
    plt.figure(figsize=(8,5))
    sns.barplot(
        x = 'Department',
        y = 'Salary',
        data = df        
    )
    plt.title("Department Vs Salary")
    plt.xticks(rotation = 45)
    plt.savefig("images/department_salary.png")
    plt.show()
    
def city_salary(df):
    plt.figure(figsize=(8,5))
    sns.barplot(
        x = 'City',
        y = 'Salary',
        data = df
    )
    plt.title("city Vs salary")
    plt.xticks(rotation = 45)
    plt.savefig("images/city_salary.png")
    plt.show()
    
    
def department_pie(df):
    plt.figure(figsize=(7,7))
    df['Department'].value_counts().plot(
        kind = "pie",
        autopct = "%1.1f%%",
    )
    plt.title("Department_Distribution")
    plt.ylabel("")
    plt.savefig("images/Department_Pie.png")
    plt.show()
    
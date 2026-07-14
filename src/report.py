import os

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer
)

def generate_report(df):
    
    os.makedirs("reports",exist_ok=True)
    
    pdf = SimpleDocTemplate(
        "reports/Final_Report.pdf"
    )
    
    styles = getSampleStyleSheet()
    elements = []
    
# Title
    elements.append(
        Paragraph(
            "Employee Exploratory Data Analysis Report",
            styles['Title']
        )
    )
    elements.append(Spacer(1, 20))
    
# Dataset Summery
    elements.append(
        Paragraph(
            "<b>Dataset Summery</b>",
            styles['Heading2']
            
        )
    )
    elements.append(
        Paragraph(
            f"Total Employees : {len(df)}",
            styles['BodyText']
        )
    )
    elements.append(
        Paragraph(
            f"Total Columns :{len(df.columns)}",
            styles['BodyText']
        )
    )
    elements.append(
        Paragraph(
            f"Missing values:{df.isnull().sum()}",
            styles['BodyText']
        )
    )
    elements.append(Spacer(1,20))
    
# Salary Analysis

    elements.append(
        Paragraph(
            "<b>Salary Analysis</b>",
            styles['Heading2']
        )
    )
    elements.append(
        Paragraph(
            f"Average salary:Rs{df['Salary'].mean():.2f}",
            styles['BodyText']
        )
    )
    elements.append(
        Paragraph(
            f"Highest Salary :Rs.{df['Salary'].max():.2f}",
            styles['BodyText']
        )
    )
    elements.append(
        Paragraph(
            f"Lowest Salary :Rs.{df['Salary'].min():.2f}",
            styles['BodyText']
        )
    )
    elements.append(Spacer(1,20))

# Bissuness Insights

    elements.append(
        Paragraph(
            "<b>Bissuness Insights</b>",
            styles['Heading2']
        )
    )
    
    elements.append(
        Paragraph(
            f"Highest Paying Department:"
            f"{df.groupby('Department')['Salary'].mean().idxmax()}",
            styles['BodyText']
        )
    )
    
    elements.append(
        Paragraph(
            f"Highest Paying City:"
            f"{df.groupby('City')['Salary'].mean().idxmax()}",
            styles['BodyText']
        )
    )

# Work Mode

    elements.append(
        Paragraph(
            f"Most Common Work Mode :"
            f"{df['Work_Mode'].mode()[0]}",
            styles['BodyText']
        )
    )
    
    
# Higheest Perfromance Rating

    elements.append(
        Paragraph(
            f"Highest Performance Rating :"
            f"{df['Performance'].max()}",
            styles['BodyText']
        )
    )
    
# Most Common Education

    elements.append(
        Paragraph(
            f"Most Common Education :"
            f"{df['Education'].mode()[0]}",
            styles['BodyText']
        )
    )
    
    elements.append(Spacer(1,20))
    
# Recommandation

    elements.append(
        Paragraph(
            "<b>Recommandation</b>",
            styles['Heading2']
        )
    )
    
    elements.append(
        Paragraph(
            "1.Review Salary Structure Across Department.",
            styles['BodyText'] 
        )
    )
    
    elements.append(
        Paragraph(
            "2.Encuorage Employee Skill Development.",
            styles['BodyText']
        )
    )
    
    elements.append(
        Paragraph(
            "3.Improve Performance Evaluation Process.",
            styles['BodyText']
        )
    )
    
    elements.append(
        Paragraph(
            "4.Monitor Salary Outlier Regularly.",
            styles['BodyText']
        )
    )
    
    elements.append(
        Paragraph(
            "5.Continue Data-Driven HR Desicion Making. ",
            styles['BodyText']
        )
    )
    
    # Build Pdf
    pdf.build(elements)
    print("="*50)
    print("Final_Report.pdf Generated Successfully")
    print("="*50)
    
    
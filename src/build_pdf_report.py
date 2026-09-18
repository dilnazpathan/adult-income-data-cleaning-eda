from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    PageBreak,
    Table,
    TableStyle
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch
import pandas as pd
import os


# ============================================================
# PATHS
# ============================================================

PROJECT_PATH = r"E:\adult_income_eda_project"

DATA_PATH = os.path.join(
    PROJECT_PATH,
    "data",
    "cleaned_adult_dataset.csv"
)

CHARTS_PATH = os.path.join(
    PROJECT_PATH,
    "report",
    "charts"
)

TABLES_PATH = os.path.join(
    PROJECT_PATH,
    "report",
    "tables"
)

PDF_PATH = os.path.join(
    PROJECT_PATH,
    "report",
    "adult_income_eda_report.pdf"
)


# ============================================================
# LOAD DATA
# ============================================================

df = pd.read_csv(DATA_PATH)


# ============================================================
# CREATE PDF
# ============================================================

doc = SimpleDocTemplate(
    PDF_PATH,
    pagesize=A4,
    rightMargin=40,
    leftMargin=40,
    topMargin=40,
    bottomMargin=40
)


# ============================================================
# STYLES
# ============================================================

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "TitleStyle",
    parent=styles["Title"],
    alignment=TA_CENTER,
    fontSize=22,
    leading=28,
    spaceAfter=20
)

subtitle_style = ParagraphStyle(
    "SubtitleStyle",
    parent=styles["Normal"],
    alignment=TA_CENTER,
    fontSize=12,
    leading=18,
    spaceAfter=20
)

heading_style = ParagraphStyle(
    "HeadingStyle",
    parent=styles["Heading1"],
    fontSize=16,
    leading=20,
    spaceBefore=12,
    spaceAfter=10
)

body_style = ParagraphStyle(
    "BodyStyle",
    parent=styles["BodyText"],
    fontSize=10,
    leading=15,
    spaceAfter=8
)


# ============================================================
# STORY
# ============================================================

story = []


# ============================================================
# TITLE PAGE
# ============================================================

story.append(
    Paragraph(
        "Adult Income Data Cleaning and EDA",
        title_style
    )
)

story.append(
    Paragraph(
        "Exploratory Analysis of Demographic, Education and Work Characteristics",
        subtitle_style
    )
)

story.append(Spacer(1, 30))

story.append(
    Paragraph(
        "<b>Business Question</b>",
        heading_style
    )
)

story.append(
    Paragraph(
        "Which demographic, education, and work characteristics "
        "are associated with an annual income above USD 50K "
        "in this census dataset?",
        body_style
    )
)

story.append(
    Paragraph(
        "<b>Dataset Source:</b> UCI Adult Income Dataset",
        body_style
    )
)

story.append(
    Paragraph(
        "<b>Dataset Size:</b> 48,842 records",
        body_style
    )
)

story.append(
    Paragraph(
        "<b>Analysis Type:</b> Descriptive and exploratory analysis",
        body_style
    )
)

story.append(Spacer(1, 30))

story.append(
    Paragraph(
        "This project focuses on descriptive associations. "
        "The observed relationships do not establish causation.",
        body_style
    )
)

story.append(PageBreak())


# ============================================================
# 1. DATA OVERVIEW
# ============================================================

story.append(
    Paragraph(
        "1. Data Overview",
        heading_style
    )
)

story.append(
    Paragraph(
        f"The combined dataset contains <b>{len(df):,}</b> records "
        f"and <b>{len(df.columns)}</b> columns after cleaning and "
        "feature engineering.",
        body_style
    )
)

story.append(
    Paragraph(
        "The dataset combines the original Adult training and test "
        "files while preserving the source split.",
        body_style
    )
)

story.append(
    Paragraph(
        "The main target variable is annual income, categorized as "
        "<b><=50K</b> and <b>>50K</b>.",
        body_style
    )
)


# ============================================================
# 2. DATA CLEANING
# ============================================================

story.append(
    Paragraph(
        "2. Data Cleaning",
        heading_style
    )
)

cleaning_points = [
    "Combined the UCI Adult training and test datasets.",
    "Preserved the original train/test source split.",
    "Trimmed leading and trailing whitespace from text fields.",
    "Converted placeholder and empty categorical values to missing values.",
    "Replaced missing workclass, occupation and native_country values with 'Unknown'.",
    "Converted numeric fields using numeric coercion.",
    "Audited invalid numeric values and impossible core values.",
    "Audited exact duplicate rows without removing them.",
    "Normalized the income labels and created the high_income indicator.",
    "Created age_group, hours_group and net_capital features."
]

for point in cleaning_points:
    story.append(
        Paragraph(
            "• " + point,
            body_style
        )
    )


# ============================================================
# 3. OVERALL INCOME DISTRIBUTION
# ============================================================

story.append(
    Paragraph(
        "3. Overall Income Distribution",
        heading_style
    )
)

high_income_count = int(
    (df["high_income"] == 1).sum()
)

low_income_count = int(
    (df["high_income"] == 0).sum()
)

high_income_pct = round(
    high_income_count / len(df) * 100,
    2
)

low_income_pct = round(
    low_income_count / len(df) * 100,
    2
)

story.append(
    Paragraph(
        f"The dataset contains <b>{low_income_count:,}</b> records "
        f"({low_income_pct}%) with income at or below $50K and "
        f"<b>{high_income_count:,}</b> records "
        f"({high_income_pct}%) above $50K.",
        body_style
    )
)

income_chart = os.path.join(
    CHARTS_PATH,
    "income_distribution.png"
)

if os.path.exists(income_chart):
    story.append(
        Image(
            income_chart,
            width=6.5 * inch,
            height=4.0 * inch
        )
    )

story.append(Spacer(1, 10))


# ============================================================
# 4. EDUCATION
# ============================================================

story.append(
    Paragraph(
        "4. Income Rate by Education",
        heading_style
    )
)

story.append(
    Paragraph(
        "Above-$50K income rates vary across education categories. "
        "The visualization compares the proportion of records above "
        "$50K within each education group.",
        body_style
    )
)

education_chart = os.path.join(
    CHARTS_PATH,
    "education_income_rate.png"
)

if os.path.exists(education_chart):
    story.append(
        Image(
            education_chart,
            width=6.5 * inch,
            height=4.2 * inch
        )
    )

story.append(PageBreak())


# ============================================================
# 5. OCCUPATION
# ============================================================

story.append(
    Paragraph(
        "5. Income Rate by Occupation",
        heading_style
    )
)

story.append(
    Paragraph(
        "The above-$50K income rate differs across occupation "
        "categories in the dataset.",
        body_style
    )
)

occupation_chart = os.path.join(
    CHARTS_PATH,
    "occupation_income_rate.png"
)

if os.path.exists(occupation_chart):
    story.append(
        Image(
            occupation_chart,
            width=6.5 * inch,
            height=4.5 * inch
        )
    )


# ============================================================
# 6. AGE GROUP
# ============================================================

story.append(
    Paragraph(
        "6. Income Rate by Age Group",
        heading_style
    )
)

story.append(
    Paragraph(
        "The above-$50K income rate varies across the defined age "
        "groups, allowing differences in income distribution to be "
        "examined across age ranges.",
        body_style
    )
)

age_chart = os.path.join(
    CHARTS_PATH,
    "age_group_income_rate.png"
)

if os.path.exists(age_chart):
    story.append(
        Image(
            age_chart,
            width=6.5 * inch,
            height=4.0 * inch
        )
    )


# ============================================================
# 7. WORK CLASS
# ============================================================

story.append(
    Paragraph(
        "7. Income Rate by Work Class",
        heading_style
    )
)

story.append(
    Paragraph(
        "Above-$50K income rates vary across work-class categories.",
        body_style
    )
)

workclass_chart = os.path.join(
    CHARTS_PATH,
    "workclass_income_rate.png"
)

if os.path.exists(workclass_chart):
    story.append(
        Image(
            workclass_chart,
            width=6.5 * inch,
            height=4.2 * inch
        )
    )

story.append(PageBreak())


# ============================================================
# 8. SEX
# ============================================================

story.append(
    Paragraph(
        "8. Income Rate by Sex",
        heading_style
    )
)

story.append(
    Paragraph(
        "The observed above-$50K income rates differ between the "
        "sex groups represented in the dataset.",
        body_style
    )
)

sex_chart = os.path.join(
    CHARTS_PATH,
    "sex_income_rate.png"
)

if os.path.exists(sex_chart):
    story.append(
        Image(
            sex_chart,
            width=6.5 * inch,
            height=4.0 * inch
        )
    )


# ============================================================
# 9. WEEKLY WORKING HOURS
# ============================================================

story.append(
    Paragraph(
        "9. Weekly Working Hours",
        heading_style
    )
)

story.append(
    Paragraph(
        "The weekly working-hour distributions are compared between "
        "the two income groups to examine differences in working-hour "
        "patterns.",
        body_style
    )
)

hours_chart = os.path.join(
    CHARTS_PATH,
    "weekly_hours_distribution.png"
)

if os.path.exists(hours_chart):
    story.append(
        Image(
            hours_chart,
            width=6.5 * inch,
            height=4.2 * inch
        )
    )


# ============================================================
# 10. NUMERIC RELATIONSHIPS
# ============================================================

story.append(
    Paragraph(
        "10. Numeric Relationships",
        heading_style
    )
)

story.append(
    Paragraph(
        "The correlation matrix summarizes linear relationships "
        "among selected numeric variables and the high-income indicator.",
        body_style
    )
)

correlation_chart = os.path.join(
    CHARTS_PATH,
    "numeric_correlation_heatmap.png"
)

if os.path.exists(correlation_chart):
    story.append(
        Image(
            correlation_chart,
            width=6.5 * inch,
            height=5.0 * inch
        )
    )

story.append(PageBreak())


# ============================================================
# 11. CAPITAL GAIN
# ============================================================

story.append(
    Paragraph(
        "11. Capital Gain Distribution",
        heading_style
    )
)

story.append(
    Paragraph(
        "Capital gain values are concentrated around lower values, "
        "with a smaller number of substantially larger observations.",
        body_style
    )
)

capital_chart = os.path.join(
    CHARTS_PATH,
    "capital_gain_distribution.png"
)

if os.path.exists(capital_chart):
    story.append(
        Image(
            capital_chart,
            width=6.5 * inch,
            height=4.2 * inch
        )
    )


# ============================================================
# 12. KEY FINDINGS
# ============================================================

story.append(
    Paragraph(
        "12. Key Findings",
        heading_style
    )
)

findings = [
    f"{high_income_pct}% of the records have annual income above $50K.",
    "Above-$50K income rates vary across education levels.",
    "Above-$50K income rates vary across occupation categories.",
    "Above-$50K income rates differ across age groups.",
    "Above-$50K income rates vary across work-class categories.",
    "Observed above-$50K income rates differ between the sex groups.",
    "Weekly working-hour distributions differ between income groups.",
    "Numeric variables show different levels of association with the income indicator.",
    "Capital gain is strongly concentrated at low or zero values with a smaller number of large observations."
]

for finding in findings:
    story.append(
        Paragraph(
            "• " + finding,
            body_style
        )
    )


# ============================================================
# 13. LIMITATIONS
# ============================================================

story.append(
    Paragraph(
        "13. Limitations",
        heading_style
    )
)

limitations = [
    "The dataset represents a historical census-based sample and may not represent current populations.",
    "The analysis is observational and descriptive; associations do not establish causation.",
    "Demographic variables should be interpreted as descriptive characteristics rather than causal explanations.",
    "The visual summaries are not weighted population estimates.",
    "The analysis does not perform predictive modeling or claim individual-level income prediction."
]

for limitation in limitations:
    story.append(
        Paragraph(
            "• " + limitation,
            body_style
        )
    )


# ============================================================
# 14. CONCLUSION
# ============================================================

story.append(
    Paragraph(
        "14. Conclusion",
        heading_style
    )
)

story.append(
    Paragraph(
        "The exploratory analysis identifies differences in above-$50K "
        "income rates across education, occupation, age group, work "
        "class and sex. Weekly working hours and numeric variables "
        "also show different patterns across income groups. These "
        "results provide descriptive insights into the dataset and "
        "can serve as a foundation for later predictive modeling, "
        "while recognizing that the observed relationships do not "
        "demonstrate causation.",
        body_style
    )
)


# ============================================================
# BUILD PDF
# ============================================================

doc.build(story)

print("PDF report created successfully.")
print("Location:")
print(PDF_PATH)
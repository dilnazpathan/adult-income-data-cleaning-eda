# Adult Income Data Cleaning and Exploratory Data Analysis

## Project Overview

This project performs data cleaning and exploratory data analysis on the UCI Adult Income dataset to understand which demographic, education, and work characteristics are associated with annual income above USD 50K.

The analysis focuses on descriptive associations in the dataset and does not attempt to establish causal relationships.

## Business Question

Which demographic, education, and work characteristics are associated with an annual income above USD 50K?

## Objectives

- Inspect the raw dataset structure, data types, missing values, and duplicate records
- Clean and standardize categorical and numeric data
- Normalize the income target variable
- Measure the proportion of records with income above USD 50K
- Compare above-50K income rates across:
  - Education
  - Occupation
  - Age groups
  - Work class
  - Sex
- Analyze weekly working-hour distributions between income groups
- Examine relationships among numeric variables
- Identify important patterns and limitations in the dataset

## Dataset

**Source:** UCI Machine Learning Repository – Adult Dataset

The dataset contains census-related demographic, education, employment, and income information.

### Dataset Size

- Records: 48,842
- Original features: 14
- Target variable: Income
- Additional project column: `source_split`

## Data Cleaning

The following cleaning steps were performed:

1. Combined the original training and testing datasets.
2. Preserved the original dataset split using `source_split`.
3. Removed unnecessary leading and trailing whitespace from text fields.
4. Identified missing-value markers and empty text values.
5. Replaced missing values in `workclass`, `occupation`, and `native_country` with `Unknown`.
6. Converted numeric columns to appropriate numeric data types.
7. Checked for invalid numeric and impossible core values.
8. Audited duplicate records without removing them because the dataset does not contain a unique person identifier.
9. Normalized the income labels.
10. Created a binary `high_income` variable:
    - `0` = Income <= 50K
    - `1` = Income > 50K

## Feature Engineering

Additional analysis features were created:

- `age_group`
- `hours_group`
- `net_capital`
- `high_income`

## Exploratory Data Analysis

The project includes analysis of:

### Income Distribution

Comparison of records with income <= 50K and income > 50K.

### Education

Comparison of the proportion of high-income records across education levels.

### Occupation

Comparison of high-income rates across occupation categories.

### Age Groups

Analysis of high-income rates across different age groups.

### Work Class

Comparison of income groups across work-class categories.

### Sex

Comparison of high-income rates by sex.

### Weekly Working Hours

Comparison of weekly working-hour distributions between income groups.

### Numeric Relationships

Correlation analysis among numeric variables including:

- Age
- Final weight
- Education number
- Capital gain
- Capital loss
- Hours per week
- Net capital
- High-income indicator

## Key Result

The cleaned dataset contains:

- 37,155 records with income <= 50K
- 11,687 records with income > 50K
- Approximately 23.93% of records belong to the above-50K income group.

The analysis also shows differences in above-50K income rates across education, occupation, age group, work class, and sex categories.

These findings describe associations within this dataset and should not be interpreted as causal effects.

## Project Structure

```text
adult-income-data-cleaning-eda/
│
├── data/
│   ├── adult_income_raw.csv
│   └── cleaned_adult_dataset.csv
│
├── report/
│   ├── adult_income_eda_report.pdf
│   ├── charts/
│   └── tables/
│
├── src/
│   ├── Data Cleaning.ipynb
│   ├── Data Analysis.ipynb
│   └── build_pdf_report.py
│
├── README.md
└── requirements.txt

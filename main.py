import pandas as pd

data = pd.read_csv('salaries_by_college_major.csv')

# .head()
# returns the first 5 rows (or another number, is spec.)
# print(data.head())

# .tail()
# returns the last 5 rows (or another number, if spec.)
# print(data.tail())

# .shape
# returns the number of rows and columns
# print(data.shape)

# .columns
# retirms the list of dataframe columns
# print(data.columns)

# .isna()
# returns True for fields that have a non-numerical value
# print(data.isna())

# .dropna()
# drops (deletes) the rows with non-numerical values
clean_data = data.dropna()
# print(clean_data.tail())

# .max() / .min()
# returns the maximum / minimum value in a given column
# >>> print(clean_data['Starting Median Salary'].max())
# 74300.0

# .idxmax() / .idxmin()
# returns the index of the column's maximum / minimum value
# >>> print(clean_data['Starting Median Salary'].idxmax())
# 43

# .loc
# returns the value at a given row (id) from a given column
# >>> print(clean_data['Undergraduate Major'].loc[43])
# Physician Assistant
# >>> print(clean_data['Undergraduate Major'][43])
# Physician Assistant

# to get the entire row, don't specify the column
# >>> print(clean_data.loc[43])
# Undergraduate Major                  Physician Assistant
# Starting Median Salary                           74300.0
# Mid-Career Median Salary                         91700.0
# Mid-Career 10th Percentile Salary                66400.0
# Mid-Career 90th Percentile Salary               124000.0
# Group                                               STEM

# [1.0] get the highest mid-career salary
# >>> highest_value = clean_data['Mid-Career Median Salary'].max()
# >>> print(highest_value)
# 107000.0
# [1.1] print the corresponding undergraduate major
# >>> highest_value_major = clean_data['Undergraduate Major'][clean_data['Mid-Career Median Salary'].idxmax()]
# >>> print(highest_value_major)
# Chemical Engineer

# [2.0] get the lowest starting median salary
# >>> print(clean_data['Starting Median Salary'].min())
# 34000.0
# [2.1] get the corresponging undergraduate major
# >>> print(clean_data['Undergraduate Major'][clean_data['Starting Median Salary'].idxmin()])

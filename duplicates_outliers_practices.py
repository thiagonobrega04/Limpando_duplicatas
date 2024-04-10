import pandas as pd
import numpy as np

# Create a DataFrame with data
df = pd.DataFrame({'Pupil': ['Sara', 'Tom', 'Sara', 'Bob', 'Tom', 'Alice'],
                   'Age':   [7, 10, 7, 11, 9, np.nan]})

print(f'DataFrame before Cleaning:\n{df}\n')

# Handle Duplicates
df = df.drop_duplicates()

# Handle Missing Values: Replacement
median_age = df['Age'].median()
df['Age'].fillna(median_age, inplace=True)

# Identify Outliers
Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Handle Outliers: Replacement
median = df['Age'].median()
df['Age'] = np.where((df['Age'] > upper_bound) | (df['Age'] < lower_bound), median, df['Age'])

print(f'DataFrame after Cleaning:\n{df}')

# Represent a small dataset of student grades
data = {'Name': ['John', 'Anna', 'Peter', 'John', 'Anna'],
        'Score': [85, 90, 78, 85, 140]}
df = pd.DataFrame(data)

print(f'DataFrame before Cleaning:\n{df}\n')

# Drop duplicate records from the dataset
df = df.drop_duplicates()

# Compute Q1, Q3, and IQR for scores
Q1, Q3 = df['Score'].quantile([0.25, 0.75])
IQR = Q3 - Q1

# Identify outliers and replace them with the mean score
mean = df['Score'].mean()
df['Score'] = np.where((df['Score'] < Q1 - 1.5 * IQR) | (df['Score'] > Q3 + 1.5 * IQR), mean, df['Score'])

print(f'DataFrame after Cleaning:\n{df}')

homes = {'Location': ['North', 'South', 'East', 'North', 'South'],
         'Price': [400000, 200000, 300000, 400000, 200000],
         'Beds': [3, 2, 1, 3, 2]}
df = pd.DataFrame(homes)

print(f'DataFrame before Cleaning:\n{df}\n')

df = df.drop_duplicates()

Q1 = df['Price'].quantile(0.25)
Q3 = df['Price'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

median = df['Price'].median()
df['Price'] = np.where((df['Price'] > upper_bound) | (df['Price'] < lower_bound), median, df['Price'])

print(f'DataFrame after Cleaning:\n{df}')

data = [{ "StudentName": "Tom", "Age": 13, "Grade": "Seventh" },
        { "StudentName": "Tom", "Age": 13, "Grade": "Seventh" },
        { "StudentName": "Jim", "Age": 15, "Grade": "Ninth" },
        { "StudentName": "Sabrina", "Age": 12, "Grade": "Sixth" },
        { "StudentName": "Penny", "Age": 15, "Grade": "Ninth" }]

df = pd.DataFrame(data)

print(f'DataFrame before Cleaning:\n{df}\n')

# TODO: Implement code to remove duplicates from our data
df = df.drop_duplicates()

Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# TODO: Implement code to replace outliers with the median
median = df['Age'].median()
df['Age'] = np.where((df['Age'] > upper_bound) | (df['Age'] < lower_bound), median, df['Age'])

print(f'DataFrame after Cleaning:\n{df}')

data = [{ "StudentName": "Tom", "Age": 13, "Grade": "Seventh" },
        { "StudentName": "Tom", "Age": 13, "Grade": "Seventh" },
        { "StudentName": "Jim", "Age": 15, "Grade": "Ninth" },
        { "StudentName": "Sabrina", "Age": 12, "Grade": "Sixth" },
        { "StudentName": "Penny", "Age": 15, "Grade": "Ninth" }]

# TODO: Create a DataFrame 'df'
df = pd.DataFrame(data)
print(f'DataFrame before Cleaning:\n{df}\n')

# TODO: Remove duplicates from the DataFrame
df = df.drop_duplicates()
print(f'Data without Duplicates:\n{df}\n')

# TODO: Calculate the median of the 'Age' column
median_age = df["Age"].median()
print(f'Median age is: \n{median_age}\n')

# TODO: Calculate Q1, Q3, and IQR for age. Afterwards, calculate the lower and upper bounds.
Q1, Q3 = df['Age'].quantile([0.25, 0.75])
IQR = Q3 - Q1

lower_bound = Q1 - 1.5*IQR
upper_bound = Q3 + 1.5*IQR

# TODO: Replace any outliers in the 'Age' data with the calculated median
df['Age'] = np.where((df['Age'] > upper_bound) | (df['Age'] < lower_bound), median_age, df['Age'])

print(f'DataFrame after Cleaning:\n{df}')
import pandas as pd
import numpy as np

# Python Tools for Handling Outliers

# Create dataset
data = pd.DataFrame({
    'students': ['Alice', 'Bob', 'John', 'Ann', 'Rob'],
    'scores': [56, 11, 50, 98, 47]
})
df = pd.DataFrame(data)

Q1 = df['scores'].quantile(0.25)  # 47.0
print(Q1)

Q3 = df['scores'].quantile(0.75)  # 56.0
print(Q3)

IQR = Q3 - Q1  # 9.0
print(IQR)

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['scores'] < lower_bound) | (df['scores'] > upper_bound)]
print(outliers)
'''Output:
  students  scores
1      Bob      11
3      Ann      98
'''

# Handling Outliers: Removal
# Typically, there are two common strategies for dealing with outliers: remove them or replace them with a median value.

# Removing outliers is the easiest method. However, there are better methods than this since you essentially throw away your data. To apply it, let's reverse the condition to choose everything except outliers.

df = df[(df['scores'] >= lower_bound) & (df['scores'] <= upper_bound)]
print(df)
'''Output:
  students  scores
0    Alice      56
2     John      50
4      Rob      47
'''

# Handling Outliers: Replacement
# The second strategy is replacing outliers with median values - they are less susceptible to outliers, so we can use them for replacement.

# The easiest way to apply this replacement is to first replace outliers with np.nan and then use the fill method. It could lead to problems, as there could already be some missing values in the dataframe, which will also be filled.

# Instead, we could use the np.where function:

median = df['scores'].median()
df['scores'] = np.where((df['scores'] > upper_bound) | (df['scores'] < lower_bound), median, df['scores'])
print(df)
import pandas as pd
import numpy as np

# Create DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'John', 'Anna'],
        'Age': [16, 15, 13, 16, 15],
        'Grade': [9, 10, 7, 9, 10]}
df = pd.DataFrame(data)

# The duplicated() function flags duplicate rows:
print(df.duplicated())
'''Output:
0    False
1    False
2    False
3     True
4     True
dtype: bool
'''

# A True in the output denotes a row in the DataFrame that repeats. Note, that one of the repeating rows is marked as False – to keep one in case we decide to drop all the duplicates.

# The drop_duplicates() function helps to discard these duplicates:
df = df.drop_duplicates()
print(df)
'''Output:
    Name  Age  Grade
0   John   16      9
1   Anna   15     10
2  Peter   13      7
'''
# Adding two numbers program 
a = 10
b = 20
sum = a + b
print("Sum:", sum)

# adding two dataframe 
import pandas as pd
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
df = pd.concat([df1, df2])
print(df)

# looping the dataframe
for index, row in df.iterrows():
    print(row['A'], row['B'])
# joining two dataframes
df3 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df4 = pd.DataFrame({'A': [1, 2], 'C': [5, 6]})
df5 = pd.merge(df3, df4, on='A')
print(df5)

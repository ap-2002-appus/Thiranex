import pandas as pd

df = pd.read_csv('student_data.csv')
df['MathScore'] = df['MathScore'].fillna(df['MathScore'].mean())
df['ScienceScore'] = df['ScienceScore'].fillna(df['ScienceScore'].mean())
df = df.drop_duplicates()
df.to_csv('cleaned_student_data.csv', index=False)

print('Data cleaned successfully')

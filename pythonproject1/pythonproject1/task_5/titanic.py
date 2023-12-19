import pandas as pd

df = pd.read_csv('titanic.csv')
print(df.groupby('Survived')['Survived'].count())
print(df.groupby(['Survived', 'Sex'])['Survived'].count()['Age'].sum())
import pandas as pd
import matplotlib.pyplot as plt

apple = pd.read_csv('apple.csv', parse_dates=True, index_col='Date')
# Временной ряд
print(apple.loc['2017', 'Close'].mean())
print(apple.loc['2017-Feb', 'Close'].mean())
print(apple.loc['2017-01-09':'2017-02-01', 'Close'].mean())

plt.plot(apple['Open'])
plt.show()
import matplotlib.pyplot as plt
import pandas as pd

flights = pd.DataFrame({
    'id': [0, 1, 2, 3],
    'year': [2013, 2013, 2013, 2013],
    'month': [1, 9, 3, 1],
    'dep_time': [517., 533., 542., 544.],
    'sched_dep_time': [515, 529, 540, 545]
}).set_index('id')

# print(flights.groupby('month')['dep_time'].sum())

# plt.plot(flights.groupby('month')['dep_time'].sum())
# plt.show()

plt.plot(flights.groupby('month')['dep_time'].mean())
plt.show()
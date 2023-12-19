import pandas as pd

my_df = pd.DataFrame({
    'product': ['bread', 'milk', 'potato', 'candies'],
    'day_1': [123, 5434, 34523, 345234],
    'day_2': [4524,23413, 34, 2134],
    'day_3': [5635, 5678,324, 42532],
    'day_4': [456,2131, 63456, 876]
}, index=['B', 'M', 'P', 'C'])

print(my_df)

# Примеры обращения
print(my_df.loc[['B', 'M'], 'day_1'])
print(my_df.loc[['B', 'M'], ['day_1', 'day_2']])
print(my_df.loc['B':'M'])
print(my_df.day_1)
print(my_df['day_1'])

my_df_step_2 = pd.DataFrame({
    'day_1': [123, 5434, 34523, 345234],
    'product': ['bread', 'milk', 'potato', 'candies'],
    'day_2': [4524,23413, 34, 2134],
    'day_3': [5635, 5678,324, 42532],
    'day_4': [456,2131, 63456, 876]
}).set_index('product')

print(my_df_step_2)

# my_df_step_2 = my_df_step_2.reset_index()
print(my_df_step_2)

my_df_step_2 = my_df_step_2.rename(columns={'day_1': 'day_2'})
my_df_step_2 = my_df_step_2.rename(index={'bread': 'bread_01'})

print(my_df_step_2)

my_df_step_2['sum'] = my_df_step_2.sum(axis=1)
print(my_df_step_2)

my_df_step_2 = my_df_step_2.drop(['day_4'], axis='columns')
my_df_step_2 = my_df_step_2.drop('candies')
print(my_df_step_2)

flies = pd.DataFrame({
    'id': [0, 1, 2, 3],
    'year': [2013, 2013, 2013, 2013],
    'month': [1, 9, 3, 1],
    'dep_time': [517., 533., 542., 544.],
    'sched_dep_time': [515, 529, 540, 545]
}).set_index('id')
print(flies[flies['month'] == 1])

flies['diff'] = flies['dep_time'] - flies['sched_dep_time']
print(flies)


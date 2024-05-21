import pandas as pd

df1 = pd.DataFrame(
    {
        'key':['A','B','C','D'],
        'value': [1,2,3,4]

    }
)

df2 = pd.DataFrame(
    {
        'key':['B','E','F'],
        'value':[6,7,8]
    }
)


print(df1)
print(df2)

# inner_join = pd.merge(df1,df2,on='key',how='inner')
# print(inner_join)

'''
  key  value_x  value_y
0   B        2        6
'''

# outer_join = pd.merge(df1,df2,on='key',how = 'outer')
# print(outer_join)

'''
  key  value_x  value_y
0   A      1.0      NaN
1   B      2.0      6.0
2   C      3.0      NaN
3   D      4.0      NaN
4   E      NaN      7.0
5   F      NaN      8.0

'''

left_join = pd.merge(df1,df2,on='key',how='left')
print(left_join)

right_join = pd.merge(df1,df2,on='key',how='right')
print(right_join)

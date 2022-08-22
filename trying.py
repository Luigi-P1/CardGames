import beforeHandAction



print (beforeHandAction.betPlacement(100))
# import pandas as pd
#
#
# def fun(df):
#     dfTypes = df.dtypes
#     columns = list(df.columns)
#     for i in range(len(columns)):
#         if dfTypes[i] == 'string':
#             print('yay')
#             for x in df[columns[i]]:
#                 df[columns[i]] = df[columns[i]].replace([x], x.strip())
#     return df
#
#
# lst = [('jack', 34, 'Sydney', 155),
#        ('Riti', 31, 'Delhi', 177.5),
#        ('Aadi', 16, 'Mumbai', 81),
#        ('Mohit', 31, 'Delhi', 167),
#        ('Veena', 12, 'Delhi', 144),
#        ('Shaunak', 35, 'Mumbai', 135),
#        ('Shaun', 35, 'Colombo', 111)
#        ]
# # print(lst)
# d = pd.DataFrame(lst)
# # print(d)
# df = pd.DataFrame(lst, columns=['Name', 'Age', 'City', 'Marks'])
# df = df.astype({'Name': 'string',
#                 'City': 'string'})
# a = fun
# print(a(df))

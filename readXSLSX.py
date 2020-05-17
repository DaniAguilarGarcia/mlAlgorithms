import pandas as pd 
# data.xslsx contains  data which contains multiple spreadsheets
#When we don't use any keyword arguments, the returned DataFrame from pd.read_excel contains the first sheet of the Excel workbook.

df = pd.read_excel('data.xlsx')
# Newline to separate print statements
print('{}\n'.format(df))
#sheet_name=None returns all the sheets in an ordered dictionary.
#sheet_name keyword argument, we can obtain a specific spreadsheet by passing in its integer index or name.
print('Sheet 1 (0-indexed) DataFrame:')
df = pd.read_excel('data.xlsx', sheet_name=1)
print('{}\n'.format(df))

print('MIL DataFrame:')
df = pd.read_excel('data.xlsx', sheet_name='MIL')
print('{}\n'.format(df))

# Sheets 0 and 1
df_dict = pd.read_excel('data.xlsx', sheet_name=[0, 1])
print('{}\n'.format(df_dict[1]))

# All Sheets
df_dict = pd.read_excel('data.xlsx', sheet_name=None)
print(df_dict.keys())

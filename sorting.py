import pandas as pd
# df is predefined
#The first example sorts by 'yearID' in ascending order, 
# while the second sorts 'playerID' in descending lexicographic (alphabetical) order.
print('{}\n'.format(df))

sort1 = df.sort_values('yearID')
print('{}\n'.format(sort1))

sort2 = df.sort_values('playerID', ascending=False)
print('{}\n'.format(sort2))
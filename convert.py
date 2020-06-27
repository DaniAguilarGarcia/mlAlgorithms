import pandas as pd
# predefined df
#get_dummies function. The function takes in a DataFrame as its required argument, 
#and returns the DataFrame with each of its categorical features converted to indicator features.

print('{}\n'.format(df))

converted = pd.get_dummies(df)
print('{}\n'.format(converted.columns))

print('{}\n'.format(converted[['teamID_BOS',
                               'teamID_PIT']]))
print('{}\n'.format(converted[['lgID_AL',
                               'lgID_NL']]))
# predefined data
#The code below demonstrates various initialization strategies for
# predefined data
print('{}\n'.format(repr(data)))

from sklearn.impute import SimpleImputer
imp_median = SimpleImputer(strategy='median') #strategy fills in missing data with the median from each column
transformed = imp_median.fit_transform(data)
print('{}\n'.format(repr(transformed)))

imp_frequent = SimpleImputer(strategy='most_frequent') #uses the value that appears the most for each column
transformed = imp_frequent.fit_transform(data)
print('{}\n'.format(repr(transformed)))

#There are also more advanced imputation methods such as k-Nearest Neighbors 
# (filling in missing values based on similarity scores from the kNN algorithm) and MICE 
# (applying multiple chained imputations, assuming the missing values are randomly distributed across observations).
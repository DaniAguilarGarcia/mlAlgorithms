# predefined pizza data and prices
#The code below demonstrates how to fit a LinearRegression model to a dataset of 
# 5 different pizzas (pizza_data) and corresponding pizza prices
print('{}\n'.format(repr(pizza_data)))
print('{}\n'.format(repr(pizza_prices)))
#represents the number of calories 
#and the second column represents net weight (in grams
from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit(pizza_data, pizza_prices)
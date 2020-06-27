# MlAlgorithms

Open source learning material.
This is a collection of basic Machine Learninc algorithms.

Some notes about the most complicated algorithms 

Linear regression
data modeling:  finding an equation or distribution that best fits a given dataset.
    *linear combination can approximate the data well
    *linear regression refers to using a linear model to represent the 
    relationship between a set of independent variables and a dependent variable.
    *y= ax1 +bx2 +cx3 + d
     y (dependent variable) based on the linear combination of independent variables x_1, x_2, x_3. 
     The coefficients a, b, c and intercept d determine the model's fit.
    * least squares regression: a regression model, which is a linear combination of the independent variables, 
    that minimizes the sum of squared residuals between the model's predictions and actual values for the dependent variable.
    * coefficient of determination (or R2 value) using the score function applied to the dataset and labels. The R2 value tells 
    us how close of a fit the linear model is to the data, or in other words, how good of a fit the model is for the data.
    R2 value is a real number between 0 and 1. In scikit-learn it ranges from -∞ to 1. 
    where lower values denote a poorer model fit to the data. The closer the value is to 1, 
    the better the model's fit on the data.
    * Cons: it relies on the fact that the dataset's features are each independent, i.e. uncorrelated. 
    when the dataset is linearly correlated , the model becomes highly intolerant to noise in the data.
    
Ridge Regression 
    *regularization, find the weights (coefficients) for the linear model that minimize the sum of squared residuals:
    the goal is to not only minimize the sum of squared residuals, but to do this with coefficients as small as possible.
    The smaller the coefficients, the less susceptible they are to random noise in the data.
    Larger quantities of α will put greater emphasis on the penalty term, forcing the model to have even smaller weight value.
    *Choosing the best alpha: we can use cross-validation to help us choose the optimal α from a list of values. RidgeCV object.

LASSO Regression
    *sparse regularization uses an L2 norm penalty term.
    *LASSO tends to prefer linear models with fewer parameter values. 
Bayesian Regression:
    *make certain assumptions about the probability distributions of a models parameters before being fitted on data.
    there are two hyperparameters to optimize: α and λ. The α hyperparameter serves the same exact purpose as it does for
    regular ridge regression; namely, it acts as a scaling factor for the penalty term. Both have gamma distribution priors 
    (we assume both values come from there).
    *Tuning the model

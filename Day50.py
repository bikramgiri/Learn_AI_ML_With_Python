# Day50: Linear Regression

# *Introduction to Linear Regression:
# Linear regression is a statistical method used to model the relationship between a dependent variable and one or more independent variables. 
# The goal is to find the best-fitting line (or hyperplane in higher dimensions) that predicts the dependent variable based on the independent variables.

# In a two-dimensional space, linear regression attempts to fit a straight line through a set of points. 
# The line is defined by the equation:
# y = mx + c
# Where:
# - y is the dependent variable (the variable we want to predict)
# - x is the independent variable (the input feature)
# - m is the slope of the line (representing the relationship between x and y)
# - c is the y-intercept (the value of y when x is 0)
# - In ML, c is bias
# The objective of linear regression is to find the values of m and c that minimize the difference between the predicted values (y') and the actual values (y) in the training data. 
# This difference is often measured using a loss function, such as mean squared error (MSE).

# *Geometric Intuition of Linear Regression:
# Geometrically, linear regression can be visualized as finding the line that best fits a scatter plot of data points. 
# The best-fitting line minimizes the vertical distances (residuals) between the actual data points and the predicted values on the line.
# The slope (m) of the line indicates the direction and steepness of the relationship between the independent and dependent variables.
# A positive slope indicates a positive correlation (as x increases, y also increases), while a negative slope indicates a negative correlation (as x increases, y decreases).
# The y-intercept (c) represents the value of y when x is zero, providing a starting point for the line on the y-axis.
# In higher dimensions (multiple independent variables), linear regression extends to fitting a hyperplane in a multi-dimensional space.
# The geometric intuition remains similar, where the goal is to minimize the distances between the actual data points and the hyperplane.


# *Cost Fuction:
# The cost function in linear regression quantifies the error between the predicted values and the actual values in the training data.
# The most commonly used cost function for linear regression is the Mean Squared Error (MSE), which is defined as:
# MSE = (1/2n) * Σ(y_i - hθ_i)²
# Where:
# - MSE is the Mean Squared Error
# - θ is theta
# - n is the number of data points
# - y_i is the actual value of the dependent variable for the i-th data point
# - h0_i is the predicted value of the dependent variable for the i-th data point
# - Σ denotes the summation over all data points
# The MSE measures the average squared difference between the actual and predicted values.
# The goal of linear regression is to minimize the MSE by adjusting the parameters (slope m and intercept c) of the linear equation.
# A lower MSE indicates a better fit of the model to the data, as it means that the predicted values are closer to the actual values.
# The cost function provides a quantitative measure of how well the linear regression model is performing, and it is used in optimization algorithms (such as gradient descent) to iteratively update the model parameters to achieve the best fit.

# *Uses of cost function:
# 1. Model Evaluation: The cost function provides a quantitative measure of how well the linear regression model is performing on the training data.
# 2. Parameter Optimization: The cost function is used in optimization algorithms (like gradient descent) to iteratively update the model parameters (slope and intercept) to minimize the error.
# 3. Hyperparameter Tuning: The cost function can be used to evaluate different configurations of the model, such as different learning rates or regularization parameters, to find the best-performing model.
# 4. Model Comparison: The cost function allows for the comparison of different linear regression models to determine which one provides a better fit to the data.
# 5. Early Stopping: In some cases, the cost function can be monitored during training to implement early stopping, preventing overfitting by halting training when the cost starts to increase on a validation set.
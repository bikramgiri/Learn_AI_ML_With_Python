# Day52:

## Lets Consider a Scenario:
# 1. The bias is approximately equal to zero.
# i.e., theta0 ~= 0
# 2. Training data has low size or is less in number
# m = 5

# While testing on training data:
# J(θ) = Nearly equal to zero or zero
# While tested on testing data:
# J(θ) = gives a large value

# 1. First we have a complete dataset.
# 2. We split the dataset into training and testing datasets.
# For example:
# 80% = training data And 
# 20% = testing data (Algorithm has never seen this data before)
# 3. We train the model on the training dataset.
# 4. We test the model on the testing dataset.
# 5. If the model performs well on the training dataset but poorly on the testing dataset, it indicates overfitting.


# Overfitting:
# Overfitting occurs when a machine learning model learns the training data too well, including its noise and outliers, leading to poor generalization to new, unseen data. 
# This often happens when the model is too complex relative to the amount of training data available.

# 1. The model performs well with the training data (low bias)
# 2. The model fails to perform well with the testing data (high variance).

# Signs of overfitting include:     
# 1. High accuracy on training data but low accuracy on validation/test data.
# 2. The model captures noise and random fluctuations in the training data rather than the underlying patterns.
# 3. The model performs well on the training set but poorly on new data.      

# Techniques to overcome overfitting:
# 1. Add External Bias(Regularization):
# Regularization is a technique used to prevent overfitting in machine learning models by adding a penalty term to the loss function.
# It discourages the model from fitting the training data too closely, thereby improving its generalization.
# L1 Regularization (Lasso Regression):
# Adds the absolute values of the coefficients as a penalty term to the loss function.
# It can lead to sparse models where some coefficients become exactly zero, effectively performing feature selection.
# L2 Regularization (Ridge Regression):
# Adds the squared values of the coefficients as a penalty term to the loss function.
# It tends to shrink the coefficients towards zero but does not set them exactly to zero.

# Advantages of L1 Regularization(Lasso Regression):
# 1. Feature Selection: L1 regularization can lead to sparse models by driving some coefficients to exactly zero, effectively performing feature selection.
# 2. Interpretability: Sparse models are often easier to interpret, as they involve fewer features.
# 3. Robustness to Outliers: L1 regularization is less sensitive to outliers compared to L2 regularization.

# Disadvantages of L1 Regularization(Lasso Regression):
# 1. Computational Complexity: L1 regularization can be computationally more intensive than L
# 2. Instability: In cases of high multicollinearity, L1 regularization may arbitrarily select one feature over another, leading to instability in feature selection.
# 3. Limited Grouping Effect: L1 regularization may not perform well when there are groups of correlated features, as it tends to select only one feature from each group.

# Advantages of L2 Regularization(Ridge Regression):
# 1. Stability: L2 regularization tends to produce more stable solutions, especially in the presence of multicollinearity among features.
# 2. Computational Efficiency: L2 regularization is computationally more efficient than L1 regularization, making it suitable for large datasets.
# 3. Smooth Solutions: L2 regularization encourages smaller coefficients, leading to smoother models.

# Disadvantages of L2 Regularization(Ridge Regression):
# 1. No Feature Selection: Unlike L1 regularization, L2 regularization does not perform feature selection, as it shrinks coefficients but does not set them to zero.
# 2. Interpretability: Models with L2 regularization may be less interpretable due to the presence of all features, even if some have small coefficients.
# 3. Sensitivity to Outliers: L2 regularization can be sensitive to outliers, as it squares the residuals in the loss function.


# 2. Use Simpler Models:
# Opt for less complex models that are less likely to overfit the training data.

# 3. Increase Training Data:
# Gather more training data to provide a more comprehensive view of the underlying patterns.

# 4. Feature Selection:
# Remove irrelevant or redundant features to reduce the complexity of the model.

# 5. Ensemble Methods:
# Combine multiple models to improve generalization and reduce the risk of overfitting.

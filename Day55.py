# Day55: Logistic Regression

# *Logistic Regression:
# It is simply a classification algorithm used to assign observations to a discrete set of classes.
# It is used when the dependent variable(target) is categorical.
# Example: Spam detection (spam or not spam), disease diagnosis (disease or no disease) etc.
# It uses the logistic function to model a binary dependent variable.

# Example: Predicting whether a student will pass or fail an exam based on their study hours.
# If student get 1 he/she pass the exam, if 0 he/she fail the exam.
# Assume if a student studies for more than 5 hours, they pass the exam; otherwise, they fail.
# In this case, the independent variable is the number of study hours, and the dependent variable is a binary outcome (pass/fail).

# In term of linear regression(In graphical representation, in x-axis: No, of hours studied and y-axis: Result) for same example:
# If result > 0.5 then pass
# If result <= 0.5 then fail

# *Linear Regression affect by outliers but Logistic Regression is not affected by outliers.
# As we know Linear Regression affect by outliers so it is not used/suitable for classification problems.

# *Sigmoid Function:
# It is also known as the logistic function.
# It is used to map predicted values to probabilities.
# The sigmoid function takes any real-valued number and maps it to a value between 0 and 1.

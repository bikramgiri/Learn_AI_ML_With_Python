# Day48: Introduction to Machine Learning

# Today Learning:

# 1. Introduction to Machine Learning
# 2. Components of Machine Learning
# 3. Why Machine Learning?
# 4. Applications of Machine Learning
# 5. Challenges in Machine Learning
# 6. Categories of Machine Learning:
# - Based on production Level: Batch Learning or Offline Mode, Online  Mode or Incremental Learning
# - Based on Learning Approach: Instance Based Learning, Model Based Learning
# - Based on Supervision: Supervised Learning, Unsupervised Learning, Semi-Supervised Learning, Reinforcement Learning
# 7. Teachable Machine


## *Based on production Level: 
# *Batch Learning or Offline Mode:
# In this mode, the model is trained on a fixed dataset and then deployed. 
# It does not learn from new data until it is retrained with a new dataset.
# E.g: Animal Recognition

# *Online  Mode or Incremental Learning
# In this mode, the model is continuously updated with new data. It learns from each new data point and can adapt to changes in the data distribution over time.
# E.g: Stock Price Prediction, Recommendation Systems


## **Based on Learning Approach: 
# *Instance Based Learning(Ratera Phadnae)
# In this approach, the model learns from specific instances or examples in the training data. 
# It makes predictions based on the similarity of new instances to the training instances.
# E.g: K-Nearest Neighbors (KNN) Algorithm, it means it stores the training data and uses it for making predictions.
# 1. Distance Metric: KNN uses a distance metric (e.g., Euclidean distance) to find the closest training examples to a new instance.
# 2. K Value: The "K" in KNN represents the number of nearest neighbors to consider when making a prediction.
# 3. Voting Mechanism: KNN typically uses a majority voting mechanism among the K nearest neighbors to determine the predicted class for a new instance.

# E.g: red dot denote fail, green dot denote pass, it take 3 dot near to it, if 2 dot are green and one dot red then it will predict pass, 
# if all are green then it will predict pass,
# if all are red then it will predict fail, 
# if 2 dot are red and one dot green then it will predict fail.

# *Model Based Learning(Bujera Phadnae)
# In this approach, the model learns a general representation from the training data and makes predictions based on this learned model.
# E.g: Linear Regression, Decision Trees

# E.g: red dot denote fail, green dot denote pass, then it make function  to predicate the result, whether it will be pass or fail,
# it will make line or curve to separate the pass and fail dot, then it will use this line or curve to predict the result.


## **Based on Supervision: 
# *Supervised Learning:
# In this approach, the model is trained on labeled data, where the correct output is provided for each training example. 
# The model learns to map inputs to outputs based on this labeled data.
# E.g: Image Classification, Spam Detection

# *Unsupervised Learning:
# In this approach, the model is trained on unlabeled data, and it tries to find patterns or structures in the data without any explicit guidance on what the output should be.
# E.g: Clustering, Dimensionality Reduction

# *Semi-Supervised Learning:
# In this approach, the model is trained on a small amount of labeled data and a large amount of unlabeled data. 
# It combines the strengths of both supervised and unsupervised learning.
# E.g: Text Classification, Image Classification with Limited Labels

# *Reinforcement Learning:
# In this approach, the model learns by interacting with an environment and receiving feedback in the form of rewards or penalties. 
# The model aims to maximize cumulative rewards over time.
# E.g: Game Playing (e.g., AlphaGo), Robotics


# **Teachable Machine:
# Teachable Machine is a web-based tool that makes creating machine learning models fast, easy, and accessible to everyone.
# Train a computer to recognize your own images, sounds, & poses.
# A fast, easy way to create machine learning models for your sites, apps, and more – no expertise or coding required.

# Teachable Machine is a web-based tool developed by Google that allows users to create machine learning models without any coding experience. 
# It provides a simple interface for training models using their own data, such as images, sounds, or poses.
# Users can teach the model to recognize specific patterns or categories by providing examples, and the tool handles the underlying machine learning processes.
# E.g: Image Classification, Gesture Recognition

# Link: https://teachablemachine.withgoogle.com/
# https://teachablemachine.withgoogle.com/train?action=onboardOpen&id=DFBbSTvtpy4
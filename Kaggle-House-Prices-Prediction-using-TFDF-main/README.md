# Kaggle-House-Prices-Prediction-using-TFDF

## Competition Description
![alt text](https://github.com/Isdinval/Kaggle-House-Prices-Prediction-using-TFDF/blob/main/housesbanner.png?raw=true)

Ask a home buyer to describe their dream house, and they probably won't begin with the height of the basement ceiling or the proximity to an east-west railroad. But this playground competition's dataset proves that much more influences price negotiations than the number of bedrooms or a white-picket fence.
With 79 explanatory variables describing (almost) every aspect of residential homes in Ames, Iowa, this competition challenges you to predict the final price of each home.

## Practice Skills
+ Creative feature engineering 
+ Advanced regression techniques like random forest and gradient boosting

## Acknowledgments
The Ames Housing dataset was compiled by Dean De Cock for use in data science education. It's an incredible alternative for data scientists looking for a modernized and expanded version of the often cited Boston Housing dataset. 

Photo by Tom Thain on Unsplash.

## My WORK
it's a Python script that performs house price prediction using a stacked regression technique. It uses various machine learning models and feature engineering techniques to make predictions. Below is a summary of the steps and models used:

Step I: Data Preprocessing and Feature Engineering
The script starts by importing necessary libraries and loading the training and test datasets.
It analyzes and preprocesses the data to handle missing values and skewed features.
It transforms the target variable ('SalePrice') to make it more normally distributed.
It concatenates the train and test data for feature engineering.
It applies label encoding to certain categorical variables that contain ordinal information.
It adds a new feature 'TotalSF' which represents the total area of basement, first floor, and second floor of each house.
It transforms the highly skewed numerical features using Box Cox Transformation.
It creates dummy variables for categorical features.

Step II: Modelling
The script defines a cross-validation strategy using KFold.
It defines several base regression models:
Lasso Regression
Elastic Net Regression
Kernel Ridge Regression
Gradient Boosting Regression
XGBoost Regression
LightGBM Regression

Step III: Stacking Models
It creates a custom class AveragingModels to average the predictions from the base models.
It trains the stacked model on the training data using the averaged base models.
It makes predictions on the training data and the test data.

Step IV: Prediction and Submission
It converts the predictions back to the original scale by applying the inverse transformation on the target variable.
It saves the predictions to a CSV file in the required format for submission.

Feel free to explore the code and documentation provided here. If you have any questions or suggestions, please don't hesitate to reach out. Happy coding and happy predicting!

## Libraries used
Data Manipulation and Analysis:
numpy
pandas
scipy

Data Visualization:
matplotlib
seaborn

Machine Learning:
sklearn (scikit-learn)
xgboost
lightgbm

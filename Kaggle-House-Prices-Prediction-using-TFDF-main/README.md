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
### House Price Prediction - Data Preprocessing and Ensemble Modeling

#### Description:
This project demonstrates my expertise in data preprocessing, feature engineering, and ensemble modeling techniques for a house price prediction problem. The code showcases my ability to handle real-world datasets, perform data cleaning, and extract meaningful features. I have used various statistical techniques to analyze and handle outliers, as well as missing data. The feature engineering process involves transforming numerical features, creating new meaningful features, and encoding categorical variables.

To build an accurate predictive model, I have implemented several base regression models such as Lasso Regression, Elastic Net Regression, Kernel Ridge Regression, Gradient Boosting Regression, XGBoost Regression, and LightGBM Regression. Through cross-validation, I have evaluated each model's performance using the root mean squared error (RMSE) as the evaluation metric.

To further enhance predictive performance, I have employed a stacking technique to create an ensemble model. By combining the strengths of multiple base models, the stacked model achieves better accuracy and robustness in predicting house prices.

The final submission file contains the predicted sale prices for the test data. This project demonstrates my proficiency in data processing, modeling, and delivering actionable insights for real-world problems.

### House Price Prediction using Stacked Regression - Hyperparameter Optimization

#### Description:
This GitHub project showcases my expertise in house price prediction using stacked regression models with hyperparameter optimization. The code demonstrates my proficiency in data preprocessing, feature engineering, and advanced regression techniques to accurately predict house prices.

The project begins with data preprocessing, including handling missing values and outliers. Outliers in the target variable 'SalePrice' are removed to improve model performance. The target variable is then transformed using a logarithmic transformation to achieve a more normal distribution.

Feature engineering is a crucial aspect of this project. New features are created to capture important aspects of the data, such as the total area of the basement, first floor, and second floor of each house. Skewed numerical features are identified and transformed using the Box-Cox method to achieve better model performance.

Categorical features are appropriately handled by applying label encoding and converting some numerical variables into categorical ones, allowing the models to capture any meaningful order information.

The stacked regression models are built using Lasso Regression, Elastic Net Regression, and Kernel Ridge Regression. A Grid Search Cross-Validation is employed to optimize hyperparameters for each regression model. This ensures that the models are fine-tuned for maximum predictive accuracy.

The final submission file contains the predicted sale prices for the test data. The project showcases my skills in machine learning modeling, hyperparameter optimization, and delivering reliable predictions for real-world problems.

Overall, this project demonstrates my proficiency in data science, from data preprocessing and feature engineering to building powerful stacked regression models for accurate house price prediction. As a data science professional, I continuously seek to optimize and enhance predictive models to solve complex problems in the field of real estate and beyond.

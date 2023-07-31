# CODE1: Crab Age Prediction - Data Preprocessing and Feature Engineering
CODE1: Crab Age Prediction - Automated Machine Learning (AutoML) with FLAML

This Python code focuses on predicting the age of crabs using Automated Machine Learning (AutoML) techniques with the FLAML library. AutoML aims to automate the process of model selection and hyperparameter tuning, simplifying the model development workflow.

The code starts by importing necessary libraries for data manipulation and loads the dataset from CSV files. It then separates the features and target variable, 'Age,' for further processing. As the 'Sex' column is categorical, the code performs One-Hot Encoding to convert it into numerical format, enabling the model to understand the sex information.

To capture potential non-linear relationships in the data, the code creates additional features such as 'volume,' 'bmi' (Body Mass Index), and 'log_weight' (logarithm of weight). It also generates squared and cubed versions of certain features. These engineered features aim to enhance the model's ability to capture complex patterns in the data.

The code utilizes the FLAML library for Automated Machine Learning. FLAML automatically tunes hyperparameters for various regression models, including XGBoost, CatBoost, LightGBM, RandomForest, GradientBoosting, ElasticNet, Lasso, Ridge, and SVR. The final predictions are obtained using an ensemble of models, including a custom estimator called LADRegression.

The training and evaluation process with FLAML involve searching through various hyperparameter configurations for each model and selecting the best-performing model. FLAML optimizes the Mean Squared Error, which serves as the loss function for regression tasks, to find the best model.

Once the best model is obtained, it is used to predict the age of crabs from the test dataset, and the results are saved in a CSV file named 'submission.csv' for submission to the competition.
# CODE2: Crab Age Prediction - LSTM-based Deep Learning Model
This Python code focuses on predicting the age of crabs using an LSTM-based Deep Learning model. Similar to CODE1, the data is preprocessed to convert categorical variables using One-Hot Encoding and perform train-test splitting.

The feature engineering step creates new features like 'volume,' 'dim1,' 'dim2,' 'dim3,' 'total_weight,' 'weight_volume_ratio,' and others, aiming to capture essential patterns in the data. These features enable the model to better understand the relationships between crab biometric measurements and their ages.

The Deep Learning model architecture comprises LSTM layers, which are well-suited for sequence data like time series or sequential measurements. The model is built using the Keras library, with dense layers, ReLU activation, and dropout layers to prevent overfitting.

The training and evaluation process involve training the LSTM model on the training set and evaluating its performance on the validation set. The model's goal is to minimize the mean squared error between predicted and actual crab ages.

Once the model is trained, it is used to predict the age of crabs from the test dataset. The predicted ages are saved in a CSV file named 'submission.csv' for submission to the competition.

# CODE3: Crab Age Prediction - Data Synthesis with GReaT
This Python code showcases the process of data synthesis using the GReaT (Generative Reinforcement Learning for Text) library for predicting crab ages. GReaT is a powerful tool for generating synthetic data based on a pre-trained GPT-2 language model fine-tuned for the crab age prediction task.

The code starts by loading the pre-trained GPT-2 model, followed by generating synthetic data samples. GReaT allows controlling various parameters like temperature and sequence length to influence the diversity and randomness of the generated data.

The generated synthetic data is saved in a CSV file named 'synthetic_data.csv.' This data augmentation technique can be used to expand the original dataset, enhancing model training and evaluation.

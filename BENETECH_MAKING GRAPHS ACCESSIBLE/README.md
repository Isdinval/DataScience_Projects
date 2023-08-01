# CODE 1 : Tuned Donut
using a vision encoder-decoder model, specifically a "Donut" model, to generate predictions for chart data from images. The goal is to identify chart types (e.g., line chart, bar chart) and extract data points from the images.

Here's a breakdown of the code:

* Importing necessary libraries and packages.
* Defining a configuration class CFG that holds various hyperparameters and paths to data.
* Defining tokens for the start and end of X-axis and Y-axis data points.
* Cleaning functions to remove unwanted characters from the prediction strings.
* A function to convert the prediction string into chart type, X-axis data, and Y-axis data.
* Loading image files and creating a dataset from them.
* Preprocessing function to convert images into pixel values for the model.
* Loading the pre-trained VisionEncoderDecoderModel and setting it to evaluation mode.
* Generating predictions for each image in the dataset and converting the predictions into chart types and data series.
* Saving the predictions in a DataFrame and exporting it to a CSV file.

# CODE 2: Donut-train
This code appears to be an implementation of an end-to-end image-to-text model called "Donut" (Document Understanding Transformer) for the task of generating text based on images without the need for OCR. The model architecture combines a Swin encoder and a BART (Bidirectional and Auto-Regressive Transformers) decoder.

Here's an overview of the different parts of the code:

* Importing libraries and installing required packages.
* Defining a configuration class CFG to set various hyperparameters and settings.
* Defining utility functions to process JSON annotations and create the dataset.
* Preprocessing the data to convert annotations into a format that the model can work with.
* Configuring the model with the required image height, width, and maximum sequence length to generate.
* Checking the tokenizer for unknown tokens and adding necessary tokens to handle them.
* Preprocessing function to get pixel values and input IDs for the model.
* Creating train and validation datasets by splitting the data into folds.
* Defining a custom collate function for DataLoader to handle variable-length sequences in a batch.
* Creating DataLoaders for training and validation.
* Implementing evaluation metrics such as RMSE (Root Mean Square Error), normalized RMSE, and normalized Levenshtein score.
* Creating a PyTorch Lightning module for the Donut model and defining training and validation steps.

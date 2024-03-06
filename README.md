# Bike_Sharing_Rental_Project

# Overview
This repository contains code for analyzing and preparing the "bike_rent.csv" dataset. The code performs various data collection, cleaning, visualization, and feature selection tasks using the Python programming language and the pandas, numpy, seaborn, and scikit-learn libraries.

This project aims to develop a predictive model to forecast the bike rental count based on various features such as date, weather conditions, and time of the day. The project utilizes hour datasets." The "day" dataset contains daily aggregated bike rental information, while the "hour" dataset provides hourly details. Dataset Description Day Dataset


# Getting Started
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# To run the project locally, please ensure you have the following dependencies installed:

- Python 3.7 or higher
- NumPy
- Pandas
- Seaborn
- Scikit-learn
- Matplotlib
- Jupyter Notebook
- ipykernel
- streamlit

Clone the repository to your local machine or download the code files.
Ensure that you have Python 3.x installed on your system.
Install the required libraries by running pip install pandas numpy seaborn scikit-learn in your command line or terminal.
Place the "bike_rent.csv" file in the same directory as the code files.

# Code Overview
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
The code performs the following tasks:

1. Reads the "bike_rent.csv" file using pandas and displays the dataset.
2. Converts the data types of certain columns to categorical and datetime.
3. Handles missing values by replacing them with the mean or mode depending on the column type.
4. Visualizes the distribution of the bike rental counts using histograms.
5. Performs data transformations to address right-skewness in the rental counts.
6. Visualizes the relationships between various weather conditions and the rental counts using scatter plots.
7. Analyzes the monthly distribution of rentals by weekdays and seasons.
8. Analyzes the yearly distribution of rentals.
9. Analyzes the distribution of rentals on working days and holidays.
10. Analyzes the distribution of rentals based on different weather conditions.
11. Detects outliers in the dataset using box plots.
12. Replaces outliers using the capping method.
13. Computes the correlation matrix and visualizes it using a heatmap.
14. Performs feature selection using recursive feature elimination, univariate feature selection, tree-based feature selection, and L1 regularization.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Usage
Launch VSCODE
Open the Model Training.ipynb notebook.
Run the cells in the notebook to execute the code and see the results.
Feel free to modify the code or experiment with different models and parameters.
Results
The results of the bike sharing demand prediction are evaluated based on various metrics such as mean absolute error (MAE), root mean squared error (RMSE), and R-squared score. These metrics provide insights into the performance of the model and how well it predicts bike sharing demand.

# Model Building and Selection
To predict the bike rental count, several machine learning models were implemented and evaluated. The following algorithms were utilized:

- Linear Regression
- Random Forest
- Extra Trees Regressor
- LightGBM
- XGBoost
- Decision Tree
  
After training and evaluating these models, XGBoost was chosen as the final model due to its superior performance in terms of accuracy and predictive power. Model Deployment

The selected XGBoost model was deployed using Streamlit, a Python library for building interactive web applications. The deployment allows users to input the relevant features such as date, weather conditions, and time, and obtain the predicted bike rental count as the output.

Deployment Link- 

# Conclusion
This code provides a comprehensive analysis of the "bike_rent.csv" dataset, including data cleaning, visualization, and feature selection. It aims to gain insights into the factors influencing bike rentals and identify the most relevant features for prediction models. Feel free to explore and modify the code to suit your specific requirements.

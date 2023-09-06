# Bike_Sharing_Rental_Project

Bike-rental-analysis
This repository contains code for analyzing and preparing the "bike_rent.csv" dataset. The code performs various data collection, cleaning, visualization, and feature selection tasks using the Python programming language and the pandas, numpy, seaborn, and scikit-learn libraries.

# Getting Started
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
To use this code, follow the steps below:

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
# Conclusion
This code provides a comprehensive analysis of the "bike_rent.csv" dataset, including data cleaning, visualization, and feature selection. It aims to gain insights into the factors influencing bike rentals and identify the most relevant features for prediction models. Feel free to explore and modify the code to suit your specific requirements.

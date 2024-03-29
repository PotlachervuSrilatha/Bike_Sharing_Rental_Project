
"""Pipeline.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hXrjteTlV6iBLPij4AKbOq7KUgtV7Sb5
"""

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline, make_pipeline
from xgboost import XGBRegressor

import pandas as pd
import numpy as np
data = pd.read_csv('/content/bike_rent.csv')
data.head()

data = data.replace('?', np.nan)

# Preprocess the 'dteday' column to convert it to datetime
data['dteday'] = pd.to_datetime(data['dteday'])

# Separate the 'dteday' column from the rest of the data
data_transform = data.drop('dteday', axis=1)
dteday_data = np.array(data['dteday']).reshape(-1, 1)

# Encode the categorical columns
categorical_columns = ['season', 'yr', 'mnth', 'hr', 'holiday', 'weekday', 'workingday', 'weathersit']
encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')
encoded_data = encoder.fit_transform(data_transform[categorical_columns])

encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(categorical_columns))

# Concatenate the encoded data with the remaining numeric columns
numeric_columns = ['temp', 'atemp', 'hum', 'windspeed', 'casual', 'registered', 'cnt']
numeric_data = data_transform[numeric_columns]
final_data_transformed = pd.concat([encoded_df, numeric_data], axis=1)

# Modify the transformer as per your dataset columns and indices
transformer = ColumnTransformer(transformers=[
    ('scaler', StandardScaler(), slice(len(categorical_columns), None))
], remainder='passthrough')

# Modify the transformer as per your dataset columns and indices
transformer = ColumnTransformer(transformers=[
    ('tnf1', OneHotEncoder(sparse=False, handle_unknown='ignore'), [2, 4, 5, 6, 7, 8, 9]),
    ('tnf2', StandardScaler(), [0, 1, 3, 10, 11, 12, 13, 14, 15])
], remainder='passthrough')

# Apply the ColumnTransformer to the data
transformed_data = transformer.fit_transform(final_data_transformed)

final_data = np.concatenate((dteday_data, transformed_data), axis=1)

from sklearn.model_selection import train_test_split

# Split the data into train and test sets
xtrain, xtest, ytrain, ytest = train_test_split(final_data, data['cnt'], test_size=0.2, random_state=1)

# Create the pipeline model
model = Pipeline(steps=[
    ('transformer', transformer),
    ('model', XGBRegressor())
])

# Fit the pipeline model
model.fit(xtrain, ytrain)

ypred = model.predict(xtest)

ypred

import pickle

pickle.dump(model, open('model.pkl','wb'))


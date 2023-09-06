import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

pickle_in = open("final_model.sav", 'rb')
reg = pickle.load(pickle_in)

def preprocess_data(data):
    encoder = LabelEncoder()
    data['season'] = encoder.fit_transform(data['season'])
    data['workingday'] = encoder.fit_transform(data['workingday'])
    return data

def predict(input_df):
    preprocessed_data = preprocess_data(input_df)
    preprocessed_data['hr'] = 0
    preprocessed_data['year'] = 0
    preprocessed_data['month'] = 0
    preprocessed_data['day'] = 0
    predictions = reg.predict(preprocessed_data)
    return predictions

def main():
    st.title("Bike Rental Calculation App")
    st.sidebar.header("Input Features")

    season = st.sidebar.selectbox("Season", ("spring", "summer", "fall", "winter"))
    mnth = st.sidebar.selectbox("Month", (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    weekday = st.sidebar.selectbox("Weekday", (0, 1, 2, 3, 4, 5, 6))
    workingday = st.sidebar.selectbox("Workingday", ("No", "Yes"))
    temp = st.sidebar.slider("Temperature", 0.0, 1.0, 0.5)
    hum = st.sidebar.slider("Humidity", 0.0, 1.0, 0.5)
    casual = st.sidebar.selectbox("Casual", range(0, 100,5))  
    registered = st.sidebar.selectbox("Registered", range(0, 100,5))  
    input_data = pd.DataFrame({
        'season': [season],
        'mnth': [mnth],
        'weekday': [weekday],
        'workingday': [workingday],
        'temp': [temp],
        'atemp': [temp],
        'hum': [hum],
        'casual': [casual],
        'registered': [registered]
    }, columns=['season', 'mnth', 'hr', 'weekday', 'workingday', 'temp', 'atemp', 'hum', 'casual', 'registered'])

    if st.button("Predict"):
        predictions = predict(input_data)
        st.success(f"The predicted bike rentals count is {int(predictions[0])}")

if __name__ == "__main__":
    main()

import streamlit as st
import pandas as pd
import numpy as np
import math
from PIL import Image
## from pipeline import full_pipeline
import pickle

with open("model.pkl", 'rb') as file:
    model = pickle.load(file)

st.title('ML Model')
st.write('Determine if your air quality is dangerously smoky!')

@st.cache
def load_data(file):
    data = pd.read_csv(file)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

DATA = 'smoke_detection_iot.csv'
data = load_data(DATA)

max_temp = int(data["temperature[c]"].max())
min_temp = 0
temp = st.sidebar.slider("Temperature", min_temp, max_temp, int((min_temp+max_temp)/2))


max_humidity = int(data["humidity[%]"].max())
min_humidity = 0
humidity = st.sidebar.slider("Humidity", min_humidity, max_humidity, int((min_humidity+max_humidity)/2))

max_tvoc = int(data["tvoc[ppb]"].max())
min_tvoc = 0
tvoc = st.sidebar.slider("tvoc", min_tvoc, max_tvoc, int((min_tvoc+max_tvoc/2)))

max_ECO2 = int(data["eco2[ppm]"].max())
min_ECO2 = 0
ECO2 = st.sidebar.slider("eco2", min_ECO2, max_ECO2, int((min_ECO2+max_ECO2)/2))

max_RAW_H2  = int(data["raw h2"].max())
min_RAW_H2 = 0
RAW_H2 = st.sidebar.slider("raw h2", min_RAW_H2, max_RAW_H2, int((min_RAW_H2+max_RAW_H2)/2))

max_ETHANOL = int(data["raw ethanol"].max())
min_ETHANOL = 0
ETHANOL = st.sidebar.slider("ethanol", min_ETHANOL, max_ETHANOL, int((min_ETHANOL+max_ETHANOL)/2))

max_PRESSURE = int(data["pressure[hpa]"].max())
min_PRESSURE = 0
PRESSURE = st.sidebar.slider("pressure", min_PRESSURE, max_PRESSURE, int((min_PRESSURE+max_PRESSURE)/2))

max_PM1 = int(data["pm1.0"].max())
min_PM1 = 0
PM1 = st.sidebar.slider("PM1.0", min_PM1, max_PM1, int((min_PM1+max_PM1)/2))

max_PM25 = int(data["pm2.5"].max())
min_PM25 = 0
PM25 = st.sidebar.slider("PM2.5", min_PM25, max_PM25, int((min_PM25+max_PM25)/2))

max_NC05 = int(data["nc0.5"].max())
min_NC05 = 0
NC05 = st.sidebar.slider("NC0.5", min_NC05, max_NC05, int((min_NC05+max_NC05)/2))

max_NC1 = int(data["nc1.0"].max())
min_NC1 = 0
NC1 = st.sidebar.slider("NC1.0", min_NC1, max_NC1, int((min_NC1+max_NC1)/2))

max_NC25 = int(data["nc2.5"].max())
min_NC25 = 0
NC25 = st.sidebar.slider("NC2.5", min_NC25, max_NC25, int((min_NC25+max_NC25)/2))

max_CNT = int(data["cnt"].max())
min_CNT = 0
cnt = st.sidebar.slider("CNT", min_CNT, max_CNT, int((min_CNT+max_CNT)/2))

user_data = pd.DataFrame(np.array([["0", 1654733331, temp, humidity, tvoc, ECO2, RAW_H2, ETHANOL, PRESSURE, PM1, PM25, NC05, NC1, NC25, cnt]]),
columns = ["", "UTC", "Temperature[C]", "Humidity[%]", "TVOC[ppb]", "eCO2[ppm]", "Raw H2", "Raw Ethanol", "Pressure[hPa]", "PM1.0", "PM2.5", "NC0.5", "NC1.0", "NC2.5", "CNT"])
st.subheader("User input:")
st.write(user_data)

submit = st.button("Submit")

user_input_prepared = pd.DataFrame(user_data, columns =["", "UTC", "Temperature[C]", "Humidity[%]", "TVOC[ppb]", "eCO2[ppm]", "Raw H2", "Raw Ethanol", "Pressure[hPa]", "PM1.0", "PM2.5", "NC0.5", "NC1.0", "NC2.5", "CNT"])
## user_input_prepared = full_pipeline.transform(user_input_prepared)
user_prediction = model.predict(X=user_input_prepared)
user_prediction = 0

if submit:
    if user_prediction == 0:
        result = "SAFE"
    else:
        result = "UNSAFE"

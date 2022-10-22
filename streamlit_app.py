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

max_temp = int(data["Temperature"].max())
min_temp = 0
temp = st.sidebar.slider("Temperature", int((min_temp+max_temp)/2))
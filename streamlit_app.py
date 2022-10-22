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
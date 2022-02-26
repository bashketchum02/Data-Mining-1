from re import S
import pandas as pd
import streamlit as st
import numpy as np
dataframe = pd.read_csv('q1.csv')

def app():
    st.write("### 4. How many patients required intubation?")

    filter = dataframe['INTUBATED'] == 'YES'
    st.write("Number of patients that required in intubation is : ", dataframe[filter].shape[0])
import imp
from re import S
import pandas as pd
import streamlit as st
import numpy as np

def app():
    st.write("### 8. Provide a chart to show the top-20 features in descending order.")
    
    st.write('Following is the top 20 features using BorutaPy')
    st.dataframe(pd.read_csv('Boruta_Top20.csv'))
    st.image('Q8_boruta.png')
    
    st.write('Following is the top 20 features using RFE')
    st.dataframe(pd.read_csv('RFE_Top20.csv'))
    st.image('Q8_rfe.png')
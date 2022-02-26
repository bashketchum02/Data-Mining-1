from re import S
import pandas as pd
import streamlit as st
import numpy as np

def app():
    ## Question 1
    st.write('### 1. Refer to data_dictionary.csv and map the attributes values accordingly.')
    st.write('Below is the Dataframe with mapped attributes according to the data_dictionary.csv')

    dataframe = pd.read_csv('q1.csv')
    st.dataframe(dataframe)
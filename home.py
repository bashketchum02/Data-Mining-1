from re import S
import pandas as pd
import streamlit as st
import numpy as np

def app():
    st.title("A comprehensive study of Covid 19 cases")

    df1 = pd.read_csv('dataset.csv')

    st.write("The Dataset we're working with")
    #showing our initial dataframe here
    st.dataframe(df1)

    st.write('## Questions and answers')
    st.write("Please use the navigation bar to navigate between questions!")
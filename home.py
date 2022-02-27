from re import S
import pandas as pd
import streamlit as st
import numpy as np

def app():
    st.title("A comprehensive study of Covid 19 cases")
    st.image("covid19.jpg")
    st.write("**Prepared By** - *(Tee Eng Leong, 1191201404), (Anirban Bala Pranto, 1181202317)*")

    st.write("This application is made for analysis and classification of COVID 19 cases. The application has been developed as an assignment for **Data Mining (TDS 3301)** class at **Multimedia University, Cyberjaya**")

    df1 = pd.read_csv('dataset.csv')

    st.write("The Dataset we're working with")
    #showing our initial dataframe here
    st.dataframe(df1)

    st.table()

    st.write('## Questions and answers')
    st.write("Please use the navigation bar to navigate between questions!")
from re import S
import pandas as pd
import streamlit as st
import numpy as np

def app():
    st.write("### 9. Based on the Top-20 features in Question 8, construct a chart to show the accuracy for top-n features. Start with Top-5, then Top-6, Top-7 etc.")
    boruta = pd.read_csv('Boruta_Top20.csv')
    rfe = pd.read_csv('RFE_Top20.csv')
    
    st.write("Boruta")
    st.write('Following is the top 20 features using BorutaPy')
    st.dataframe(boruta['Features'])
    st.write('Following is the top n features accuracy using BorutaPy')
    st.dataframe(pd.read_csv('Boruta_Accuracy.csv'))
    st.image('Q9_boruta.png')

    st.write("RFE")
    st.write('Following is the top 20 features using RFE')
    st.dataframe(rfe['Features'])
    st.write('Following is the top n features accuracy using RFE')
    st.dataframe(pd.read_csv('RFE_Accuracy.csv'))
    st.image('Q9_boruta.png')
    st.image('Q9_rfe.png')
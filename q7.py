import imp
from re import S
import pandas as pd
import streamlit as st
import numpy as np

def app():
    st.write('### 7. Use the BORUTA and RFE packages to find the importance scores for each independent variables with respect to ICU.')

    st.write('We get the following dataframe after following all the label encoding and data cleaning instructions given.')

    dataframe = pd.read_csv('cleaned.csv')

    st.dataframe(dataframe)

    st.write('Following is the importance score of each variable with respect to ICU, using BorutaPy')
    st.dataframe(pd.read_csv('Boruta_Score.csv'))

    st.write('Following is the importance score of each variable with respect to ICU, using RFE')
    st.dataframe(pd.read_csv('RFE_Scores.csv'))


from re import S
import pandas as pd
import streamlit as st
import numpy as np
def app():
    df1 = pd.read_csv('dataset.csv')

    st.write("### 5. What are the correlations between diseases and ICU admission?")
    diseases_and_ICU = list(['DIABETES', 'COPD', 'ASTHMA', 'INMUSUPR', 'HYPERTENSION', 'OTHER_DISEASE', 'ICU'])
    corr_disease = df1[diseases_and_ICU].corr()

    st.write('Here is the correlation that we could find between diseases and ICU admission, it was apparent that there were no significant correlation between the diseases and ICU admission.')
    st.dataframe(corr_disease)

    st.write('We also plotted the following heatmap of the correlation Matrix')
    st.image('Q5_heatmap.png')
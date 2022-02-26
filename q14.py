from re import S
import pandas as pd
import streamlit as st
import numpy as np

def app():
    st.write("### 14. SMOTE the data you prepared in Question 7. Repeat steps in Question 10, 11, 12. Compare the models’ performances with and without SMOTE by using a table and a chart.")
    
    st.image('Q14_nb_roc.png')
    st.image('Q14_rfe_roc.png')
    st.image('Q14_knn_roc.png')
    st.image('Q14_overall_roc.png')
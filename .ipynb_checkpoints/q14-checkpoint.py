from re import S
import pandas as pd
import streamlit as st
import numpy as np

def app():
    st.write("### 14. SMOTE the data you prepared in Question 7. Repeat steps in Question 10, 11, 12. Compare the models’ performances with and without SMOTE by using a table and a chart.")
    
    st.write("### Naive Bayes Classifier")
    st.write('Following is the Classification Report for Naive Bayes Classifier without SMOTE')
    st.dataframe(pd.read_csv('NB_Report.csv', index_col=0))
    st.write('Following is the Classification Report for Naive Bayes Classifier with SMOTE')
    st.dataframe(pd.read_csv('SMOTE_NB_Report.csv', index_col=0))
    st.write('Following is the ROC curve for Naive Bayes Classifier with SMOTE')
    st.image('Q14_nb_roc.png')
    
    st.write("### Random Forest Model")
    st.write('Following is the Classification Report for Random Forest Model without SMOTE')
    st.dataframe(pd.read_csv('RF_Report.csv', index_col=0))
    st.write('Following is the Classification Report for Random Forest Model with SMOTE')
    st.dataframe(pd.read_csv('SMOTE_RF_Report.csv', index_col=0))
    st.write('Following is the ROC curve for Random Forest Model with SMOTE')
    st.image('Q14_rfe_roc.png')
    
    st.write("### K-Nearest Neighbour Model")
    st.write('Following is the Classification Report for K-Nearest Neighbour Model without SMOTE')
    st.dataframe(pd.read_csv('KNN_Report.csv', index_col=0))
    st.write('Following is the Classification Report for K-Nearest Neighbour Model with SMOTE')
    st.dataframe(pd.read_csv('SMOTE_KNN_Report.csv', index_col=0))
    st.write('Following is the ROC curve for K-Nearest Neighbour Model with SMOTE')
    st.image('Q14_knn_roc.png')
    
    st.write("### Overall Performance")
    st.write('Following is the comparison of ROC curve for all the models with and without SMOTE')
    st.image('Q14_overall_roc.png')
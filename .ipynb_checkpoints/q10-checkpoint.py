from re import S
import pandas as pd
import streamlit as st
import numpy as np

def app():
    st.write("### 10. Create a Naïve Bayes Classifier. Provide the following info:\n- Overall accuracy\n- AUC\n- Confusion matrix with TP, TN, FP, FN\nNote: in Streamlit, you should demo how hyper-parameters tuning could influence the accuracy of the model.")
    
    
    accuracy = open("Q10_Accuracy.txt")
    lines = accuracy.readlines()
    for line in lines:
        st.write(line)
        
    accuracy.close()
    
    confusion = open("Q10_Confusion_Matrix.txt")
    lines = confusion.readlines()
    for line in lines:
        st.write(line)
        
    confusion.close()
    
    auc = open("Q10_AUC.txt")
    lines = auc.readlines()
    for line in lines:
        st.write(line)
        
    auc.close()
    st.image('Q10_roc.png')
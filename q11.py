from re import S
import pandas as pd
import streamlit as st
import numpy as np

def app():
    st.write("### 11. Create a Random Forest model. Provide the following info:\n- Overall accuracy\n- AUC\n- Confusion matrix with TP, TN, FP, FN\nNote: in Streamlit, you should demo how hyper-parameters tuning could influence the accuracy of the model.")
    st.image('Q11_roc.png')

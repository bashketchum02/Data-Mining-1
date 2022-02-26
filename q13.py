from re import S
import pandas as pd
import streamlit as st
import numpy as np

def app():
    st.write("### 13. Compare the models you created in Question 10, 11, 12 using ROC.")
    st.write('Following is the comparison of ROC Curves created in Question 10, 11, 12')
    st.image('Q13_roc.png')
from re import S
import pandas as pd
import streamlit as st
import numpy as np

import q1
import q2
import q3
import q4
import q5
import q6
import q7
import q8
import q9
import q10
import q11
import q12
import q13
import q14
import home

st.set_page_config(page_title='A Covid 19 Story', page_icon=None, layout="wide",
                    initial_sidebar_state="auto", menu_items=None)
PAGES = {
    "Home" : home,
    "Question 1": q1,
    "Question 2": q2,
    "Question 3": q3,
    "Question 4": q4,
    "Question 5": q5,
    "Question 6": q6,
    "Question 7": q7,
    "Question 8": q8,
    "Question 9": q9,
    "Question 10": q10,
    "Question 11": q11,
    "Question 12": q12,
    "Question 13": q13,
    "Question 14": q14
}
st.sidebar.title('Introduction and Questions')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()










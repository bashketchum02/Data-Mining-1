import pandas as pd
import streamlit as st
import numpy as np

dataframe = pd.read_csv('dataset.csv')

st.set_page_config(page_title='Covid 19 in Mexico', page_icon=None, layout="wide",
                   initial_sidebar_state="auto", menu_items=None)

st.title("A comprehensive study of Covid 19 cases in Mexico")

st.write("The Dataset we're working with")
#showing our initial dataframe here
dataframe

st.write('## Questions and answers')

## Question 1
st.write('### 1. Refer to data_dictionary.csv and map the attributes values accordingly.')
st.write('Below is the Dataframe with mapped attributes according to the data_dictionary.csv')

q1 = pd.read_csv('q1.csv')
q1
##Question 2


import pandas as pd
import streamlit as st
import numpy as np

dataframe = pd.read_csv('dataset.csv')

st.set_page_config(page_title='Covid 19 in Malaysia', page_icon=None, layout="wide",
                   initial_sidebar_state="auto", menu_items=None)

st.title("A comprehensive study of Covid 19 cases in Malaysia")

st.write("The Dataset we're working with")
#showing our initial dataframe here
dataframe

st.write('## Questions and answers')

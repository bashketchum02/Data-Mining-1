from re import S
import pandas as pd
import streamlit as st
import numpy as np

def app():
    st.write('### 3. What is the distribution of cases by gender and age group?')

    bins = [0,10,20,30,40,50,60,70,80,90,100]
    dataframe = pd.read_csv('q1.csv')
    group = dataframe.groupby(['SEX',pd.cut(dataframe.AGE, bins)])
    st.dataframe(group.size().unstack())
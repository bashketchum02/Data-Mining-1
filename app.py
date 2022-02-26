import pandas as pd
import streamlit as st
import numpy as np

dataframe = pd.read_csv('dataset.csv')

st.set_page_config(page_title='Covid 19 in Mexico', page_icon=None, layout="wide",
                   initial_sidebar_state="auto", menu_items=None)

st.title("A comprehensive study of Covid 19 cases")

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

st.write("### 2. Create a chart for AGE using the bin information below: [0,10,20,30,40,50,60,70,80,90,100]")

st.image('Q2_histogram.png')

st.write('### 3. What is the distribution of cases by gender and age group?')

bins = [0,10,20,30,40,50,60,70,80,90,100]

group = dataframe.groupby(['SEX',pd.cut(dataframe.AGE, bins)])
st.dataframe(group.size().unstack())

st.write("### 4. How many patients required intubation?")




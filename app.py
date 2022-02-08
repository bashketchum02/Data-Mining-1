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

df = pd.read_excel('data_dictionary.xlsx')
dictionary = df.set_index('variable').T.to_dict()

for key, value in dictionary.items():
    for i in value.values():
        res = dict(item.split("=") for item in i.split(", "))
        dictionary[key] = res

dictionary = {outer_k.upper(): {inner_k.replace(' ', ''): inner_v for inner_k, inner_v in outer_v.items()} for outer_k, outer_v in dictionary.items()}

for key, value in dictionary.items():
    dataframe[key]= dataframe[key].astype(str)
    dataframe.replace({key: dictionary[key]}, inplace=True)

st.write('### 1. Refer to data_dictionary.csv and map the attributes values accordingly.')
st.write('Below is the Dataframe with mapped attributes according to the data_dictionary.csv')
st.write(dataframe)

##Question 2


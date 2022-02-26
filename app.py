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

st.write("### 8. Provide a chart to show the top-20 features in descending order.")
st.image('Q8_boruta.png')
st.image('Q8_rfe.png')

st.write("### 9. Based on the Top-20 features in Question 8, construct a chart to show the accuracy for top-n features. Start with Top-5, then Top-6, Top-7 etc.")
st.write("Boruta Top 20 Features: 'TREATMENT_LOCATION', 'INTUBATED_NO', 'PNEUMONIA_NO', 'SECTOR_SSA', 'SECTOR_SEMAR', 'PNEUMONIA_YES', 'SECTOR_PRIVATE', 'ADMISSION_MONTH_04', 'ANOTHER CASE_YES', 'ANOTHER CASE_UNKNOWN', 'SECTOR_ISSSTE', 'SECTOR_IMSS', 'ANOTHER CASE_NO', 'PATIENT_LOCATION', 'ORIGIN_USMER', 'ORIGIN_OUTSIDE USMER', 'AGE', 'INTUBATED_YES', 'ADMISSION_MONTH_06', 'OBESITY_YES'")
st.write("Top  5 features :  0.9220170038111991\nTop  6 features :  0.9220170038111991\nTop  7 features :  0.9234828496042217\nTop  8 features :  0.9205511580181764\nTop  9 features :  0.9234828496042217\nTop  10 features :  0.9201602658067038\nTop  11 features :  0.9189875891722857\nTop  12 features :  0.9170331281149223\nTop  13 features :  0.9164467897977133\nTop  14 features :  0.9155672823218998\nTop  15 features :  0.9155672823218998\nTop  16 features :  0.918010358643604\nTop  17 features :  0.9179126355907359\nTop  18 features :  0.9244600801329034\nTop  19 features :  0.9247532492915078\nTop  20 features :  0.924264634027167\n")
st.image('Q9_boruta.png')

st.write("'INTUBATED_YES', 'SECTOR_IMSS', 'INTUBATED_NO', 'TREATMENT_LOCATION', 'PATIENT_LOCATION', 'ANOTHER CASE_UNKNOWN', 'PNEUMONIA_NO', 'SECTOR_SSA', 'AGE', 'PNEUMONIA_YES', 'ANOTHER CASE_NO', 'SECTOR_PRIVATE', 'SECTOR_ISSSTE', 'ORIGIN_USMER', 'ORIGIN_OUTSIDE USMER', 'ADMISSION_MONTH_04', 'ANOTHER CASE_YES', 'SECTOR_SEDENA', 'SECTOR_STATE', 'ADMISSION_MONTH_06'")
st.write("Top  5 features :  0.9221147268640673\nTop  6 features :  0.92250561907554\nTop  7 features :  0.9207466041239128\nTop  8 features :  0.9210397732825173\nTop  9 features :  0.9217238346525946\nTop  10 features :  0.9221147268640673\nTop  11 features :  0.9211374963353856\nTop  12 features :  0.9220170038111991\nTop  13 features :  0.9260236489787941\nTop  14 features :  0.9241669109742988\nTop  15 features :  0.9244600801329034\nTop  16 features :  0.9250464184501124\nTop  17 features :  0.9247532492915078\nTop  18 features :  0.9241669109742988\nTop  19 features :  0.9253395876087169\nTop  20 features :  0.924264634027167\n")
st.image('Q9_boruta.png')
st.image('Q9_rfe.png')

st.write("### 10. Create a Naïve Bayes Classifier. Provide the following info:\n- Overall accuracy\n- AUC\n- Confusion matrix with TP, TN, FP, FN\nNote: in Streamlit, you should demo how hyper-parameters tuning could influence the accuracy of the model.")
st.image('Q10_roc.png')

st.write("### 11. Create a Random Forest model. Provide the following info:\n- Overall accuracy\n- AUC\n- Confusion matrix with TP, TN, FP, FN\nNote: in Streamlit, you should demo how hyper-parameters tuning could influence the accuracy of the model.")
st.image('Q11_roc.png')

st.write("### 12. Create a K-Nearest Neighbour model. Provide the following info:\n- Overall accuracy\n- AUC\n- Confusion matrix with TP, TN, FP, FN\nNote: in Streamlit, you should demo how hyper-parameters tuning could influence the accuracy of the model.")
st.image('Q12_roc.png')

st.write("### 13. Compare the models you created in Question 10, 11, 12 using ROC.")
st.image('Q13_roc.png')

st.write("### 14. SMOTE the data you prepared in Question 7. Repeat steps in Question 10, 11, 12. Compare the models’ performances with and without SMOTE by using a table and a chart.")
st.image('Q14_nb_roc.png')
st.image('Q14_rfe_roc.png')
st.image('Q14_knn_roc.png')
st.image('Q14_overall_roc.png')
import imp
from re import S
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.metrics import precision_recall_curve



def app():
    st.write("### Create a Naive Bayes Classifier.")
    
    df1 = pd.read_csv('cleaned.csv', index_col=0)

    y = df1.ICU
    X = df1.drop("ICU", 1)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
    st.write("Hyper-parameters tuning won't improve Naive Bayes performance.")
    st.warning("It may take some time to train the model :) Please patiently wait!")
    nb = GaussianNB()
    nb.fit(X_train, y_train)
    y_pred = nb.predict(X_test)

    st.write("#### Results : ")
    st.write("Accuracy on training set: {:.3f}".format(nb.score(X_train, y_train)))
    st.write("Accuracy on test set: {:.3f}".format(nb.score(X_test, y_test)))

    #Confusion Matrix
    confusion_majority = confusion_matrix(y_test, y_pred)

    st.write('Mjority classifier Confusion Matrix\n', confusion_majority)

    st.write('**********************')
    st.write('Mjority TN= ', confusion_majority[0][0])
    st.write('Mjority FP=', confusion_majority[0][1])
    st.write('Mjority FN= ', confusion_majority[1][0])
    st.write('Mjority TP= ', confusion_majority[1][1])
    st.write('**********************')

    st.write('Precision= {:.2f}'.format(precision_score(y_test, y_pred)))
    st.write('Recall= {:.2f}'. format(recall_score(y_test, y_pred)))
    st.write('F1= {:.2f}'. format(f1_score(y_test, y_pred)))
    st.write('Accuracy= {:.2f}'. format(accuracy_score(y_test, y_pred)))

    #AUC
    prob_NB = nb.predict_proba(X_test)
    prob_NB = prob_NB[:, 1]

    auc_NB= roc_auc_score(y_test, prob_NB)
    st.write('AUC: %.2f' % auc_NB)

    fpr_NB, tpr_NB, thresholds_NB = roc_curve(y_test, prob_NB) 

    plt.plot(fpr_NB, tpr_NB, color='orange', label='NB') 
    plt.plot([0, 1], [0, 1], color='green', linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.savefig('NB_ROC.png')

    st.image('NB_ROC.png')

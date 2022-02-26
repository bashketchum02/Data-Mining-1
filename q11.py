import imp
from re import S
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.metrics import precision_recall_curve

df1 = pd.read_csv('cleaned.csv')

y = df1.ICU
X = df1.drop("ICU", 1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

def app():
    st.write("### Create a Random Forest model.")
    st.write("#### Please select Number of Estimators and Max Depth for your Random Forest Model : ")
    n_estimator = st.slider('Number of estimators for Random Forest (n_estimators)', 0, 1000, (100,200), 100)
    max_depth = st.slider('Max depth : ', 0, 20, (5,20), 5)
    #st.write(n_estimator[1])

    st.warning("It may take some time to train the model :) Please patiently wait!")
    rf = RandomForestClassifier(random_state=1, n_estimators=n_estimator[1], max_depth=max_depth[1])
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_test)

    st.write("#### Results of the selected hyperparameters : ")
    st.write("Accuracy on training set: {:.3f}".format(rf.score(X_train, y_train)))
    st.write("Accuracy on test set: {:.3f}".format(rf.score(X_test, y_test)))

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
    prob_RF = rf.predict_proba(X_test)
    prob_RF = prob_RF[:, 1]

    auc_RF= roc_auc_score(y_test, prob_RF)
    st.write('AUC: %.2f' % auc_RF)

    fpr_RF, tpr_RF, thresholds_RF = roc_curve(y_test, prob_RF) 

    plt.plot(fpr_RF, tpr_RF, color='blue', label='RF') 
    plt.plot([0, 1], [0, 1], color='green', linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    #plt.legend()

    plt.savefig('RF_ROC.png')

    st.image('RF_ROC.png')

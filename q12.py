import imp
from re import S
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.metrics import precision_recall_curve

df1 = pd.read_csv('cleaned.csv', index_col=0)

y = df1.ICU
X = df1.drop("ICU", 1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

def app():
    st.write("### Create a K-Nearest Neighbour model.")
    st.write("#### Please select Number of Neighbors for your K-Nearest Neighbor Classifier: ")
    n_neighbors = st.slider('Number of Neighbors (n_neighbors)', 1, 6, (1,2), 1)
    #st.write(n_estimator[1])
    st.warning("It may take some time to train the model :) Please patiently wait!")

    if n_neighbors[1] == 2:
        accuracy = pd.read_csv('2_KNN_Accuracy.csv')
        st.write("#### Results of the selected hyperparameters : ")
        st.write("Accuracy on training set: {:.3f}".format(accuracy['Accuracy'][0]))
        st.write("Accuracy on test set: {:.3f}".format(accuracy['Accuracy'][1]))

        #Confusion Matrix
        confusion = pd.read_csv('2_KNN_Confusion.csv')
        #st.write('Mjority classifier Confusion Matrix\n', confusion_majority)

        st.write('**********************')
        st.write('Mjority TN= ', confusion['Score'][0])
        st.write('Mjority FP=', confusion['Score'][1])
        st.write('Mjority FN= ', confusion['Score'][2])
        st.write('Mjority TP= ', confusion['Score'][3])
        st.write('**********************')

        st.write('Precision= {:.2f}'.format(confusion['Score'][4]))
        st.write('Recall= {:.2f}'.format(confusion['Score'][5]))
        st.write('F1= {:.2f}'. format(confusion['Score'][6]))
        st.write('Accuracy= {:.2f}'.format(confusion['Score'][7]))

        auc = pd.read_csv('2_KNN_AUC.csv')
        #AUC
        st.write('AUC: %.2f' % auc['Score'][0])

        #plt.legend()

        st.image('2_KNN_Q12_roc.png')

    if n_neighbors[1] == 3:
        accuracy = pd.read_csv('3_KNN_Accuracy.csv')
        st.write("#### Results of the selected hyperparameters : ")
        st.write("Accuracy on training set: {:.3f}".format(accuracy['Accuracy'][0]))
        st.write("Accuracy on test set: {:.3f}".format(accuracy['Accuracy'][1]))

        #Confusion Matrix
        confusion = pd.read_csv('3_KNN_Confusion.csv')
        #st.write('Mjority classifier Confusion Matrix\n', confusion_majority)

        st.write('**********************')
        st.write('Mjority TN= ', confusion['Score'][0])
        st.write('Mjority FP=', confusion['Score'][1])
        st.write('Mjority FN= ', confusion['Score'][2])
        st.write('Mjority TP= ', confusion['Score'][3])
        st.write('**********************')

        st.write('Precision= {:.2f}'.format(confusion['Score'][4]))
        st.write('Recall= {:.2f}'.format(confusion['Score'][5]))
        st.write('F1= {:.2f}'. format(confusion['Score'][6]))
        st.write('Accuracy= {:.2f}'.format(confusion['Score'][7]))

        auc = pd.read_csv('3_KNN_AUC.csv')
        #AUC
        st.write('AUC: %.2f' % auc['Score'][0])

        #plt.legend()

        st.image('3_KNN_Q12_roc.png')
    
    if n_neighbors[1] == 4:
        accuracy = pd.read_csv('4_KNN_Accuracy.csv')
        st.write("#### Results of the selected hyperparameters : ")
        st.write("Accuracy on training set: {:.3f}".format(accuracy['Accuracy'][0]))
        st.write("Accuracy on test set: {:.3f}".format(accuracy['Accuracy'][1]))

        #Confusion Matrix
        confusion = pd.read_csv('4_KNN_Confusion.csv')
        #st.write('Mjority classifier Confusion Matrix\n', confusion_majority)

        st.write('**********************')
        st.write('Mjority TN= ', confusion['Score'][0])
        st.write('Mjority FP=', confusion['Score'][1])
        st.write('Mjority FN= ', confusion['Score'][2])
        st.write('Mjority TP= ', confusion['Score'][3])
        st.write('**********************')

        st.write('Precision= {:.2f}'.format(confusion['Score'][4]))
        st.write('Recall= {:.2f}'.format(confusion['Score'][5]))
        st.write('F1= {:.2f}'. format(confusion['Score'][6]))
        st.write('Accuracy= {:.2f}'.format(confusion['Score'][7]))

        auc = pd.read_csv('4_KNN_AUC.csv')
        #AUC
        st.write('AUC: %.2f' % auc['Score'][0])

        #plt.legend()

        st.image('4_KNN_Q12_roc.png')
    
    if n_neighbors[1] == 5:
        accuracy = pd.read_csv('5_KNN_Accuracy.csv')
        st.write("#### Results of the selected hyperparameters : ")
        st.write("Accuracy on training set: {:.3f}".format(accuracy['Accuracy'][0]))
        st.write("Accuracy on test set: {:.3f}".format(accuracy['Accuracy'][1]))

        #Confusion Matrix
        confusion = pd.read_csv('5_KNN_Confusion.csv')
        #st.write('Mjority classifier Confusion Matrix\n', confusion_majority)

        st.write('**********************')
        st.write('Mjority TN= ', confusion['Score'][0])
        st.write('Mjority FP=', confusion['Score'][1])
        st.write('Mjority FN= ', confusion['Score'][2])
        st.write('Mjority TP= ', confusion['Score'][3])
        st.write('**********************')

        st.write('Precision= {:.2f}'.format(confusion['Score'][4]))
        st.write('Recall= {:.2f}'.format(confusion['Score'][5]))
        st.write('F1= {:.2f}'. format(confusion['Score'][6]))
        st.write('Accuracy= {:.2f}'.format(confusion['Score'][7]))

        auc = pd.read_csv('5_KNN_AUC.csv')
        #AUC
        st.write('AUC: %.2f' % auc['Score'][0])

        #plt.legend()

        st.image('5_KNN_Q12_roc.png')

    if n_neighbors[1] == 6:
        accuracy = pd.read_csv('6_KNN_Accuracy.csv')
        st.write("#### Results of the selected hyperparameters : ")
        st.write("Accuracy on training set: {:.3f}".format(accuracy['Accuracy'][0]))
        st.write("Accuracy on test set: {:.3f}".format(accuracy['Accuracy'][1]))

        #Confusion Matrix
        confusion = pd.read_csv('6_KNN_Confusion.csv')
        #st.write('Mjority classifier Confusion Matrix\n', confusion_majority)

        st.write('**********************')
        st.write('Mjority TN= ', confusion['Score'][0])
        st.write('Mjority FP=', confusion['Score'][1])
        st.write('Mjority FN= ', confusion['Score'][2])
        st.write('Mjority TP= ', confusion['Score'][3])
        st.write('**********************')

        st.write('Precision= {:.2f}'.format(confusion['Score'][4]))
        st.write('Recall= {:.2f}'.format(confusion['Score'][5]))
        st.write('F1= {:.2f}'. format(confusion['Score'][6]))
        st.write('Accuracy= {:.2f}'.format(confusion['Score'][7]))

        auc = pd.read_csv('6_KNN_AUC.csv')
        #AUC
        st.write('AUC: %.2f' % auc['Score'][0])

        #plt.legend()

        st.image('6_KNN_Q12_roc.png')
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 09:44:30 2025

@author: me574
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('C:/coding/ML Course/Multiple Disease Prediction/ML Models/trainedmodel.sav','rb'))
breast_cancer_model = pickle.load(open('C:/coding/ML Course/Multiple Disease Prediction/ML Models/breast_cancer_model.sav', 'rb'))

# navigation sidebar

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction', 
                           'Breast Cancer Prediction'],
                           icons=['activity','person'],
                           default_index = 0)
    
    
# Diabetes Prediction
if (selected == 'Diabetes Prediction'):
    
    st.title('Diabetes Prediction')

    Pregnancies = st.text_input('Number of  Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure Value')
    SkinThickness = st.text_input('SkinThickness Value' )
    Insulin = st.text_input('Insulin Value')
    BMI = st.text_input('BMI Value')
    DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction Value')
    Age = st.text_input('Age')
    
    diagnosis_diabetes = ''
    
    if st.button('Diabetes Results'):
        prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        if (prediction[0]==1):
            diagnosis_diabetes = 'Diabetic'
        else:
            diagnosis_diabetes = 'Not Diabetic'
            
    st.success(diagnosis_diabetes)
if (selected == 'Breast Cancer Prediction'):
    
    st.title('Breast Cancer Prediction')
    


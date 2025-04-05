# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 17:49:22 2025

@author: me574
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open("C:\\coding\\ML Course\\ML Models\\trainedmodel.sav", 'rb'))

def diabetes_predicition(input_data):


 input_data_as_numpy_array = np.asarray(input_data)

 input_data_reshape = input_data_as_numpy_array.reshape(1,-1)


 prediction = loaded_model.predict(input_data_reshape)
 print(prediction)

 if (prediction[0]==0):
   return("The patient is not diabetic pog")
 else:
   return("The patient is diabetic sadge")
  
def main():
    st.title('Diabetes Prediction Web App')
    

    
    Pregnancies = st.text_input('Number of  Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure Value')
    SkinThickness = st.text_input('SkinThickness Value' )
    Insulin = st.text_input('Insulin Value')
    BMI = st.text_input('BMI Value')
    DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction Value')
    Age = st.text_input('Age')
    
    
    diagnosis = ''
    
    if st.button('Diabetes Test Result'):
        
        diagnosis = diabetes_predicition([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        st.success(diagnosis)
        
if __name__== '__main__':
    main()

# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 23:36:43 2025

@author: GIRISH GOWDA
"""

import numpy as np
import pickle
import streamlit as st
#import pandas as pd
from streamlit_option_menu import option_menu

#df = pd.read_csv('C:/Users/User/Downloads/heart.csv')  

# Extract selected feature names (assuming all columns except the target are features)
#feature_names = df.drop(columns=["target"]).columns  # Replace "target" with actual target column name

#print("Selected Feature Names:", feature_names.tolist())
loaded_model=pickle.load(open('C:/Users/User/deployment_model/heart_disease_model.sav','rb'))
with st.sidebar:
    selected = option_menu('MULTIPLE DESEASE PREDICTION',
                         ['heart desease prediction','diabetes prediction'],icons=['heart','activity'],
                         default_index=0)
    
def heart(input_list):
    

# change the input data to a numpy array
    input_data_as_numpy_array= np.array(input_list, dtype=np.float64)

# reshape the numpy array as we are predicting for only on instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    
    

    if (prediction[0] == 0):
       return 'The Person does not have a Heart Disease'
    else:
       return 'The Person has Heart Disease'
if selected=='heart desease prediction':   
  def main():
    st.title('heart desease pediction')
    age=st.text_input('age')
    sex=st.text_input('sex')
    cp=st.text_input('cp')
    trestbps=st.text_input('trestbps')
    chol=st.text_input('chol')
    fbs=st.text_input('fbs')
    restecg=st.text_input('restecg')
    talach=st.text_input('talach')
    exang=st.text_input('exang')
    oldpeak=st.text_input('oldpeak')
    slope=st.text_input('slope')
    ca=st.text_input('ca')
    thal=st.text_input('thal')
    diagnosis=''
    
    if st.button('heart disease prediction result'):
        diagnosis=heart([age,sex,cp,trestbps,chol,fbs,restecg,talach,exang,oldpeak,slope,ca,thal])
    st.success(diagnosis)   
    
if __name__=='__main__':
        main()

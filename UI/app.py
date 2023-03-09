# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 14:01:55 2023

@author: Kingsley
"""
#importing dependencies
import numpy as np
import pandas as pd
from joblib import load
import streamlit as st
from sklearn.preprocessing import StandardScaler

# loading in the data(The dumped model)
model = load('../model/log_model.joblib')


# creating an object of standardscaler
sc = StandardScaler()



#Backend
def predictions(IsActiveMember,EstimatedSalary, HasCrCard, Balance, Age, CreditScore):
    prediction = model.predict(np.array([[IsActiveMember,EstimatedSalary, HasCrCard, Balance, Age, CreditScore]]))

    return prediction

# fuction to create the UI
def main():
    st.title('Bank customer churn model')
    


    Age = st.text_input('Enter your age: ')
    IsActiveMember = st.selectbox('Are you an active member? :', ['yes', 'no'])   
    EstimatedSalary = st.text_input('What is your expected salary :')
    HasCrCard = st.text_input('Do you have a credit card? :')
    Balance = st.number_input('What is your current balance :')
    CreditScore = st.text_input('What is your credit score :')
    
    
    
    button = st.button('Predict')

    
    if IsActiveMember.lower() == 'yes':
       IsActiveMember = 1
    else:
       IsActiveMember = 0
       
     
    
    
    if HasCrCard .lower() == 'yes':
        HasCrCard  = 1
    else:
        HasCrCard  = 0
    
    
    
 
    
  
    
    
    result = ''
    
    if (button):
        result = predictions(IsActiveMember, EstimatedSalary, HasCrCard, Balance, Age, CreditScore)
        if result == 0:
            st.success('this user would not exit')
        else:
            st.success('this user would exit')
    
    
if __name__ == '__main__':
    main()
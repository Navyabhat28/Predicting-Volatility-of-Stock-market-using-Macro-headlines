# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 01:41:24 2021

@author: Lenovo
"""

import pickle

#import nltk
import numpy as np
import pandas as pd
import streamlit as st
import datetime

pickle_in = open("regressor1.pkl","rb")
model = pickle.load(pickle_in)

def close_price(Year, Month, Day,StockName,Positive,Negative,Neutral,Volume,Open,High,Low,Day_of_week):
    if StockName == 'apple':
        StockName = 0
    elif StockName == 'microsoft':
        StockName = 1
    elif StockName == 'nvidia':
        StockName = 2
    elif StockName == 'paypal':
        StockName == 3
    elif StockName == 'tesla':
        StockName = 4
    else:
        print()
        
    if Day_of_week == 'Sunday':
        Day_of_week = 4
    elif Day_of_week == 'Monday':
        Day_of_week = 1
    elif Day_of_week == 'Tuesday':
        Day_of_week = 5
    elif Day_of_week == 'Wednesday':
        Day_of_week = 6
    elif Day_of_week == 'Thursday':
        Day_of_week = 4
    elif Day_of_week == 'Friday':
        Day_of_week = 0
    elif Day_of_week == 'Saturday':
        Day_of_week == 2
    else:
        print()
        
    prediction = model.predict([[Year, Month, Day, StockName, Positive, Negative, Neutral,
                                 Volume, Open, High, Low, Day_of_week]])
    print(prediction)
    return(prediction)



def main():
    st.title("STOCK PRICE PREDICTION")


    
    html_temp = """
    <div style="background-color:#BB5BE7;padding:10px">
    <h2 style="color:white;text-align:center;font-family:'Tahoma';font-weight:bolder;"> Predicting Close price of the stock</h2>
    </div>
    """
    st.markdown('**Enter the following details and we will predict the closing price of the selected** ***Stock***')


    st.markdown(html_temp,unsafe_allow_html=True)
    
    Year = st.number_input('Year', min_value=2019, max_value=2099, step = 1)
    Month = st.number_input('Month', min_value=1, max_value=12, step = 1)
    Day = st.number_input('Day',min_value=1, max_value=31, step = 1)
    #st.write('STOCKNAME:0 for apple, 1 for microsoft, 2 for Nvidia, 3 for paypal, 4 for tesla')
    #StockName = st.number_input('StockName', min_value=0, max_value=4, step = 1)
    StockName = st.selectbox('StockName',('apple', 'microsoft', 'nvidia', 'paypal', 'tesla'))
    Positive = st.text_input('Positive')#, min_value=0, max_value=50, step = 1
    Negative = st.text_input('Negative')#, min_value=0, max_value=50, step = 1
    Neutral = st.text_input('Neutral')#, min_value=0, max_value=50, step = 1
    
    Volume = st.text_input("VOLUME")
    Open = st.text_input("OPEN")
    High = st.text_input("HIGH")
    Low = st.text_input("LOW")
    Day_of_week = st.selectbox('Day_of_week',('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday'))
    
    
    #Headlines = st.text_input("HEADLINES")
    #Headlines = list(Headlines.split("-"))
    #Date = st.text_input("Date")
    #head = filter(Date)
    #negt,neut,post,subj,pol = sent_anls(head)
    
    
    #compound = st.slider("Compound",min_value=0.00 , max_value = 1.00 ,step = 0.01)
    #negative = st.slider("negative",min_value=0.00 , max_value = 1.00 ,step = 0.01)
    #neutral = st.slider("neutral",min_value=0.00 , max_value = 1.00 ,step = 0.01)
    #positive = st.slider("positive",min_value=0.00 , max_value = 1.00 ,step = 0.01)
    #Subjectivity = st.slider("Subjectivity",min_value=0.00 , max_value = 1.00 ,step = 0.01)
    #Polarity = st.slider("Polarity",min_value=0.00 , max_value = 1.00 ,step = 0.01)

       
    result=""

    if st.button("Predict"):
        
        result = close_price(Year, Month, Day,StockName, Positive, Negative, Neutral,Volume,Open,High,Low,Day_of_week)
        
    st.success('Predicted Close Price : $ {}'.format(result))
    

if __name__ =='__main__':
    main()

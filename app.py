import streamlit as st
import pickle
import pandas as pd
import numpy as np

pickle_in=open('best_grid.pkl','rb')
best_grid=pickle.load(pickle_in)

st.title('concrete dataset')

def pred_func(a,b,c,d,e,f,g,h):
    prediction=best_grid.predict([[a,b,c,d,e,f,g,h]])
    print(prediction)
    return prediction




Cement=st.text_input('Cement','Type Here')
Blast=st.text_input('Blast','Type Here')
Fly=st.text_input('Fly','Type Here')
Water=st.text_input('Water','Type Here')
Superplasticizer=st.text_input('Superplasticizer','Type Here')
Coarse=st.text_input('Coarse','Type Here')
Fine=st.text_input('Fine','Type Here')
Age=st.text_input('Age','Type Here')
Strength=''

if st.button('predict'):
    Strength=pred_func(Cement,Blast,Fly,Water,Superplasticizer,Coarse,Fine,Age)

st.success('the strength is {}'.format(Strength))

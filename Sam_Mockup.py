import streamlit as st
import numpy as np

st.title('Lululemon Brand Card Mockup')

dropdowns = {'Drop1':'Text',
              'Drop2':'Text',
               'Drop3':'Text'}
               
for dropdown in range(len(dropdowns.keys())):
  with st.container(dropdowns.keys()[dropdown]):
    st.write(dropdowns[dropdowns[dropdowns.keys()[dropdown]])

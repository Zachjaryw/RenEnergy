import streamlit as st
import numpy as np

st.title('Lululemon Brand Card Mockup')


primark, lulu = st.tabs(['Primark','lululemon'])
               
with primark.expander("Introduction",expanded=False):
  primark.write('\tPrimark holds the view that all must take responsibility in protecting Earth. To join the fight against Climate Change, Primark has formed long-term initiatives to tackle their negative impacts on the environment. With regards to long-term initiatives, Primark looks to encompass a wide range of strategies that includes environmental initiatives, water stewardship, and sustainable chemicals management.')
  
with primark.expander('Goals',expanded=False):
  with primark.expander('Product',expanded=False):
    primark.write('-Create clothes which last: Primark hopes to increase their clothes durability by 2025\n-Clothes that can be recycled: Primark’s clothes will be recyclable by 2027 \n-Clothes created from recycled fibers: Clothes will be made from either recycled or more sustainably sourced materials by 2030')
  with primark.expander('Planet',expanded=False): 
    primark.write('-Halve carbon footprint: Reduce carbon emissions by 50% across value chain by 2030 \n-Eliminate non-clothing waste: In addition to eliminating non-clothing waste, Primark is dedicated to eliminate single use plastic by 2027\n-Restore biodiversity: Incorporate more regenerative agriculture practices by 2030')
    
with primark.expander('Carbon Footprint',expanded=False):
  primark.write('Primark’s total 2021/22 emissions sat slightly above 6.5 million tC02e. Of their total emissions, Scope 3 was vastly responsible for about 6.45 million tC02e; meanwhile Scope 1 and 2 produced 123,772 tC02e. While Scope 3 did increase 3.3% compared to the baseline year of 2018/19, Scope 1 and 2 decreased 22.9% from the 2018/19 baseline year. ')
  
with primark.expander('Climate Activists Groups',expanded=False):
  primark.write('''
Primark Sustainable Cotton Programme 
    -Ensure cotton is 10
    -0% organic, recycled, or sourced from PSCP (idk what this is)  by 2027
    -By the end of 2024, increase volume of cotton from program by around 60%
    -Aims to promote farming methods that support biodiversity and strengthen the resilience of local ecosystems 
Fashion Industry Charter 
Alliance for Water Stewardship 2021
    -Recognizes and rewards those who practice good  water stewardship globally 
Zero Discharge of Hazardous Chemicals Foundation 
    -On current Board of Directors 
    -Help provide direction n the management of sustainable chemicals''')
  
with primark.expander('Other Actions Taken',expanded=False):
  primark.write("Primark continues to look to lead in the categories of conversion, diversion, and innovation. By partnering with Maersk’s EcoDelivery solutions, Primark is able to replace traditional fuels with greener alternatives. With the conversion of  fuel sources, there should be a reduction in emission with shipping products. Furthermore, Primark has diverted 95% of waste from landfills. Not only has Primark learned how to properly expose waste, but it has taught business partners how to deal with waste appropriately. Lastly, Primark has turned to innovation where it will make all hangers out of 100% recycled materials. ")
  
with lulu.expander('Introduction',expanded=False):
  lulu.write('lululemon has established climate targets, backed by the Science Based Targets initiatives, that will work to not only help lululemon achieve net zero carbon by 2050 or earlier, but also help mitigate climate change by preventing an increase of 2 °C in  Earth’s climatic temperature. lululemon has divided its initiatives into the two categories of climate action and sustainable products and material innovation.')

with lulu.expander('Goals',expanded=False):
  with lulu.expander('Climate Action',expanded=False):
    lulu.write('')
  with lulu.expander('Sustainable Products',expanded=False)
    lulu.write('')

import streamlit as st
import numpy as np

st.title('Brand Card Mockup')


select = st.selectbox('Select a Brand',['**Select a Brand**','Lululemon','Primark'])

if select == '**Select a Brand**':
    st.warning('Select a Brand')

elif select == 'Primark':
    with st.expander("Introduction",expanded=False):
      st.write('\tPrimark holds the view that all must take responsibility in protecting Earth. To join the fight against Climate Change, st has formed long-term initiatives to tackle their negative impacts on the environment. With regards to long-term initiatives, st looks to encompass a wide range of strategies that includes environmental initiatives, water stewardship, and sustainable chemicals management.')
      
    with st.expander('Goals',expanded=False):
      st.write('Products')
      st.write('-Create clothes which last: Primark hopes to increase their clothes durability by 2025\n-Clothes that can be recycled: st’s clothes will be recyclable by 2027 \n-Clothes created from recycled fibers: Clothes will be made from either recycled or more sustainably sourced materials by 2030')
      st.write('Planet')
      st.write('-Halve carbon footprint: Reduce carbon emissions by 50% across value chain by 2030 \n-Eliminate non-clothing waste: In addition to eliminating non-clothing waste, st is dedicated to eliminate single use plastic by 2027\n-Restore biodiversity: Incorporate more regenerative agriculture practices by 2030')
        
    with st.expander('Carbon Footprint',expanded=False):
      st.write('Primark’s total 2021/22 emissions sat slightly above 6.5 million tC02e. Of their total emissions, Scope 3 was vastly responsible for about 6.45 million tC02e; meanwhile Scope 1 and 2 produced 123,772 tC02e. While Scope 3 did increase 3.3% compared to the baseline year of 2018/19, Scope 1 and 2 decreased 22.9% from the 2018/19 baseline year. ')
      
    with st.expander('Climate Activists Groups',expanded=False):
      st.write('Primark Sustainable Cotton Programme')
      st.write('-Ensure cotton is 10%')
      st.write('-0% organic, recycled, or sourced from PSCP (idk what this is)  by 2027')
      st.write('-By the end of 2024, increase volume of cotton from program by around 60%')
      st.write('-Aims to promote farming methods that support biodiversity and strengthen the resilience of local ecosystems ')
      st.write('Fashion Industry Charter ')
      st.write('Alliance for Water Stewardship 2021')
      st.write('-Recognizes and rewards those who practice good  water stewardship globally ')
      st.write('Zero Discharge of Hazardous Chemicals Foundation ')
      st.write('-On current Board of Directors ')
      st.write('-Help provide direction n the management of sustainable chemicals')
      
    with st.expander('Other Actions Taken',expanded=False):
      st.write("st continues to look to lead in the categories of conversion, diversion, and innovation. By partnering with Maersk’s EcoDelivery solutions, st is able to replace traditional fuels with greener alternatives. With the conversion of  fuel sources, there should be a reduction in emission with shipping products. Furthermore, st has diverted 95% of waste from landfills. Not only has st learned how to properly expose waste, but it has taught business partners how to deal with waste appropriately. Lastly, Priamrk has turned to innovation where it will make all hangers out of 100% recycled materials. ")


elif select == 'Lululemon':  
    with st.expander('Introduction',expanded=False):
      st.write('lululemon has established climate targets, backed by the Science Based Targets initiatives, that will work to not only help lululemon achieve net zero carbon by 2050 or earlier, but also help mitigate climate change by preventing an increase of 2 °C in  Earth’s climatic temperature. lululemon has divided its initiatives into the two categories of climate action and sustainable products and material innovation.')

    with st.expander('Goals',expanded=False):
      st.write('Climate Action')
      st.write('-Obtain 100% renewable electricity to power own and operated facilities (Achieved) ')
      st.write('-Lower Scope 1 and 2 GHG emission in all owned and operated facilities (Achieved)')
      st.write('-Reduce Scope 3 GHG emissions across entire global supply chain by 60%')
      st.write('Sustainable Products')
      st.write('-Have 75% sustainable materials for their products by 2025')
      st.write('-Have 100% sustainable materials for their products by 2030')
      st.write('-To reach the 2025 set goal of 75%:')
      st.write('-Have their forest-based materials be certified by a third party to ensure that the materials are sourced responsibly')
      st.write('-Verify that 100% of animal-derived materials are 100% sourced responsibly')
      st.write('-Source 100% of cotton from sustainable sources')
      st.write('-Use 75% recycled polyester')
      st.write('-Implement 100% renewable or recycled nylon for products.')

    with st.expander('Carbon Footprint',expanded=False):
      st.write('lululemon’s 2021 carbon footprint is 927k tCO2e. Of its total footprint, Scope 1 and 2 make up .3%, resulting in Scope 3 being responsible for the other 99.7%. However, 69.3% of lululemon’s carbon footprint is included in the company’s science-based targets.')

    with st.expander('Climate Activist Groups',expanded=False):
      st.write('Climate Activation Council ')
      st.write('-Enact change through science-based targets in Product, Transportation, Fulfillment, Manufacturing, Materials, Quality, and Sustainable Business.')
      st.write('Carbon Leadership  Project and Fashion Climate Fund ')
      st.write('Fashion Climate Fund ')
      st.write('-Hopes to raise a total of $2 billion in blended capital. ')
      st.write('-Raised capital is diverted to climate solutions within the apparel industry’s supply chain')
      
    with st.expander('Other Actions Taken',expanded=False):
      st.write('lululemon has placed an emphasis on using materials that hold lower impacts on the environment. The implementation of these low impact materials include innovating and converting materials into being recycled, renewable, responsibly sourced, and lower-impact manufacturing process. ')

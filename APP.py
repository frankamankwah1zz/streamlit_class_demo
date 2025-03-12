import streamlit as st
import seaborn as sns
import pandas as pd

st.title("My first Streamlit App!")

data =  pd.read_csv("https://raw.githubusercontent.com/qurat-azim/instructionaldatasets/refs/heads/main/data/penguins.csv")

st.subheader("Raw Data")



st.sidebar.header("Filter the Options")
selected_category = st.sidebar.selectbox("Select Category", options= ['All', 'Adelie', 'Gentoo', 'Chisnstrap'])

st.write("This shows the scatter plot")


if selected_category !='All':
    filtered_data = data[data['species'] == selected_category]
    st.scatter_chart(data,x='flipper_length_mm', y='body_mass_g', color = 'species')
else:
    st.scatter_chart(data,x='flipper_length_mm', y='body_mass_g', color = 'sex')
 
# Display the plot in Streamlit
st.pyplot(plot.fig)
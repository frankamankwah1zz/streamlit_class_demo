import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Give title to the app
st.title("My first Streamlit App!!!")

# Load penguins data
data = pd.read_csv("https://raw.githubusercontent.com/qurat-azim/instructionaldatasets/refs/heads/main/data/penguins.csv")


# Display raw data
st.write('Raw Data')
st.dataframe(data)

# Sidebar for user input
st.sidebar.header("Filter the Options")
select_category = st.sidebar.selectbox("Select Category", 
                                      options=['All', 'Adelie', 'Gentoo', 'Chinstrap'])

# Filter data based on selection
if select_category != 'All':
    filtered_data = data[data['species'] == select_category]
else:
    filtered_data = data

# Display scatter chart
st.write('This shows the scatter chart')
st.scatter_chart(filtered_data, x='flipper_length_mm', y='body_mass_g', color='species')

# Seaborn Histogram
st.write('Seaborn Histogram of culmen length')
fig,  ax = plt.subplots()
sns.histplot(filtered_data, x='culmen_length_mm', kde=True, ax=ax)
st.pyplot(fig)

# create bar chart
fig, ax = plt.subplots(figsize=(10, 6))
species_counts = filtered_data['species'].value_counts()
ax.bar(species_counts.index, species_counts.values)
ax.set_title("Number of Penguins by Species")
ax.set_xlabel("Species")
ax.set_ylabel("Count")
st.pyplot(fig)


# Boxplot for body mass across species
st.write('Boxplot of Body Mass by Species')
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=filtered_data, x='species', y='body_mass_g', ax=ax)
ax.set_title("Body Mass Distribution by Species")
ax.set_xlabel("Species")
ax.set_ylabel("Body Mass (g)")
st.pyplot(fig)





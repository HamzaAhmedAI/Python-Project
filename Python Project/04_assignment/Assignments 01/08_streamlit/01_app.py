import streamlit as st
import pandas as pd

data = {"Name": ["John", "Jane", "Anna", "Peter"],
        "Age": [28, 34, 29, 42],
        "City": ["New York", "Los Angeles", "Chicago", "Houston"]}  # Removed the extra comma

df = pd.DataFrame(data)

city = st.selectbox("Choose a city", df["City"].unique())
filtered_data = df[df["City"] == city]

st.write(f"Data for {city}:")
st.dataframe(filtered_data)
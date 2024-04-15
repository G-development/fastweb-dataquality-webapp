from urllib.error import URLError

import streamlit as st
import pandas as pd

# Set wide layout for the app
st.set_page_config(layout="wide")

st.title("Fastweb - WebApp x DQ ")
st.subheader("Edit data")

# st.write("Hello world")

def load_data():
    data = pd.read_csv("csv/economic-survey.csv")
    return data

data = load_data()

# Table on screen
# st.write(data)

data = st.data_editor(data)

# Bottone per salvare i dati
if st.button("Salva modifiche"):
    data.to_csv("economic-survey.csv", index=False)
    st.success("Dati salvati con successo!")

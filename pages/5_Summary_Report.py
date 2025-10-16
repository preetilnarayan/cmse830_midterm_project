import streamlit as st
import pandas as pd
from config import STUDENT_DATA_PATH

st.title("Summary Report")

try:
    df = pd.read_csv(STUDENT_DATA_PATH, sep=';', skipinitialspace=True)

    # Clean column names
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.replace(r'\s+', ' ', regex=True)

    st.write("### Missing Values Summary")
    st.dataframe(df.isna().sum().sort_values(ascending=False))

    st.write("### Data Overview")
    st.dataframe(df.describe(include='all').transpose(), height=400)

    st.write("### Target Value Counts")
    if 'Target' in df.columns:
        st.dataframe(df['Target'].value_counts())

except FileNotFoundError:
    st.error(f"Dataset not found at: `{STUDENT_DATA_PATH}`")

import streamlit as st
import pandas as pd

st.title("📊 Data Quality Audit Dashboard")

uploaded_file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("Data Preview")
    st.dataframe(df)

    st.subheader("Missing Values")
    st.write(df.isnull().sum())

    st.subheader("Duplicate Rows")
    st.write(df.duplicated().sum())

    if 'Date of Birth' in df.columns:
        invalid_dates = df['Date of Birth'].apply(lambda x: not pd.to_datetime(str(x), errors='coerce')).isna().sum()
        st.subheader("Invalid 'Date of Birth' Entries")
        st.write(invalid_dates)

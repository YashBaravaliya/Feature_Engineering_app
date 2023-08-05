import streamlit as st
import pandas as pd

cleaned_data = st.session_state["cleaned_data"]


st.title("📈 Export CSV File 📊")


cleaned_data = st.session_state["cleaned_data"]


# Display the data
st.subheader("Data 👇")
st.dataframe(cleaned_data)

@st.cache_data
def convert_df_to_csv(df):
  # IMPORTANT: Cache the conversion to prevent computation on every rerun
  return df.to_csv().encode('utf-8')


st.download_button(
  label="Download data as CSV",
  data=convert_df_to_csv(cleaned_data),
  file_name='export.csv',
  mime='text/csv',
)

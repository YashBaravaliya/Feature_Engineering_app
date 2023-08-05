import pandas as pd
import pandas_profiling as pp
import streamlit as st
from streamlit_pandas_profiling import st_profile_report


cleaned_data = st.session_state["cleaned_data"]
data = st.session_state["data"]

DataFrame = st.sidebar.selectbox("Select DataFrame",["Original DataFrame","cleaned DataFrame"])

# Function to generate pandas profiling report
def generate_profile_report(df):
    profile = pp.ProfileReport(df, explorative=True)
    return profile


st.title("🐼📊 Pandas Profiling with Streamlit 🚀")

if DataFrame == "Original DataFrame":

    # Display the original DataFrame
    st.subheader("Original DataFrame")
    st.dataframe(data)

    # Generate and display the pandas profiling report
    if st.button("Generate Report"):
        st.subheader("Pandas Profiling Report")
        report = generate_profile_report(data)
        st_profile_report(report)

else:
    # Display the original DataFrame
    st.subheader("Cleaned DataFrame")
    st.dataframe(cleaned_data)

    # Generate and display the pandas profiling report
    if st.button("Generate Report"):
        st.subheader("Pandas Profiling Report")
        report = generate_profile_report(cleaned_data)
        st_profile_report(report)


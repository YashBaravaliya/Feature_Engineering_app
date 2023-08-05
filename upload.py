import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import io

# Function to perform some exploratory data analysis
def perform_eda(data):
    st.subheader("Exploratory Data Analysis 📊")

    # Show data summary
    st.write("Data Summary:")
    st.dataframe(data.describe())

    # Show data info
    st.write("Data Info:")
    buffer = io.StringIO()
    data.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)

    # Show data distribution
    st.write("Data Distribution:")
    fig, ax = plt.subplots(figsize=(8, 6))
    for col in data.columns:
        sns.histplot(data[col], ax=ax, kde=True)
        plt.title(f"Distribution of {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        st.pyplot(fig)

def main():
    st.set_page_config(page_title="Feature Engineering App", layout="wide")

    st.title("Feature Engineering App 🚀")

    upload_file = "titanic.csv"

    st.sidebar.header("Feature Engineering")
    upload_file_ = st.sidebar.file_uploader("Upload a CSV file 📂", type=["csv"])

    # Display the selected DataFrame in the main area
    st.subheader("Original DataFrame")

    if upload_file_ is not None:
        data = pd.read_csv(upload_file_)
        cleaned_data = data.copy()

        # Save the cleaned data in session state
        st.session_state["cleaned_data"] = cleaned_data
        st.session_state["data"] = data

        # Show the uploaded data
        with st.container():
            st.subheader("Uploaded Data")
            st.write(data, wide_mode=True)

        with st.container():
            st.write("---")
            left_column, right_column = st.columns(2)

            # Perform Exploratory Data Analysis
            with left_column:
                perform_eda(data)

            # Perform Feature Engineering (add more feature engineering options if needed)
            with right_column:
                st.subheader("Feature Engineering Options")

                # You can add more feature engineering options here

        


if __name__ == "__main__":
    main()

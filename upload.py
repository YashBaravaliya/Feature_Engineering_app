import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import io
from streamlit_extras.stoggle import stoggle

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

    stoggle("How to Use",
            """
    Welcome to the Dataset Explorer app! 🎉 This app allows you to upload a dataset and interactively explore its contents. You can view both the "Original Dataset" and the "Clean Dataset" according to your preference. Here's how to use the app:


    📥 Upload Dataset: On the left sidebar(on top of the left you found a ">" button), click on the "Upload Dataset" button to select and upload your dataset file. Supported formats are CSV, Excel, and JSON.

    🔍 Explore Dataset: After uploading the dataset, click on the "Explore Dataset" button in the sidebar.

    📋 Select Dataset: A dropdown menu will appear with two options: "Original Dataset" and "Clean Dataset." Choose one to view the corresponding version.

    🧰 Customize Data Display: Utilize the provided controls to customize the displayed data. You can specify rows and columns to view, apply filters, and sort the data to your preference.

    🕵️‍♂️ View Specific Data: Dive deep into the dataset by analyzing and inspecting specific rows and columns.

    📊 Pandas Profiling Report: Click on the "Report" button to generate a Pandas profiling report for a comprehensive overview of the dataset.

    🗂️ Handling Missing Values: Below the "Report" button, you'll find a button to handle missing values. In this section, use two dropdown menus—one for visualizing data and the other for performing operations—to manage missing values effectively.

    📈 Handle Categorical Values: Further down, find a button to handle categorical values in the dataset. Use the dropdown to select your preference.

    📤 Export Dataset: At the bottom, you can choose to export the dataset in your desired format.

    We hope you enjoy exploring your data with our app! 📊 If you have any feedback or suggestions, feel free to let us know. 🙌
            """)

    if upload_file_ is not None:
        data = pd.read_csv(upload_file_)
        cleaned_data = data.copy()

        # Save the cleaned data in session state
        st.session_state["cleaned_data"] = cleaned_data
        st.session_state["data"] = data
        st.session_state["file_name"] = upload_file_.name

        # Display the selected DataFrame in the main area
        st.subheader("Original DataFrame")

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

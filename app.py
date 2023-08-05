import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import io

        


def main():
    st.title("Feature Engineering App")
    
    upload_file = "titanic.csv"

    st.sidebar.header("Feature Engineering")
    upload_file_ = st.sidebar.file_uploader("upload a CSV file", type=['csv'])

    
    # Display the selected DataFrame in the main area
    st.subheader("Original DataFrame")

    if upload_file is not None:
        data=pd.read_csv(upload_file)

        cleaned_data = data.copy()

        # Show the uploaded data
        with st.container():
            st.subheader("Uploaded Data")
            st.write(data,wide_mode=True)

        with st.container():
            st.write("---")
            left_cloumn,right_column = st.columns(2)

            with left_cloumn:
                st.write(data.describe())

            with right_column:
                buffer = io.StringIO()
                data.info(buf=buffer)
                s = buffer.getvalue()
                st.text(s)

    

            st.session_state["cleaned_data"] = cleaned_data
            st.session_state["data"] = data

        




if __name__ == "__main__":
    main()

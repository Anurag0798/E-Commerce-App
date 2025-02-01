import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

def main():
    st.title('E-commerce App')
    st.sidebar.title('Navigation')
    upload_file = st.sidebar.file_uploader('Upload Dataset', type=['csv', 'xlsx'])

    if upload_file is not None:
        try:
            if upload_file.name.endswith('csv'):
                data = pd.read_csv(upload_file)
            else:
                data = pd.read_excel(upload_file)
            st.sidebar.success("File uploaded successfully")

            st.subheader("Data Information")
            st.dataframe(data.head())

            st.subheader("Data Statistics")
            st.write("Shape of dataset: ", data.shape)
            st.write("Columns: ", data.columns)
            st.write("Missing Values: ", data.isnull().sum())

            st.subheader("Descriptive Statistics")
            st.write(data.describe())


        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()
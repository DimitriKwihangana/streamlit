import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sample Streamlit App", layout="centered")

st.title("📊 Sample Streamlit Application")

# 1. Text Input
name = st.text_input("Enter your name:", "")

if name:
    st.success(f"Hello, {name}! Welcome to the demo app.")

# 2. File Upload
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("📄 Data Preview:", df.head())

    # Plot a histogram for numeric columns
    numeric_cols = df.select_dtypes(include=["float", "int"]).columns.tolist()
    if numeric_cols:
        column_to_plot = st.selectbox("Choose a column to plot:", numeric_cols)
        fig, ax = plt.subplots()
        df[column_to_plot].hist(ax=ax, bins=20)
        ax.set_title(f"Histogram of {column_to_plot}")
        st.pyplot(fig)
    else:
        st.warning("No numeric columns found in the uploaded file.")

# 3. Sidebar
st.sidebar.header("Settings")
st.sidebar.write("This is a simple sidebar.")

# 4. Checkbox
if st.checkbox("Show appreciation"):
    st.balloons()
    st.write("🎉 Thank you for checking this out!")

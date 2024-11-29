import streamlit as st
import pandas as pd
from app.utils.data_loader import load_csv
from app.utils.plot_helper import plot_data
from config import get_historical_files_path

# Set up Streamlit
st.title("Data Visualization: Historical Prices")

# Load the CSV file using `get_historical_files_path`
try:
    file_path = get_historical_files_path('Bleached Softwood Kraft Pulp Futures Historical Data.csv')
    data = load_csv(file_path)  # Ensure `load_data` is implemented to load CSVs from file paths
    if data is None or data.empty:
        st.error("Failed to load data or data is empty.")
        st.stop()
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# Display a preview of the data
st.write("Data Preview:")
st.write(data.head())

# Allow the user to select columns for plotting
columns = data.columns.tolist()
x_column = st.selectbox("Select X-axis column", ["Date"] + columns)
y_column = st.selectbox("Select Y-axis column", columns)

# Select the type of plot
plot_type = st.selectbox("Select Plot Type", ["line", "scatter", "bar"])

# Generate the plot when the button is clicked
if st.button("Generate Plot"):
    fig = plot_data(data, x_column, y_column, plot_type=plot_type)
    if fig:
        st.pyplot(fig)
    else:
        st.error("Failed to generate the plot. Please check your input.")

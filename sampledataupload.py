import streamlit as st
import pandas as pd

# Load sample data
@st.cache_resource
def load_data():
    data = pd.read_csv(r"C:\Users\HP\Desktop\MISc\data\diabetesdata_csv.csv")  # Load your CSV file
    return data

# Main function
def main():
    # Load sample data
    data = load_data()

    # Display the data
    st.title('Sample Data')
    st.write(data)

if __name__ == "__main__":
    main()

import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

# Navigation sidebar
selected2 = option_menu(None, ["Dataset", "Processing data", "Modelling", "Model Validation"], 
    icons=['house', 'cloud-upload', 'list-task', 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")

# Page: Dataset
if selected2 == 'Dataset':
    st.title('Deskripsi data')
    st.write('Deskripsi data')
    data1 = pd.read_csv('milknew.csv')
    st.write(data1)

# Page: Processing data
if selected2 == 'Processing data':
    st.title('Processing Data')
    st.write("Kami Melakukan Pre-processing data dengan metode Min - Max Scalar")
    st.write("Dengan Hasil Processing Data")
    data2 = pd.read_csv('milk_quality_non-imbalance.csv')
    st.write(data2)
    
    st.title('Processing Data')
    st.write("Kami Melakukan Pre-processing data dengan metode Min - Max Scalar")
    st.write("Dengan Hasil Processing Data")
    data3 = pd.read_csv('milk_quality_imbalance.csv')
    st.write(data3)

# Page: Modelling
if selected2 == 'Modelling':
    st.title('Modelling')
    pilih = st.radio('Pilih', ('Naive Bayes', 'Decision Tree', 'KNN', 'ANN'))

    if pilih == 'Naive Bayes':
        st.title(' Nilai Akurasi 52,5 %')
    elif pilih == 'Decision Tree':
        st.title(' Nilai Akurasi 88 %')
    elif pilih == 'KNN':
        st.title(' Nilai Akurasi 77,5 %')
    elif pilih == 'ANN':
        st.title(' Nilai Akurasi 62,5%')

# Page: Implementasi
# Uncomment and complete the code if needed
# if selected2 == 'Implementasi':
#     st.title('Implementasi')
#     ...

# Uncomment and complete the code if needed
# def calculate_risk(age, sex, blood_pressure, cholesterol, ratio, drug_type):
#     ...

# Uncomment and complete the code if needed
# def main():
#     ...

# Uncomment and complete the code if needed
# if __name__ == "__main__":
#     main()

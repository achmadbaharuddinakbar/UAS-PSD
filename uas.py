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
    st.write('Untuk mengetahui Kualitas pada Susu')
    st.write('Data yang saya gunakan disini yaitu tentang Prediksi Kualitas Susu yang saya dapatkan dari kaggle : https://www.kaggle.com/datasets/cpluzshrijayan/milkquality')
    st.write('Data Kualitas Susu ini merupakan Type Data Numerical.')
    st.write('Tentang Dataset : ')
    st.write('Dataset ini dikumpulkan secara manual dari pengamatan. Hal ini dapat membantu dalam membangun model pembelajaran mesin untuk memprediksi kualitas susu.')
    st.write('Dataset ini terdiri dari 8 variabel independen yaitu :')
    st.write('1. pH : variabel ini mendefinisikan pH halus susu yang berkisar antara 3 hingga 9.5 maks : 6.25 hingga 6.90')
    st.write('2. Temperature : variabel ini mendefinisikan Suhu susu yang berkisar dari 34 derajat Celcius hingga 90 derajat Celcius maks : 34 derajat Celcius hingga 45.20 derajat Celcius')
    st.write('3. Taste : variabel ini mendefinisikan Rasa susu yang merupakan data kategori 0 (Buruk) atau 1 (Baik) maks : 1 (Baik)')
    st.write('4. Odor : variabel ini mendefinisikan Bau susu yang merupakan data kategori 0 (Buruk) atau 1 (Baik) maks : 0 (Buruk)')
    st.write('5. Fat : variabel ini mendefinisikan Lemak susu yang merupakan data kategori 0 (Rendah) atau 1 (Tinggi) maks : 1 (Tinggi)')
    st.write('6. Turbidity : variabel ini mendefinisikan Kekeruhan susu yang merupakan data kategorikal 0 (Rendah) atau 1 (Tinggi) maks : 1 (Tinggi)')
    st.write('7. Color : variabel ini menentukan Warna susu yang berkisar dari 240 hingga 255 maks : 255')
    st.write('8. Grade : variabel ini mendefinisikan Grade (Target) susu yang merupakan data kategori Dimana Low (Buruk) atau Medium (Sedang) atau High (Baik)')

    data1 = pd.read_csv('milknew.csv')
    st.write(data1)

# Page: Processing data
if selected2 == 'Processing data':
    st.title('Processing Data imbalanced (Tidak Seimbang)')
    st.write("Pre-processing imbalanced data")
    st.write("Dengan Hasil :")
    data2 = pd.read_csv('milk_quality_non-imbalance.csv')
    st.write(data2)
    
    st.title('Processing Data')
    st.write("Pre-processing balanced Data")
    st.write("Dengan Hasil :")
    data3 = pd.read_csv('milk_quality_imbalance.csv')
    st.write(data3)

# Page: Modelling
if selected2 == 'Modelling':
    st.title('Modelling')
    st.write('Modelling')
    pilih = st.radio('Pilih', ('Balanced Data', 'Imbalanced Data'))

    if pilih == 'Balanced Data':
        st.title(' Nilai Akurasi 52,5 %')
        st.write('Performa model dengan kelas seimbang (Balanced data)')
        st.write('            precision    recall  f1-score   support')

        st.write('       0       0.99      1.00      0.99        95')
        st.write('       1       1.00      1.00      1.00        73')
        st.write('       2       1.00      0.99      0.99        90')
        st.write('accuracy                           1.00       258')
        st.write('macro avg      1.00      1.00      1.00       258')
        st.write('weighted avg   1.00      1.00      1.00       258')

    elif pilih == 'Imbalanced Data':
        st.title(' Nilai Akurasi 88 %')
        st.write('Performa model dengan kelas tidak seimbang (Imbalanced data)')
        st.write('            precision    recall  f1-score   support')

        st.write('       0       0.98      1.00      0.99        44')
        st.write('       1       1.00      1.00      1.00        92')
        st.write('       2       1.00      0.99      0.99        76')
        st.write('accuracy                           1.00       212')
        st.write('macro avg      0.99      1.00      0.99       212')
        st.write('weighted avg   1.00      1.00      1.00       212')
        
if selected2 == 'Model Validation':
    st.title('Model Validation')



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

import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

# Navigation sidebar
selected2 = st.sidebar.selectbox("Navigation", ["Dataset", "Processing data", "Modelling", "Model Validation", "Implementasi", "About Us"])
    icons=['house', 'cloud-upload', 'list-task', 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")

# Page: Dataset
if (selected2 == 'Dataset') :
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
if (selected2 == 'Processing data') :
    st.title('Processing Data imbalanced (Tidak Seimbang)')
    st.write("Pre-processing imbalanced data")
    st.write("Dengan Hasil :")
    data2 = pd.read_csv('milk_quality_non-imbalance.csv')
    st.write(data2)
    
    # Tombol unduh untuk data tidak seimbang
    st.download_button(
        label="Unduh Data Tidak Seimbang",
        data=data2.to_csv(index=False),
        file_name="milk_quality_non-imbalance.csv",
        key="download_non_imbalance_data",
    )

    st.title('Processing Data')
    st.write("Pre-processing balanced Data")
    st.write("Dengan Hasil :")
    data3 = pd.read_csv('milk_quality_imbalance.csv')
    st.write(data3)
    
    # Tombol unduh untuk data seimbang
    st.download_button(
        label="Unduh Data Seimbang",
        data=data3.to_csv(index=False),
        file_name="milk_quality_imbalance.csv",
        key="download_imbalance_data",
    )


# Page: Modelling
if (selected2 == 'Modelling') :
    st.title('Modelling')
    st.write('Modelling')
    pilih = st.radio('Pilih', ('Balanced Data', 'Imbalanced Data'))

    if pilih == 'Balanced Data':
        st.title('Nilai Akurasi 100 %')
        st.write('Performa model dengan kelas seimbang (Balanced data)')
    
        data4 = {
            '': [' 0', ' 1', ' 2', 'Accuracy', 'Macro Avg', 'Weighted Avg'],
            'Precision': [0.99, 1.00, 1.00, '', 1.00, 1.00],
            'Recall': [1.00, 1.00, 0.99, '', 1.00, 1.00],
            'F1-Score': [0.99, 1.00, 0.99, 1.00, 1.00, 1.00],
            'Support': [95, 73, 90, 258, 258, 258]
        }
    
        table = st.table(data4)
    
    elif pilih == 'Imbalanced Data':
         st.title('Nilai Akurasi 100 %')
         st.write('Performa model dengan kelas tidak seimbang (Imbalanced data)')
    
         data5 = {
             '': [' 0', ' 1', ' 2', 'Accuracy', 'Macro Avg', 'Weighted Avg'],
             'Precision': [0.98, 1.00, 1.00, '', 0.99, 1.00],
             'Recall': [1.00, 1.00, 0.99, '', 1.00, 1.00],
             'F1-Score': [0.99, 1.00, 0.99, 1.00, 0.99, 1.00],
             'Support': [44, 92, 76, 212, 212, 212]
         }
    
         table = st.table(data5)


if (selected2 == 'Model Validation') :
    st.title('Model Validation')
    st.write('Selanjutnya menguji model dengan memprediksikan kualitas suatu susu dengan spesifikasi berikut:')
    
    data6 = {
                 '': [' A', ' B', ' C'],
                 'PH': [6.8, 6.5, 6.5],
                 'Temperature': [45, 40, 45.0],
                 'Odor': [1, 1, 0],
                 'Fat': [1, 0, 0],
                 'Tutbidity': [1, 1, 0],
                 'Colour': [255, 255, 255],
    }
        
    table = st.table(data6)

    st.write('NB: Variabel Taste telah dihapus karena memiliki nilai information gain terkecil yaitu sebesar 0.04, yang artinya variabel tersebut tidak memberikan informasi yang signifikan untuk membedakan kelas target.')

    st.title('Hasil Memprediksi Target Menggunakan Model Terlatih')
    
    data7 = {
                 'Susu': [' A', ' B', ' C'],
                 'PH': [6.8, 6.5, 6.5],
                 'Temperature': [45, 40, 45.0],
                 'Odor': [1, 1, 0],
                 'Fat': [1, 0, 0],
                 'Tutbidity': [1, 1, 0],
                 'Colour': [255, 255, 255],
                 'Prediction': [0, 1, 2],
    }
        
    table = st.table(data7)

    st.write('Susu A diprediksi memiliki kualitas 0 (High)')
    st.write('Susu B diprediksi memiliki kualitas 1 (Low)')
    st.write('Susu C diprediksi memiliki kualitas 2 (Medium)')


# Page: Implementasi
if (selected2 == 'Implementasi') :
    st.title('Klasifikasi Kualitas Susu')
    st.write('Untuk mengetahui Kualitas pada Susu')

    
    col1, col2, col3 = st.columns(3)

    with col1:
        ph = st.number_input('Silahkan Masukkan pH:')
        temprature = st.number_input('Silahkan Masukkan Suhu:', 0)

    with col2:
        list_odor = ['Silahkan Pilih Bau', 'Baik', 'Buruk']
        odor = st.selectbox('Silahkan Pilih Bau susu', list_odor)
        list_fat = ['Silahkan Pilih Lemak', 'Rendah', 'Tinggi']
        fat = st.selectbox('Silahkan Pilih Lemak', list_fat)

    with col3:
        list_turbidity = ['Silahkan Pilih Kekeruhan', 'Rendah', 'Tinggi']
        turbidity = st.selectbox('Silahkan Pilih Kekeruhan', list_turbidity)
        colour = st.number_input('Silahkan Masukkan Warna:', 0)

    button = st.button('Cek Kualitas Susu', use_container_width=500, type='primary')

    if button:
        if odor != 'Silahkan Pilih' and fat != 'Silahkan Pilih' and turbidity != 'Silahkan Pilih' and ph != 0 and temprature != 0 and colour != 0:
            # Mengubah kategori menjadi angka biner
            if odor == 'Baik':
                odor = 1
            elif odor == 'Buruk':
                odor = 0

            if fat == 'Rendah':
                fat = 0
            elif fat == 'Tinggi':
                fat = 1

            if turbidity == 'Rendah':
                turbidity = 0
            elif turbidity == 'Tinggi':
                turbidity = 1

            # Normalisasi fitur-fitur
            ph = ((ph - 3) / (9.5 - 3)) * (1 - 0) + 0
            temprature = ((temprature - 34) / (90 - 34)) * (1 - 0) + 0
            colour = ((colour - 240) / (255 - 240)) * (1 - 0) + 0

            # Melakukan prediksi dengan model Decision Tree yang telah disimpan
            decision_tree_model = load_model(milk.pkl)  # Load the model using the function you've defined

            # Remove 'taste' column from the input features
            cek = decision_tree_model.predict([[ph, temprature, odor, fat, turbidity, colour]])

            # Menampilkan hasil prediksi
            for prediksi in cek:
                st.write('Kualitas Susu Anda', prediksi)
        else:
            st.write('ISI KOLOM TERLEBIH DAHULU')

            
if (selected2 == 'About Us') :
    st.title('Kelompok 7')
    st.write('Mata Kuliah : Proyek Sains Data (C)')

    data8 = {
                 'Nama Anggota Kelompok': [' Achmad Baharudin Akbar', ' Mohammad Iqbal Surya Ramadhan', ' Arif Hidayahtullah', 'Ainur Rifqi'],
                 'NIM': [210411100001, 210411100002, 210411100012, 210411100236],
    }
        
    table = st.table(data8)

    

# Uncomment and complete the code if needed
# def calculate_risk(age, sex, blood_pressure, cholesterol, ratio, drug_type):
#     ...

# Uncomment and complete the code if needed
# def main():
#     ...

# Uncomment and complete the code if needed
# if __name__ == "__main__":
#     main()

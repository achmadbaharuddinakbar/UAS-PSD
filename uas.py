import streamlit as st
from PIL import Image
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np

selected = option_menu(
    menu_title=None,
    options=['Data','Preprocessing','Modelling','Implementasi','Profil'],
    orientation='horizontal',
    menu_icon=None,
    default_index=0,
    styles={
        "nav-link":{
        "font-size":"11.5px",
        "text-align":"center",
        "margin":"5px",
        "--hover-color":"#eee",},
        "nav-link-selected":{
        "background-color":"red"},
    }
)

dt = pd.read_csv('milknew.csv')
if (selected == 'Data') :
    st.title('Deskripsi Data')
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
    dt

if (selected == 'Preprocessing') :
    st.title(' Preprocessing')
    from sklearn.preprocessing import MinMaxScaler
    st.write('Data Asli')
    dt = pd.read_csv('milknew.csv')
    dt
    st.write('Normalisasi Data Menggunkan Min-Max')
    #memilih kolom yang akan di normalisasi
    minmax=['pH','Temprature','Colour']
    #membuat objek scaler Min-Max
    scaler_minmax=MinMaxScaler()
    #melakukan normalisasi pada kolom yang dipilih
    dt[minmax]=scaler_minmax.fit_transform(dt[minmax])
    dt
    #menampilkan data yang sudah di normalisasi
    dt.to_csv('milkquality_minmax.csv')

if (selected == 'Modelling') :
    st.title('Metode dan Hasil Akurasi')
    dt = pd.read_csv('milk_quality_imbalanced.csv')
    X = dt.drop(['Grade'], axis=1)
    y = dt['Grade']
    genre = st.radio(
        "Pilih Model : ",
        ('Decision Tree','knn')
    )
    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import confusion_matrix
    if  genre == 'Decision Tree':
        X_train_balance, X_test_balance, y_train_balance, y_test_balance = train_test_split(X_balance, y_balance, test_size = 0.2, random_state=42)
        clf_balance = DecisionTreeClassifier
        clf_balance.fit(X_train_balance, y_train_balance)
        y_pred_balance = clf_balance.predict(X_test_balance)
        from sklearn.metrics import confusion_matrix
        st.write('Accuracy Pohon Keputusan : ',confusion_matrix(y_test_balance, y_pred_balance))

    #import pickle
    #filename='milkquality.pkl'
    #pickle.dump(classifier,open(filename,'wb'))

    #import os
    #print(os.getcwd())

    #from google.colab import files
    #files.download('milkquality.pkl')

if (selected == 'Implementasi') :
    st.title('Klasifikasi Kualitas Susu')
    st.write('Untuk mengetahui Kualitas pada Susu')
   

    col1,col2,col3 = st.columns(3)
    with col1:
        ph = st.number_input('Silahkan Masukkan pH  :')
        list_odor = ['Silahkan Pilih Bau ','Baik','Buruk']
        odor = st.selectbox('Silahkan Pilih Bau susu', list_odor)
        list_taste = ['Silahkan Pilih Rasa ','Baik','Buruk']
        taste = st.selectbox('Silahkan Pilih Rasa ', list_taste)
    with col2:
        temprature = st.number_input('Silahkan Masukkan Suhu  :')
        list_fat = ['Silahkan Pilih Lemak ','Rendah','Tinggi']
        fat = st.selectbox('Silahkan Pilih Lemak ', list_fat)
    with col3:
        colour = st.number_input('Silahkan Masukkan Warna  :')
        list_turbidity = ['Silahkan Pilih Kekeruhan ','Rendah','Tinggi']
        turbidity = st.selectbox('Silahkan Pilih Kekeruhan ', list_turbidity)

    button = st.button('Cek Kualitas Susu', use_container_width = 500, type = 'primary')

    if button:
        if taste != 'Silahkan Pilih' odor != 'Silahkan Pilih' and fat != 'Silahkan Pilih' and turbidity != 'Silahkan Pilih' and ph != 0 and temprature != 0 and colour != 0:
            if taste=='Baik':
                taste=1
            if taste=='Buruk':
                taste=0
            if odor=='Baik':
                odor=1
            if odor=='Buruk':
                odor=0
            if fat=='Rendah':
                fat=0
            if fat=='Tinggi':
                fat=1
            if turbidity=='Rendah':
                turbidity=0
            if turbidity=='Tinggi':
                turbidity=1
            
            ph=((ph-3)/(9.5-3))*(1-0)+0
            temprature=((temprature-34)/(90-34))*(1-0)+0
            colour=((colour-240)/(255-240))*(1-0)+0
            #st.write(ph,temprature,taste,odor,fat,turbidity,colour)
            import pickle
            with open('milk.pkl','rb') as read:
                clf_balance=pickle.load(read)
            cek=clf_balance.predict([[ph,temprature,odor,fat,turbidity,colour]])
            for prediksi in cek:
                st.write('Kualitas Susu Anda ',prediksi)
        else:
            st.write('ISI KOLOM TERLEBIH DAHULU')
            
if (selected == 'Profil') :
    st.title('My Profile')
    st.write('Nama : Arif Hidayatullah')
    st.write('NIM : 210411100012')
    st.write('Kelas : Penambangan Data (C)')

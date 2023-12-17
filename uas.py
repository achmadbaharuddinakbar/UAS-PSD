import streamlit as st
from PIL import Image
from sklearn.tree import DecisionTreeClassifier
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


if (selected == 'Implementasi') :
    st.title('Klasifikasi Kualitas Susu')
    st.write('Untuk mengetahui Kualitas pada Susu')
   

    col1,col2,col3 = st.columns(3)
    with col1:
        ph = st.number_input('Silahkan Masukkan pH  :')
        temprature = st.number_input('Silahkan Masukkan Suhu  :',0)
        list_taste = ['Silahkan Pilih Rasa ','Baik','Buruk']
        taste = st.selectbox('Silahkan Pilih Rasa ', list_taste)
    with col2:
        list_odor = ['Silahkan Pilih Bau ','Baik','Buruk']
        odor = st.selectbox('Silahkan Pilih Bau susu', list_odor)
        list_fat = ['Silahkan Pilih Lemak ','Rendah','Tinggi']
        fat = st.selectbox('Silahkan Pilih Lemak ', list_fat)
    with col3:
        list_turbidity = ['Silahkan Pilih Kekeruhan ','Rendah','Tinggi']
        turbidity = st.selectbox('Silahkan Pilih Kekeruhan ', list_turbidity)
        colour = st.number_input('Silahkan Masukkan Warna  :',0)

    button = st.button('Cek Kualitas Susu', use_container_width = 500, type = 'primary')

    if button:
        if taste != 'Silahkan Pilih' and odor != 'Silahkan Pilih' and fat != 'Silahkan Pilih' and turbidity != 'Silahkan Pilih' and ph != 0 and temprature != 0 and colour != 0:
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
            with open('milkquality.pkl','rb') as read:
                clf=pickle.load(read)
            cek=clf.predict([[ph,temprature,taste,odor,fat,turbidity,colour]])
            for prediksi in cek:
                st.write('Kualitas Susu Anda ',prediksi)
        else:
            st.write('ISI KOLOM TERLEBIH DAHULU')
            
if (selected == 'Profil') :
    st.title('My Profile')
    st.write('Nama : Arif Hidayatullah')
    st.write('NIM : 210411100012')
    st.write('Kelas : Penambangan Data (C)')

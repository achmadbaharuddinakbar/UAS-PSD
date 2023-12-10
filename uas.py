import streamlit as st
import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from streamlit_option_menu import option_menu
import streamlit as st

#navigasi sidebar
# horizontal menu
selected2 = option_menu(None, ["Data", "Procecing data", "Modelling", 'Implementasi'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
selected2

#halaman Data
if (selected2 == 'Data') :
    st.title('Deskripsi data')

    st.write("Ini adalah contoh data yang tersedia dalam aplikasi Streamlit.")
    st.write("Data ini dikumpulkan dari internet yang berasal dari sebuah perusahaan obat yang telah berlabel set data obat dan parameter yang mempengaruhinya. Oleh karena itu, berdasarkan penyakit dan jenis pasien, obat tersebut direkomendasikan.")
    st.write("Data ini diambil dari Kaggle")
    st.write("The target feature is")
    st.write("- Drug type")
    st.write("The feature sets are:")
    st.write("- Age")
    st.write("- Sex")
    st.write("- Blood Pressure Levels (BP)")
    st.write("- Cholesterol Levels")
    st.write("- Na to Potassium Ration")
    data = pd.read_csv('drug200.csv')
    st.write(data)



#halaman procecing data 
if (selected2 == 'Procecing data') :
    st.title('Procecing Data')

    st.write("Saya Melakukan Pre-processing data dengan metode Min - Max Scalar")
    st.write("Dengan Hasil Processing Data")
    data = pd.read_csv('drug_preprocessed.csv')
    st.write(data)

#halaman modelling
if (selected2 == 'Modelling'):
    st.title('Modelling')

    pilih = st.radio('Pilih', ('Naive Bayes', 'Decision Tree', 'KNN', 'ANN'))

    if (pilih == 'Naive Bayes'):
        st.title(' Nilai Akurasi 52,5 %')
    elif (pilih == 'Decision Tree'):
        st.title(' Nilai Akurasi 88 %')
    elif (pilih == 'KNN'):
        st.title(' Nilai Akurasi 77,5 %')
    elif (pilih == 'ANN'):
        st.title(' Nilai Akurasi 62,5%')


#halaman implementasi
# Load the saved model

# Load the saved model
if (selected2 == 'Implementasi'):
    st.title('Implementasi')


    model_filename = 'loan.pkl'
    with open(model_filename, 'rb') as file:
        model = pickle.load(file)

    # Create a function to preprocess the input data
    def preprocess_input(data):
        # Convert the input data into a DataFrame
        df = pd.DataFrame(data, index=[0])
        
        # Standarisasi fitur
        scaler = StandardScaler()
        scaler.fit(df)  # Fit the scaler on the input data
        df_std = scaler.transform(df)
        
        return df_std

    # Create the Streamlit web app
    def main():
        st.title('Drug Type')

        # Create input fields for the features
        age = st.number_input('Age', min_value=0, max_value=100, value=0)
        sex = st.radio('Sex', ['Male', 'Female'])
        blood_pressure = st.number_input('Blood Pressure (BP)', min_value=0, max_value=200, value=0)
        cholesterol = st.number_input('Cholesterol', min_value=0, value=0)
        sodium_potassium = st.number_input('Na to K (Sodium to Potassium ratio)', min_value=0, value=0)
        
        # Create a dictionary with the input data
        input_data = {
            'Age': age,
            'Sex': sex,
            'Blood Preassure (BP)': blood_pressure,
            'Cholestrol': cholesterol,
            'Na to K (Sodium to Potassium rate)': sodium_potassium,
        }

        # Perform prediction when the button is pressed
        if st.button('Hitung'):
        # Determine the drug type based on the input features
            if age <= 16:
                drug_type = 'Drug_X'
            elif age > 16 and sex == 'Male' and blood_pressure < 1 and cholesterol < 1 and sodium_potassium < 20.037:
                drug_type = 'Drug_A'
            elif age > 16 and sex == 'Female' and blood_pressure >= 1 and cholesterol >= 1 and sodium_potassium >= 20.037:
                drug_type = 'drug_type_3'
            elif age > 16 and sex == 'Male' and blood_pressure >= 1 and cholesterol >= 1 and sodium_potassium < 20.037:
                drug_type = 'drug_type_4'
            elif age > 16 and sex == 'Female' and blood_pressure < 1 and cholesterol < 1 and sodium_potassium >= 20.037:
                drug_type = 'Drug_Y'
            else:
                drug_type = 'Drug_C'

            st.write("Predicted Drug Type:", drug_type)

            # # Display the prediction
            # if prediction[0] == 0:
            #     st.error('DrugC')
            # else:
            #     st.success('DrugY')


# if (selected2 == 'Implementasi'):
#     st.title('Implementasi')

# def calculate_risk(age, sex, blood_pressure, cholesterol, ratio, drug_type):
#     # Lakukan perhitungan di sini sesuai dengan logika yang diperlukan
#     # Misalnya, kamu dapat menggunakan algoritma atau rumus yang sesuai untuk menghitung risiko obat

#     # Contoh sederhana untuk menunjukkan hasil perhitungan
    
#     def klasifikasi_obat(drug_type, nama_obat):
#         if nama_obat in ['Y1', 'Y2', 'Y3']:
#             return 'Tipe Y'
#         elif nama_obat in ['C1', 'C2', 'C3']:
#             return 'Tipe C'
#         elif nama_obat in ['A1', 'A2', 'A3']:
#             return 'Tipe A'
#         elif nama_obat in ['B1', 'B2', 'B3']:
#             return 'Tipe B'
#         elif nama_obat in ['X1', 'X2', 'X3']:
#             return 'Tipe X'
#         else:
#             return 'Tipe obat tidak dikenali'
        
#         return 

# def main():
#     st.title("Drug Risk Calculator")

#     # Buat input fields untuk menerima input dari pengguna
#     age = st.number_input("Usia", min_value=1, max_value=100)
#     sex = st.selectbox("Jenis Kelamin", ["Pria", "Wanita"])
#     blood_pressure = st.number_input("Tingkat Tekanan Darah")
#     cholesterol = st.number_input("Kolesterol")
#     ratio = st.number_input("Rasio Na ke K")
#     # drug_type = st.selectbox("Tipe Obat", ["DrugY", "drugX", "drugA", "drugC", "drugB"])

#     # Buat tombol untuk memulai perhitungan saat ditekan
#     if st.button("Hitung Risiko"):
#         result = calculate_risk(age, sex, blood_pressure, cholesterol, ratio,)
#         st.write("Hasil Perhitungan:")
#         st.write(result)

if __name__ == "__main__":
    main()

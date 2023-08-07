import streamlit as st
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier

# Streamlit uygulamasını oluştur
st.title('Diyabet Teşhisi Uygulaması')
st.write('Bu uygulama ile diyabet teşhisi yapabilirsiniz.')

# Dosya yükleme işlevselliği ekle
st.sidebar.title('Dosya Yükleme')
uploaded_file = st.sidebar.file_uploader('Diyabet verilerini yükleyin (CSV)', type=['csv'])

# Verileri yükle
if uploaded_file is not None:
    diabetes = pd.read_csv(uploaded_file)

    # Modeli eğit
    y = diabetes[['Outcome']]
    x = diabetes.drop(columns=['Outcome'], axis=1)
    model = DecisionTreeClassifier()
    model.fit(x, y)

    # Kullanıcı girişini al
    st.sidebar.title('Veri Girişi')
    pregnancies = st.sidebar.number_input('Kaç adet hamilelik geçirdi?', value=0)
    glucose = st.sidebar.number_input('Glikoz', value=0)
    blood_pressure = st.sidebar.number_input('Kan Basıncı', value=0)
    skin_thickness = st.sidebar.number_input('Deri Kalınlığı', value=0)
    insulin = st.sidebar.number_input('İnsülin direnci', value=0)
    bmi = st.sidebar.number_input('Vücut Kitle İndeksi', value=0.0)
    diabetes_pedigree = st.sidebar.number_input('Diyabet Soyağacı Fonksiyonu', value=0.0)
    age = st.sidebar.number_input('Yaş', value=0)

    # Kullanıcının girdiği veriyi tahminle
    user_input = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]])
    prediction = model.predict(user_input)

    # Tahmin sonucunu göster
    st.write('Tahmin Sonucu:', prediction[0])

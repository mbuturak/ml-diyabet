import streamlit as st
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score


# Streamlit uygulamasını oluştur
st.title('Diyabet Teşhisi Uygulaması')
st.write('Bu uygulama ile diyabet teşhisi yapabilirsiniz.')

# Verileri yükle (kök dizininden)
csv_path = './diabetes.csv'  # Diabetes veri kümesinin doğru yoluyla değiştirin
diabetes = pd.read_csv(csv_path)

# Veri kümesinin boyutlarını göster
total_records = len(diabetes)
st.write(f'Veri kümesinde toplam {total_records} kayıt bulunmaktadır.')

# Veriyi eğitim ve test olarak ayır
y = diabetes[['Outcome']]
x = diabetes.drop(columns=['Outcome'], axis=1)
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.9, random_state=34)

# Modeli eğit
model = DecisionTreeClassifier(max_depth=5, min_samples_split=5, min_samples_leaf=2)
model.fit(x_train, y_train)

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

# Tahmin sonucunu renk ve yazı stili ile göster
if prediction[0] == 1:
    st.write('Tahmin Sonucu:', f'<span style="color:red;font-size:20px">Diyabet riski taşımaktasınız</span>', unsafe_allow_html=True)
else:
    st.write('Tahmin Sonucu:', f'<span style="color:green;font-size:20px">Diyabet riski taşımamaktasınız</span>', unsafe_allow_html=True)


# Eğitim ve test kümesi boyutlarını göster
train_records = len(x_train)
test_records = len(x_test)
st.write(f'Kullanılan Eğitim Kayıt Sayısı: {train_records}/{total_records}')
# st.write(f'Kullanılan Test Kayıt Sayısı: {test_records}/{total_records}')

# Model skorunu hesapla
score = model.score(x_test, y_test)
st.write('Model Doğruluk Oranı:', f'**{score:.2f}**')

cv_scores = cross_val_score(model, x, y, cv=5)  # 5 katlı çapraz doğrulama
st.write('Ortalama Doğruluk Oranı:', np.mean(cv_scores))
st.write('Çapraz Doğrulama Skorları:', cv_scores)


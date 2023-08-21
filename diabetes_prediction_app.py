import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier,export_text
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.tree import plot_tree


# Streamlit uygulamasını oluştur
st.title('Diyabet Teşhisi Uygulaması')
st.write('Bu uygulama ile diyabet teşhisi yapabilirsiniz.')

# Verileri yükle (kök dizininden)
csv_path = './diabetes.csv'  # Diabetes veri kümesinin doğru yoluyla değiştirin
diabetes = pd.read_csv(csv_path)

# Veriyi eğitim ve test olarak ayır
y = diabetes[['Outcome']]
x = diabetes.drop(columns=['Outcome'], axis=1)
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.9, random_state=34)

# Modeli eğit
model = DecisionTreeClassifier(max_depth=5, min_samples_split=5, min_samples_leaf=2)
model.fit(x_train, y_train)

# Kullanıcı girişini al
st.sidebar.title('Diyabet Riski Tahmini')
pregnancies = st.sidebar.number_input('Kaç adet hamilelik geçirdi?', value=0)
glucose = st.sidebar.number_input('Glikoz', value=0)
blood_pressure = st.sidebar.number_input('Kan Basıncı', value=0)
skin_thickness = st.sidebar.number_input('Deri Kalınlığı', value=0)
insulin = st.sidebar.number_input('İnsülin direnci', value=0)
bmi = st.sidebar.number_input('Vücut Kitle İndeksi', value=0.0)
diabetes_pedigree = st.sidebar.number_input('Diyabet Soyağacı Fonksiyonu', value=0.0)
age = st.sidebar.number_input('Yaş', value=0)

# Tahmin işlemi ve yeni kayıtları eklemek
if st.sidebar.button('Hesapla'):
    
    if all([pregnancies == 0, glucose == 0, blood_pressure == 0, skin_thickness == 0, insulin == 0, bmi == 0, diabetes_pedigree == 0, age == 0]):
        st.warning("En az 1 değer girmeniz gerekmektedir.")
    else:
        user_input = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]])
        prediction = model.predict(user_input)

        if prediction[0] == 0:
            result = "Diyabet değil"
        else:
            result = "Diyabet"

        # Tahmin sonucunu renk ve yazı stili ile göster
        if prediction[0] == 1:
            st.write('Tahmin Sonucu:', f'<span style="color:red;font-size:20px">Diyabet riski taşımaktasınız</span>', unsafe_allow_html=True)
        else:
            st.write('Tahmin Sonucu:', f'<span style="color:green;font-size:20px">Diyabet riski taşımamaktasınız</span>', unsafe_allow_html=True)


# Veri kümesinin boyutlarını göster
total_records = len(diabetes)
st.write(f'Veri kümesinde toplam {total_records} kayıt bulunmaktadır.')

# Eğitim ve test kümesi boyutlarını göster
train_records = len(x_train)
test_records = len(x_test)

# Model skorunu hesapla
score = model.score(x_test, y_test)
cv_scores = cross_val_score(model, x, y, cv=5)  # 5 katlı çapraz doğrulama

# Düğmeye tıklanınca ağacın metin tabanlı açıklamalarını göster/gizle
show_tree = st.checkbox('Karar Ağacı Açıklamalarını Göster/Gizle')

#Karar ağacı metin açıklamalarını göster
if show_tree:
     tree_rules = export_text(model, feature_names=x_train.columns.tolist())
     st.code("Decision Tree Rules:\n" + tree_rules, language='text')

# Düğmelere tıklanınca çapraz doğrulama skorlarını, kullanılan kayıt sayılarını ve model doğruluk oranını göster/gizle
show_scores = st.checkbox('Skorları Göster/Gizle')

# Çapraz doğrulama skorlarını göster
if show_scores:
    # Çapraz doğrulama skorları
    st.write('Çapraz Doğrulama Skorları:', cv_scores)
    
    # Kullanılan kayıt sayıları
    st.write(f'Kullanılan Eğitim Kayıt Sayısı: {train_records}/{total_records}')
    st.write(f'Model Doğruluk Oranı: **{score:.2f}**')
    st.write(f'Ortalama Doğruluk Oranı: {np.mean(cv_scores):.2f}')

# Düğmeye tıklanınca ağacın görselleştirmesini göster/gizle
show_tree_plot = st.checkbox('Karar Ağacı Görselleştirmesini Göster/Gizle')

# Karar ağacı görselleştirmesini göster
if show_tree_plot:
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Görselin boyutunu ve çözünürlüğünü ayarla
    plt.figure(figsize=(65, 35), dpi=300)
    plot_tree(model, filled=True, feature_names=x_train.columns.tolist(), max_depth=3)

    # Görselin çıktısını ayarla
    st.pyplot(bbox_inches='tight')


# def predict_diabetes(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age):
#     try:
#         # Modeli eğitiyorsanız bu kısmı bu fonksiyona taşıyabilirsiniz
#         model = DecisionTreeClassifier(max_depth=5, min_samples_split=5, min_samples_leaf=2)
#         model.fit(x_train, y_train)  # x_train ve y_train verileri kullanılarak eğitim yapılıyor

#         user_input = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]])
#         prediction = model.predict(user_input)

#         if prediction[0] == 0:
#             result = "Diyabet değil"
#         else:
#             result = "Diyabet"

#         return result
#     except Exception as e:
#         return str(e)
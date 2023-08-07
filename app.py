import streamlit as st

def main():
    st.title("Hamilelik ve Diyabet Riski Tahmin Arayüzü")

    # Girdileri alın
    pregnancy = st.slider("Hamilelik Sayısı", 0, 17, 1)
    glucose = st.slider("Glikoz", 0, 200, 80)
    blood_pressure = st.slider("Kan Basıncı", 0, 150, 70)
    skin_thickness = st.slider("Deri Kalınlığı", 0, 100, 20)
    insulin = st.slider("İnsülin Direnci", 0, 846, 79)
    bmi = st.slider("Vücut Kitle İndeksi", 0.0, 67.1, 22.0)
    diabetes_pedigree = st.slider("Diyabet Soyağacı Fonksiyonu", 0.078, 2.42, 0.3725)
    age = st.slider("Yaş", 21, 90, 25)

     # Modeli yükle
    with open("./model.pkl", "rb") as model_file:
        model = pickle.load(model_file)

    # Tahmin fonksiyonunu çağırın
    if st.button("Tahmin Et"):
        # Burada tahmin işlemini yapabilirsiniz (örneğin, bir makine öğrenimi modeli kullanarak)
        # Tahmin sonucunu gösterin
        result = "Diyabet Riski: Yüksek"  # Örnek bir sonuç
        st.write(result)

if __name__ == "__main__":
    main()

import streamlit as st
import os
import subprocess

# Doğru kullanıcı adı ve parola
correct_username = "mbuturak"
correct_password = "123456"

# Streamlit arayüzünü oluştur
st.title("Giriş Ekranı")

# Kullanıcı adı ve parola girişi
username = st.text_input("Kullanıcı Adı")
password = st.text_input("Parola", type="password")

# Giriş düğmesi
if st.button("Giriş"):
    if username == correct_username and password == correct_password:
        st.success("Giriş başarılı! Uygulamaya erişiminiz sağlandı.")

        # diabetes_prediction_app.py dosyasını çalıştır
        subprocess.run(["streamlit", "run", "diabetes_prediction_app.py"])

        # Uygulama sonlandığında buraya dönecek
        st.warning("Uygulama sonlandı.")
    else:
        st.error("Kullanıcı adı veya parola yanlış. Lütfen tekrar deneyin.")

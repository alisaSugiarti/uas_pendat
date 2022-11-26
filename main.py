import streamlit as st
import numpy as np

st.title('Aplikasi Web Data Mining')
st.write("""
# Menggunakan beberapa algoritma dengan dataset yang sama
""")

sex=int(st.number_input("Kode Jenis Kelamin ",0))
age=int(st.number_input("Umur ",0))
times=int(st.number_input("jam ",0))
Number_of_warts=int(st.number_input("Number Of Warts ",0))
tipe=int(st.number_input("Tipe ",0))
area=int(st.number_input("Area ",0))
in_di=int(st.number_input("Induration Diameter ",0))

submit = st.button("submit")


nama_dataset = st.sidebar.selectbox(
    'Nama Dataset',
    ('Data Cryotherapy', 'Data Immunotherapy')
)

nama_algoritma = st.sidebar.selectbox(
    'Pilih Metode Algoritma',
    ('K-nearest Neighbors', 'Gaussian Naive Bayes', )
)

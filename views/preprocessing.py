from sklearn.preprocessing import LabelEncoder
import streamlit as st
import pandas as pd

def app():
    st.markdown("# Halaman Pra-pemrosesan Data")

    st.write("### Alur Pra-pemrosesan Data")
    st.write("##### 1. Import Dataset")
    st.code('''df = pd.read_csv("./static/Data_kualifikasi.csv", sep=";")\ndf = df.drop('Nama', axis=1)''', language='python')

    df = pd.read_csv("./static/Data_kualifikasi.csv", sep=";")
    df = df.drop('Nama', axis=1)

    st.table(df.sample(8))

    st.write("##### 2. Mengambil Nama Kolom Pada Dataset")
    columns = df.columns
    st.code('columns = df.columns', language='python')
    st.write(columns)

    st.write("##### 4. Mengubah Data Menjadi Label Encoding")
    st.code('''
    for i in columns:
    le = LabelEncoder()
    df[i]= le.fit_transform(df[i].values)
    ''', language='python')

    for i in columns:
        le = LabelEncoder()
        df[i]= le.fit_transform(df[i].values)

    st.table(df.sample(8))
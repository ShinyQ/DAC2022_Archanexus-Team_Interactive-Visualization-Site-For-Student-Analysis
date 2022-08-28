from re import I
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def app():
    pd.set_option('display.max_columns', None)
    st.markdown("# Halaman Exploratory Data Analysis")

    df = pd.read_csv('./static/Data_kualifikasi.csv', sep=';')
    df['Tgl_Daftar_Kuliah'] = df['Tgl_Daftar_Kuliah'].apply(str)

    st.markdown(f'Total Dataset: {len(df)}')
    st.table(df.sample(10))
    
    df.drop('Nama', axis=1, inplace=True)

    nan_count = []
    columns = df.columns

    for i in columns:
        nan_count.append([i, df[i].isnull().sum()])

    df_count_nan = pd.DataFrame(np.array(nan_count), columns = ['Kolom','Jumlah Kosong'])

    st.markdown("#### Mengecek Jumlah Data Kosong")
    st._legacy_dataframe(df_count_nan, height=350)

    f = plt.figure(figsize=(20, 18))
    
    for i, val in enumerate(list(df.columns)):
        f.add_subplot(4, 3, i+1)
        sns.histplot(df[val], bins=15)
    
    st.write("")
    st.markdown("#### Mengecek Distribusi Data")
    st.pyplot(f)

    for i in columns:
        le = LabelEncoder()
        df[i]= le.fit_transform(df[i].values)



    heatmap_corr = plt.figure(figsize=(12, 10))
    st.markdown("#### Mengecek Korelasi Setiap Kolom")
    sns.heatmap(df.corr(), vmin=-1, vmax=1, annot=True, cmap='BrBG')
    st.pyplot(heatmap_corr)

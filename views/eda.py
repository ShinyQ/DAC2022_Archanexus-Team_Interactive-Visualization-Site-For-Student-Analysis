import random
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
        hexadecimal = ["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])]

        f.add_subplot(4, 3, i+1)
        sns.histplot(df[val], bins=15, color=hexadecimal)
    
    st.write("")
    st.markdown("#### Mengecek Distribusi Data")

    col1, col2 = st.columns([10, 1])

    with col1:
        st.pyplot(f)

    for i in columns:
        le = LabelEncoder()
        df[i]= le.fit_transform(df[i].values)

    st.markdown("#### Mengecek Korelasi Setiap Kolom")

    heatmap_corr = plt.figure(figsize=(12, 10))
    mask = np.triu(np.ones_like(df.corr(), dtype=bool))

    sns.heatmap(df.corr(), mask=mask, vmin=-1, vmax=1, annot=True, cmap='BrBG')

    col1, col2 = st.columns([2, 1])

    with col1:
        st.pyplot(heatmap_corr)

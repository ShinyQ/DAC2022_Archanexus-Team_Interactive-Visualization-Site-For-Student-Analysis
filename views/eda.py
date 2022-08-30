from sklearn.preprocessing import LabelEncoder

import plotly.express as px
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import random

def get_df():
    df = pd.read_csv('./static/Data_kualifikasi.csv', sep=';')
    df['Tgl_Daftar_Kuliah'] = df['Tgl_Daftar_Kuliah'].apply(str)
    df.drop('Nama', axis=1, inplace=True)

    return df


def get_column_unique():
    df = get_df()
    col1, col2 = st.columns([3, 9])

    with col1:
         choose_columns = st.selectbox('Silahkan Pilih Kolom', df.columns)

    df_faculty = dict(df[choose_columns].value_counts())
    df_faculty = sorted(df_faculty.items(), key=lambda item: item[1], reverse=True)
    df_faculty = pd.DataFrame(list(df_faculty), columns=["Jenis", "Jumlah"])

    fig = px.bar(df_faculty, x='Jenis', y='Jumlah', color='Jenis', text_auto=True)
    fig.update_traces(textposition='inside', text='label')
    fig.update_layout(
        font_size = 14, 
        height=400, 
        width=650, 
        margin=dict(l=0, r=15, t=25, b=15),
        showlegend=False
    )

    st.plotly_chart(fig)


def get_column_correlation(df, columns):
    for i in columns:
        le = LabelEncoder()
        df[i]= le.fit_transform(df[i].values)

    heatmap_corr = plt.figure(figsize=(12, 10))
    mask = np.triu(np.ones_like(df.corr(), dtype=bool))

    sns.heatmap(df.corr(), mask=mask, vmin=-1, vmax=1, annot=True, cmap='BrBG')

    col1, col2 = st.columns([2, 1])

    with col1:
        st.pyplot(heatmap_corr)


def get_column_distribution(df):
    f = plt.figure(figsize=(20, 18))
    
    for i, val in enumerate(list(df.columns)):
        hexadecimal = ["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])]

        f.add_subplot(4, 3, i+1)
        sns.histplot(df[val], bins=15, color=hexadecimal)

    col1, col2 = st.columns([10, 1])

    with col1:
        st.pyplot(f)


def app():
    pd.set_option('display.max_columns', None)
    st.markdown("# Halaman Exploratory Data Analysis")

    df = get_df()
    st.markdown(f'Total Dataset: {len(df)}')
    st.table(df.sample(10))

    nan_count = []
    columns = df.columns

    for i in columns:
        nan_count.append([i, df[i].isnull().sum()])

    df_count_nan = pd.DataFrame(np.array(nan_count), columns = ['Kolom','Jumlah Kosong'])
    
    st.write("")
    st.markdown("#### Mengecek Jumlah Data Kosong")
    st._legacy_dataframe(df_count_nan, height=350)

    st.write("")
    st.markdown("#### Persebaran Data Setiap Kolom")
    get_column_unique()

    st.write("")
    st.markdown("#### Mengecek Distribusi Data")
    get_column_distribution(df)

    st.write("")
    st.markdown("#### Mengecek Korelasi Setiap Kolom")
    get_column_correlation(df, columns)
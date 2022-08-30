import streamlit as st
import pandas as pd
import plotly.express as px

def get_df():
    df = pd.read_csv('./static/Data_kualifikasi.csv', sep=';')
    return df

def ukm_fakultas(df):
    pass


def app():
    st.markdown("# Halaman Analisis Dataset")

    df = get_df()
    ukm_fakultas(df)


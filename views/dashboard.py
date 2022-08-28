import streamlit as st
import pandas as pd

def app():
    st.markdown("# Halaman Dashboard")
    df = pd.read_csv('static/Data_kualifikasi.csv', sep=';')
    
    st.markdown('''
        #### Alur Pengerjaan:
        - Topik dataset yang dianalisis adalah data mahasiswa.
        - Dataset babak penyisihan dan kamus data dapat diakses di : https://bit.ly/DatasetBabakPenyisihanDAC2022	
        - Lakukan analisis data yang ada pada "Data - Kualifikasi.csv". Jenis analisis yang digunakan hanya sebatas deskriptif dan diagnostik.
        - Setiap tim juga diperbolehkan sampai ke tahap pembuatan model (tidak diwajibkan).
    ''')

    st.markdown("#### Dataset")
    st.table(df.head(10))

    st.markdown("#### Deskripsi Dataset")
    st.markdown('''
        | Kolom             | Deskripsi                                         |
        |-------------------|---------------------------------------------------|
        | Nama              | Nama Siswa / Mahasiswa                            |
        | Gender            | Jenis Kelamin                                     |
        | Tinggal_Dengan    | Tempat Siswa / Mahasiswa tinggal                  |
        | Status_Kerja      | Apakah siswa / mahasiswa bekerja atau tidak       |
        | Biaya             | Biaya kuliah                                      |
        | Tgl_Daftar_Kuliah | Tahun Daftar Kuliah                               |
        | Alamat            | Alamat siswa / mahasiswa                          |
        | UKM               | Jenis UKM yang diikuti ketika kuliah              |
        | Organisasi_Kampus | Apakah mahasiswa mengikuti organisasi kampus      |
        | Lama_Kuliah       | Lama mahasiswa menyelesaikan kuliah (dalam tahun) |
    ''')


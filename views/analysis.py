import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def get_df():
    df = pd.read_csv('./static/Data_kualifikasi.csv', sep=';')
    return df

def space():
    st.write("\n")
    st.write("\n")

def sankey_dataset(df):
    df_temp1 = df.groupby(["Gender", "Tinggal_Dengan"])["Nama"].count().reset_index()
    df_temp1.columns = ["source", "target", "value"]
    
    df_temp2 = df.groupby(["Tinggal_Dengan", "Status_Kerja"])["Nama"].count().reset_index()
    df_temp2.columns = ["source", "target", "value"]

    df_temp3 = df.groupby(["Status_Kerja", "Biaya"])["Nama"].count().reset_index()
    df_temp3.columns = ["source", "target", "value"]
    df_temp3["target"] = df_temp3.target.map({"Beasiswa" : "Beasiswa", "Orang Tua" : "Ortu"})

    df_temp4 = df.groupby(["Biaya", "Tgl_Daftar_Kuliah"])["Nama"].count().reset_index()
    df_temp4.columns = ["source", "target", "value"]
    df_temp4["source"] = df_temp4.source.map({"Beasiswa" : "Beasiswa", "Orang Tua" : "Ortu"})

    df_temp5 = df.groupby(["Tgl_Daftar_Kuliah", "Alamat"])["Nama"].count().reset_index()
    df_temp5.columns = ["source", "target", "value"]

    df_temp6 = df.groupby(["Alamat", "UKM"])["Nama"].count().reset_index()
    df_temp6.columns = ["source", "target", "value"]
    df_temp6["target"] = df_temp6.target.map({"UKM_1" : "UKM 1", "UKM_2" : "UKM 2", "UKM_3" : "UKM 3", "UKM_4" : "UKM 4", "Tidak" : "Tidak Ada"})

    df_temp7 = df.groupby(["UKM", "Organisasi_Kampus"])["Nama"].count().reset_index()
    df_temp7.columns = ["source", "target", "value"]
    df_temp7["source"] = df_temp7.source.map({"UKM_1" : "UKM 1", "UKM_2" : "UKM 2", "UKM_3" : "UKM 3", "UKM_4" : "UKM 4", "Tidak" : "Tidak Ada"})
    df_temp7["target"] = df_temp7.target.map({"Ya" : "Ya", "Tidak" : "Tidak Ikut"})

    df_temp8 = df.groupby(["Organisasi_Kampus", "Fakultas"])["Nama"].count().reset_index()
    df_temp8.columns = ["source", "target", "value"]
    df_temp8["source"] = df_temp8.source.map({"Ya" : "Ya", "Tidak" : "Tidak Ikut"})

    df_temp9 = df.groupby(["Fakultas", "Lama_Kuliah"])["Nama"].count().reset_index()
    df_temp9.columns = ["source", "target", "value"]

    links = pd.concat([df_temp1, df_temp2, df_temp3, df_temp4, df_temp5, df_temp6, df_temp7, df_temp8, df_temp9], axis=0)
    unique_source_target = list(pd.unique(links[["source", "target"]].values.ravel("K")))
    mapping_dict = {k: v for v, k in enumerate(unique_source_target)}

    links["source"] = links["source"].map(mapping_dict)
    links["target"] = links["target"].map(mapping_dict)
    links_dict = links.to_dict(orient="list")

    fig = go.Figure(data=[go.Sankey(
        valueformat = ".0f",
        node = dict(
            pad=15,
            thickness=15,
            label=unique_source_target
        ),

        link=dict(
            source=links_dict["source"],
            target=links_dict["target"],
            value=links_dict["value"]
        )
    )])
    
    fig.update_layout(
        font_size = 16, 
        height=500, 
        width=1400, 
        margin_pad=0,
        margin=dict(l=0, r=0, t=0, b=0),
    )

    st.plotly_chart(fig)


def pie_ukm_fakultas(df):
    df = df.loc[: , ["UKM", "Fakultas"]]

    col1, col2 = st.columns([3, 9])

    with col1:
         choose_columns = st.selectbox('Silahkan Pilih Kolom', df["UKM"].unique())

    space()
    col1, col2, _ = st.columns([5, 4, 1])
    
    with col1:  
        df_faculty = df.loc[lambda df: df['UKM'] == choose_columns]
        df_faculty = dict(df_faculty['Fakultas'].value_counts())
        df_faculty = df_faculty.items()
        df_faculty = pd.DataFrame(list(df_faculty), columns=["Fakultas", "Jumlah"])

        fig = px.pie(df_faculty, values='Jumlah', names='Fakultas')
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(
            font_size = 18, 
            height=350, 
            width=550, 
            margin=dict(l=0, r=0, t=0, b=0),
            margin_pad=0
        )

        st.plotly_chart(fig)

    with col2:
        st.markdown(f'##### Deskripsi Jumlah Fakultas Pada {choose_columns}:')
        st.table(df_faculty)


def pie_alamat_fakultas(df):
    df = df.loc[: , ["Alamat", "Fakultas"]]

    col1, col2 = st.columns([3, 9])

    with col1:
         choose_columns = st.selectbox('Silahkan Pilih Kolom', df["Fakultas"].unique())

    space()
    col1, col2, _ = st.columns([5, 4, 1])
    
    with col1:  
        df_faculty = df.loc[lambda df: df['Fakultas'] == choose_columns]
        df_faculty = dict(df_faculty['Alamat'].value_counts())
        df_faculty = df_faculty.items()
        df_faculty = pd.DataFrame(list(df_faculty), columns=["Alamat", "Jumlah"])

        fig = px.pie(df_faculty, values='Jumlah', names='Alamat')
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(
            font_size = 18, 
            height=350, 
            width=550, 
            margin=dict(l=0, r=0, t=0, b=0),
            margin_pad=0
        )

        st.plotly_chart(fig)

    with col2:
        st.markdown(f'##### Deskripsi Jumlah Alamat Pada Fakultas {choose_columns}:')
        st.table(df_faculty)


def app():
    st.markdown("# Halaman Analisis Dataset")
    st.write("Pada halaman ini ditampilkan analisis terkait data mahasiswa yang ada.")
    df = get_df()

    st.markdown("#### Persentase Fakultas Berdasarkan UKM Yang Diikuti")
    pie_ukm_fakultas(df)

    space()

    st.markdown("#### Persentase Kota Tinggal Berdasarkan Fakultas")
    pie_alamat_fakultas(df)
    
    space()

    st.markdown("#### Sankey Diagram")
    sankey_dataset(df)

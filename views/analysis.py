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
    columns = [
        'Tinggal_Dengan', 'Status_Kerja', 
        'Biaya', 'Tgl_Daftar_Kuliah', 'Alamat', 
        'UKM', 'Organisasi_Kampus', 'Fakultas', 'Lama_Kuliah'
    ]

    col1, _ = st.columns([11, 1])

    with col1:
        options = st.multiselect(
            'Pilih Urutan Kolom',
            columns,
            columns
        )

    df["Biaya"] = df.Biaya.map({"Beasiswa" : "Beasiswa", "Orang Tua" : "Ortu"})
    df["UKM"] = df.UKM.map({"UKM_1" : "UKM 1", "UKM_2" : "UKM 2", "UKM_3" : "UKM 3", "UKM_4" : "UKM 4", "Tidak" : "Tidak Ada"})
    df["Organisasi_Kampus"] = df.Organisasi_Kampus.map({"Ya" : "Ya", "Tidak" : "Tidak Ikut"})

    if len(options) > 0: 
        temp = []   

        for i in range(0, len(options)):
            if i == 0:
                df_temp1 = df.groupby(["Gender", options[i]])["Nama"].count().reset_index()
                df_temp1.columns = ["source", "target", "value"]
            else:
                df_temp1 = df.groupby([options[i-1], options[i]])["Nama"].count().reset_index()
                df_temp1.columns = ["source", "target", "value"]
            
            temp.append(df_temp1)
        
        links = pd.concat(temp, axis=0)
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
            height=400, 
            width=1100, 
            margin_pad=0,
            margin=dict(l=0, r=0, t=20, b=20),
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
            font_size = 16, 
            height=300, 
            width=450, 
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
            font_size = 16, 
            height=300, 
            width=450, 
            margin=dict(l=0, r=0, t=0, b=0),
            margin_pad=0
        )

        st.plotly_chart(fig)

    with col2:
        st.markdown(f'##### Deskripsi Jumlah Alamat Pada Fakultas {choose_columns}:')
        st.table(df_faculty)


def barplot_year_description(df):
    col1, col2, _ = st.columns([9, 4, 2])

    columns = list(df.columns)
    columns.remove('Nama')
    columns.remove('Tgl_Daftar_Kuliah')

    with col1:
        options = st.multiselect('Pilih Urutan Kolom', columns, columns)

    with col2:
        choose_columns = st.selectbox('Silahkan Pilih Kolom', df["Tgl_Daftar_Kuliah"].unique())


    df_temp = df.loc[lambda df: df['Tgl_Daftar_Kuliah'] == choose_columns]
    df_temp = df_temp.loc[: , options]

    items = []

    for i, column in enumerate(options):
        df_selected = dict(df_temp[column].value_counts())
        items.append([i, list(df_selected.keys()), list(df_selected.values())])

    fig = go.Figure()
    
    for i, data in enumerate(items):
        arr_key = data[0]

        for i in range(len(data[1])):    
            temp_arr = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            temp_arr[arr_key] = data[2][i]

            fig.add_trace(go.Bar(
                y=options,
                x=temp_arr,
                name=data[1][i],
                orientation='h',
                text=data[1][i] + " (" + str(round(data[2][i] / len(df_temp), 2)) + "%) ",
                hoverinfo="x",
                hoverlabel=dict(
                    bgcolor="white",
                    font_size=16,
                    font_family="Rockwell"
                )
            ))

    fig.update_layout(
        barmode='stack',
        font_size = 16, 
        height=450, 
        width=1050,
        extendpiecolors=True,
        margin=dict(l=0, r=0, t=20, b=0),
        showlegend=False,
        hoverlabel_align = 'left',
    )

    st.plotly_chart(fig)


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

    st.markdown("#### Analisis Kolom Berdasarkan Tahun")
    barplot_year_description(df)

    space()

    st.markdown("#### Sankey Diagram")
    sankey_dataset(df)

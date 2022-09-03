import streamlit as st


def app():
    st.markdown("# Halaman Tentang Kami")
    st.markdown("#### Archanexus Team - Telkom University")

    # 4x1
    cols = st.columns([4, 4, 4, 4])

    team = [
        {
            'image': "./static/image/photo/img_ahmad.jpg",
            'name': 'Ahmad Julius Tarigan',
            'nim': '1301190345'
        },
        {
            'image': "./static/image/photo/img_vito.png",
            'name': 'Hanvito Michael Lee',
            'nim': '1301190090'
        },
        {
            'image': "./static/image/photo/img_kurniadi.jpg",
            'name': 'Kurniadi Ahmad Wijaya',
            'nim': '1301194024'
        },
        {
            'image': "./static/image/photo/img_dini.jpg",
            'name': 'Ni Made Dwipadini P.',
            'nim': '1301194141'
        }
    ]

    for i, v in enumerate(cols):
        with v:
            st.image(team[i]['image'], use_column_width=True)
            st.markdown(
                f"""<h5 style='text-align: center;'>{team[i]['name']}</h5>""", unsafe_allow_html=True)
            st.markdown(
                f"""<p style='font-size:20px;text-align: center;'>{team[i]['nim']}</p>""", unsafe_allow_html=True)
            st.markdown(
                "<p style='font-size:20px;text-align: center;'>S1 Informatika</p>", unsafe_allow_html=True)

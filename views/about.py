import streamlit as st
from PIL import Image


def app():
    st.markdown("# Halaman Tentang Kami")
    st.markdown("#### Archanexus Team - Telkom University")
    
    # 4x1
    cols = st.columns([4, 4, 4, 4])

    team = [
        {'image': Image.open(r"./static/image/photo/img_ahmad.jpg").resize((300, 350)),
            'name': 'Ahmad Julius Tarigan', 'nim': '1301190345'},
        {'image': Image.open(r"./static/image/photo/img_vito.png").resize((300, 350)),
            'name': 'Hanvito Michael Lee', 'nim': '1301190090'},
        {'image': Image.open(r"./static/image/photo/img_kurniadi.jpg").resize((300, 350)),
            'name': 'Kurniadi Ahmad Wijaya', 'nim': '1301194024'},
        {'image': Image.open(r"./static/image/photo/img_dini.jpg").resize((300, 350)),
            'name': 'Ni Made Dwipadini Puspitarini',  'nim': '1301194141'}
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
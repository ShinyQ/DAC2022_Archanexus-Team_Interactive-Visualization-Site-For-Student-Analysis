import streamlit as st
from PIL import Image


def app():
    st.markdown("# Halaman Tentang Kami")
    st.markdown("### Archanexus Team - Telkom University")
    
    # 4x1
    cols = st.columns([4, 4, 4, 4])

    team = [
        {'image': Image.open(r"./static/image/photo/img_ahmad.jpg").resize((300, 400)),
            'name': 'Ahmad Julius Tarigan', 'nim': '1301190345'},
        {'image': Image.open(r"./static/image/photo/img_vito.png").resize((300, 400)),
            'name': 'Hanvito Michael Lee', 'nim': '1301190090'},
        {'image': Image.open(r"./static/image/photo/img_kurniadi.jpg").resize((300, 400)),
            'name': 'Kurniadi Ahmad Wijaya', 'nim': '1301194024'},
        {'image': Image.open(r"./static/image/photo/img_dini.jpg").resize((300, 400)),
            'name': 'Ni Made Dwipadini Puspitarini',  'nim': '1301194141'}
    ]

    for i, v in enumerate(cols):
        with v:
            st.image(team[i]['image'], use_column_width=True)
            st.markdown(
                f"""<h4 style='text-align: center;'>{team[i]['name']}</h4>""", unsafe_allow_html=True)
            st.markdown(
                f"""<h5 style='text-align: center;'>{team[i]['nim']}</h5>""", unsafe_allow_html=True)
            st.markdown(
                "<h5 style='text-align: center;'>S1 Informatika</h5>", unsafe_allow_html=True)

    # 2x2
    # row1 = st.columns([12, 12])
    # row2 = st.columns([12, 12])

    # team_row1 = [{'image': Image.open(r"./static/image/photo/img_ahmad.jpg").resize((300, 400)),
    #             'name': 'Ahmad Julius Tarigan', 'nim': '1301190345'},
    #             {'image': Image.open(r"./static/image/photo/img_vito.png").resize((300, 400)),
    #              'name': 'Hanvito Michael Lee', 'nim': '1301190345'}]
    # team_row2 = [{'image': Image.open(r"./static/image/photo/img_kurniadi.jpg").resize((300, 400)),
    #              'name': 'Kurniadi Ahmad Wijaya', 'nim': '1301190345'},
    #             {'image': Image.open(r"./static/image/photo/img_dini.jpg").resize((300, 400)),
    #              'name': 'Ni Made Dwipadini Puspitarini',  'nim': '1301190345'}]
    # for i, v in enumerate(row1):
    #     with v:
    #         st.image(team_row1[i]['image'], use_column_width=True)
    #         st.markdown(
    #             f"""<h4 style='text-align: center;'>{team_row1[i]['name']}</h4>""", unsafe_allow_html=True)
    #         st.markdown(
    #             f"""<h5 style='text-align: center;'>{team_row1[i]['nim']}</h5>""", unsafe_allow_html=True)
    #         st.markdown(
    #             "<h5 style='text-align: center;'>S1 Informatika</h5>", unsafe_allow_html=True)
    # for i, v in enumerate(row2):
    #     with v:
    #         st.image(team_row2[i]['image'], use_column_width=True)
    #         st.markdown(
    #             f"""<h4 style='text-align: center;'>{team_row2[i]['name']}</h4>""", unsafe_allow_html=True)
    #         st.markdown(
    #             f"""<h5 style='text-align: center;'>{team_row2[i]['nim']}</h5>""", unsafe_allow_html=True)
    #         st.markdown(
    #             "<h5 style='text-align: center;'>S1 Informatika</h5>", unsafe_allow_html=True)

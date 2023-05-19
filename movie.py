import streamlit as st
import pandas as pd
import requests

menu = st.sidebar.selectbox(
    'Menu:',
    ('Home', 'Top Anime', 'Recommendation')
)

st.header("Anime Recommendation System")

if menu == 'Home' or menu == '':
    st.subheader("Anime Title")
    with st.form("anime_recs"):
        title = st.text_input("Anime Title", placeholder="Masukkan judul anime")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.markdown(f"Pencarian rekmendasi berdasarkan : <strong>" + title + "</strong>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        col1.write("Judul Anime sini1")
        col1.
        col2.write("Judul Anime sini2")
        col3.write("Judul Anime sini3")

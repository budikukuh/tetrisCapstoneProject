import streamlit as st
import pandas as pd
import plotly.graph_objs as go

top_sma_df = pd.read_excel('top_sman_dataset.xlsx')

sidebar = st.sidebar
sidebar.title('Menu Options')

def introduction():
    st.image('introduction.png', width=None)
    st.markdown("""
    ## Analisis Kualitas Sekolah Menengah Atas berdasarkan Nilai UTBK dan Rekomendasi Sekolah Terbaik di Daerah Sekitar (Kabupaten)
    by : Muhhamad Kukuh Budi Martono\n

    \n

    # Latar Belakang

    Sejak tahun 2017, Kementerian Pendidikan, Kebudayaan, Ristek, dan Teknologi
    (Kemendikbudristek) telah mengeluarkan kebijakan zonasi dalam sistem penerimaan peserta
    didik baru (PPDB). Kebijakan PPDB merupakan salah satu upaya untuk meningkatkan akses
    layanan pendidikan yang berkeadilan.\n

    Sebagaimana telah disebutkan dalam Permendikbud Nomor 1 Tahun 2021, Jenjang Sekolah
    Menengah Pertama (SMP) dan Sekolah Menengah Atas (SMA), jalur zonasi diberikan kuota
    sebesar 50 persen dari daya tampung sekolah, afirmasi 15 persen, serta jalur perpindahan
    orang tua maksimal 5 persen dan selebihnya dapat digunakan sebagai jalur prestasi.\n

    Penerapan sistem zonasi ternyata berpengaruh terhadap murid ataupun wali murid karena
    mereka harus mencari sekolah terbaik di sekitar tempat tinggal mereka. Terkadang mereka
    bingung memilih sekolah yang terbaik untuk putra/putri mereka, sehingga menyebabkan
    mereka gegabah dalam memilih sekolah tanpa mencari informasi terlebih dahulu. Berdasarkan
    permasalahan di atas, penulis mengembangkan sistem rekomendasi sekolah terbaik di daerah
    kabupaten pengguna.\n

    \n
    \n

    \nThis Project is to perform the analysis on the Top 1000 sekolah Tahun 2022 Berdasarkan Nilai UTBK.
    Here I use the scrapping dataset from the website [LTMPT](https://ltmpt.ac.id/) and used various libraries of Python
    for visualization of Data.
    \nThe Libraries I used in Project are: [Matplotlib](https://matplotlib.org/), 
    [Seaborn](https://seaborn.pydata.org/), [Plotly](https://plotly.com/python/), 
    [Pandas](https://pandas.pydata.org/), dan [Streamlit](https://streamlit.io/)
    
    """)


def analisis():
    st.markdown("""
    ## Analisis Kualitas Sekolah Menengah Atas berdasarkan Nilai UTBK dan Rekomendasi Sekolah Terbaik di Daerah Sekitar (Kabupaten)

    """)

options = ['Project Introduction', 'Analisis']

selOption = sidebar.selectbox("Select an Option", options)

if selOption == options[0]:
    introduction()
elif selOption == options[1]:
    analisis()
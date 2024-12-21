import streamlit as st
import pandas as pd

st.title("BIODATA DAN PENDIDIKAN")
st.header("IVAN TRIYADI")

col_1, col_2 = st.columns([1,2])

with col_1:
    st.subheader("Biodata")
    st.text("Nama:Ivan Triyadi")

    st.subheader("Alamat")
    st.text("Serua Residence, Depok")

with col_2:
    st.subheader("Kegiatan")
    st.text("Fulltime: kantor GE")

    st.subheader("Kontak")
    st.text("Phone: +628111588698")
    st.text("Instagram: ivantriyadi")

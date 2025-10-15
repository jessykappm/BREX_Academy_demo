import streamlit as st


st.set_page_config(page_title="BREX Academy")
st.logo("imagens/logo.png")
col1, col2= st.columns(2, gap="large")
with col1:
    st.subheader("Bem-vindo ao hub de informações da BREX!")
    st.write("Aqui você encontra informaçãoes e tutoriais para melhorar sua performance no jogo.")
    st.write("Navegue pelo menu lateral, e encontre o que precisa.")
with col2:
    st.image("imagens/logo.png")
import streamlit as st

tab0, tab1, tab2, tab3, tab4, tab5 = st.tabs(["Home","Heróis", "VS","Construções","Quartel", "Temporada 1"])

with tab0:
    st.title("BREX Academy")
    st.logo("imagens/logo.png")
    col1, col2= st.columns(2, gap="large")
with col1:
    st.subheader("Bem-vindo ao hub de informações da BREX!")
    st.write("Aqui você encontra informaçãoes e tutoriais para melhorar sua performance no jogo.")
    st.write("Navegue pelo menu lateral, e encontre o que precisa.")
with col2:
    st.image("imagens/logo.png")

with tab1:
    st.subheader("Formação dos esquadrões:")
    st.video("https://youtu.be/ccrW8UV1nXk")
    
with tab2:
    st.subheader("Dia 1:")
    st.video("https://youtu.be/eiEgahem3Qc")
    
with tab3:
    st.subheader("Guia de construçãoes")
    st.video("https://youtu.be/0PmHHKwb1iw")
    
with tab4:
    st.subheader("Treinamento cascata:")
    st.video("https://youtu.be/oeWlkY_FqhI")

with tab5:
    with st.expander("Playlist da Temporada 1"):
        st.video("https://youtu.be/TGy_DKJukN8?list=PL5Ct1GWEEkBRFpjPIJigLPVyWue4cORSt")

    with st.expander("Tutorial fazenda de soro"):
        st.image("imagens/resistencia.jpeg")
import streamlit as st



def generate_title():
    # Ttile
    col1, col2, col3 = st.columns([0.2, 0.6, 0.2])

    with col1:
        st.image("./images/logo.png")
    with col2:
        st.markdown("<h1 style='text-align: center;'>The Hugging Stack</h1>", unsafe_allow_html=True)
    with col3:
        st.image("./images/logo.png")
    
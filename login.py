import streamlit as st

def login_page():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        # Switch to the Insight page
        st.session_state.page = 'insight'

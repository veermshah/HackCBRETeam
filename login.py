import streamlit as st

def login_page(roles):
    st.title("Login Page")
    # Create a dropdown for selecting a role
    selected_role = st.selectbox("Select Your Role:", roles)
    
    valid = True  # Set valid to True for any username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        st.session_state.page = 'insight'
    # You can remove the "Login Incorrect" message as it's always valid now

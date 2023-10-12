import streamlit as st

# Sample list of roles
roles = ["Technician", "Building Manager", "Account Director", "Chief Engineer", "Portfolio Manager", "Asset Manager", "Leasing Manager", "Facility Coordinator", "Maintenance Supervisor"]

def login_page():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    selected_role = st.selectbox("Select Your Role:", roles)
    if st.button("Login"):
        # Switch to the Insight page
        st.session_state.page = 'insight'

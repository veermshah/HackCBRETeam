import streamlit as st
import csv

roles = ["Technician", "Building Manager", "Account Director", "Chief Engineer", "Portfolio Manager", "Asset Manager", "Leasing Manager", "Facility Coordinator", "Maintenance Supervisor"]

users = []
# Open and read the CSV file
with open('property_insights_extended.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        users.append(row)
        
def login_page():
    st.title("Login Page")
    # Create a dropdown for selecting a role
    selected_role = st.selectbox("Select Your Role:", roles)
    
    valid = False
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in users:
            valid = True
            st.session_state.page = 'insight'
    if valid == False:
        st.success("Login Incorrect")
        

    
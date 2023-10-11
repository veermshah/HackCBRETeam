# Import prerequisite libraries
import streamlit as st
import os
import openai
import csv
import gpt

# Sample list of roles
roles = ["Technician", "Building Manager", "Account Director", "Chief Engineer", "Portfolio Manager", "Asset Manager", "Leasing Manager", "Facility Coordinator", "Maintenance Supervisor"]

# Streamlit app title
st.title("Role Selection with Login")

# Create input boxes for username and password
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Create a dropdown for selecting a role
selected_role = st.selectbox("Select Your Role:", roles)

# Create a login button
if st.button("Login"):
    # Check if the username and password are correct (for demo purposes, you can replace this with your authentication logic)
    if username == "your_username" and password == "your_password":
        st.success("Login successful!")
        st.write(f"You selected role: {selected_role}")
    else:
        st.error("Login failed. Please check your username and password.")
        
gpt.promptGPT("How long do elephants live?")

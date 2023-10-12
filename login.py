import streamlit as st
import csv

roles = ["Technician", "Building Manager", "Account Director", "Chief Engineer", "Portfolio Manager", "Asset Manager", "Leasing Manager", "Facility Coordinator", "Maintenance Supervisor"]

# Initialize empty lists to store data
names = []
emails = []
roles1 = []
businessLines = []
locations = []
clients = []
dashboard = []
userActivity = []

# Open and read the CSV file
with open('recommendation_engine_users.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row if it exists
    for row in reader:
        names.append(row[0])
        emails.append(row[1])
        roles1.append(row[2])  
        businessLines.append(row[3])  
        locations.append(row[4])
        clients.append(row[5]) 
        dashboard.append(row[6])
        userActivity.append(row[7])

selected_role = "Technician"

def login_page():
    st.title("Login Page")
    # Create a dropdown for selecting a role
    selected_role = st.selectbox("Select Your Role:", roles)
    
    valid = False
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        st.session_state.page = 'insight'
        #if username in emails:
            #valid = True
            #st.session_state.page = 'insight'
    #if valid == False:
        #st.markdown("Login Incorrect")
        
import streamlit as st

# Sample list of roles
roles = ["Technician", "Building Manager", "Account Director", "Chief Engineer", "Portfolio Manager", "Asset Manager", "Leasing Manager", "Facility Coordinator", "Maintenance Supervisor"]

# Create a Streamlet app
st.title("Role Selection")

# Create a dropdown box for selecting a role
selected_role = st.selectbox("Select Your Role:", roles)

# Display the selected role
st.write(f"You selected: {selected_role}")
import streamlit as st

# Sample list of roles
roles = ["Technician", "Building Manager", "Account Director", "Chief Engineer", "Portfolio Manager", "Asset Manager", "Leasing Manager", "Facility Coordinator", "Maintenance Supervisor"]

# Create a Streamlit app title
st.title("Multi-Page Streamlit App")

# Create a session state to manage page switching
if 'page' not in st.session_state:
    st.session_state.page = 'login'

# Function to render the login page
def login_page():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    selected_role = st.selectbox("Select Your Role:", roles)
    if st.button("Login"):
        # Switch to the Insight page
        st.session_state.page = 'insight'

# Function to render the insight page
def insight_page():
    st.title("Insight Page")
    st.write("Welcome to the Insight Page!")

# Remove the Streamlit sidebar
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

# Check the page state and render the appropriate page
if st.session_state.page == 'login':
    login_page()
else:
    insight_page()

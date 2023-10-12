import streamlit as st
from login import login_page
from insight import insight_page
import os
import openai
import csv
import gpt


# Create a Streamlit app title
st.title("Multi-Page Streamlit App")

# Create a session state to manage page switching
if 'page' not in st.session_state:
    st.session_state.page = 'login'

# Check the page state and render the appropriate page
if st.session_state.page == 'login':
    login_page()
else:
    insight_page()

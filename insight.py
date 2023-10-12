import streamlit as st
from gpt import GPT  # Import the GPT function from the gpt module

def insight_page():
    st.title("Insight Page")

    for i in range(1, 11):
        st.header(f"Insight {i}")  # Use header for a standard text format

        # Call your GPT function here and store the generated insight in a variable
        insight = GPT()  # Assuming GPT() returns a single insight

        # Display the AI-generated insight in a standard text format
        st.text(insight)

        # Create a column to contain the buttons for this insight
        col = st.columns(5)

        # Add unique keys to the buttons
        like_button = col[0].button("Like", key=f"like_button_{i}")
        dislike_button = col[1].button("Dislike", key=f"dislike_button_{i}")
        share_button = col[2].button("Share", key=f"share_button_{i}")
        bookmark_button = col[3].button("Bookmark", key=f"bookmark_button_{i}")
        comment_button = col[4].button("Comment", key=f"comment_button_{i}")

        # You can handle the button actions here as needed
        if like_button:
            # Handle the Like action for insight i
            pass

        if dislike_button:
            # Handle the Dislike action for insight i
            pass

        if share_button:
            # Handle the Share action for insight i
            pass

        if bookmark_button:
            # Handle the Bookmark action for insight i
            pass

        if comment_button:
            # Handle the Comment action for insight i
            pass

    # Centered and styled "Log Out" button
    st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
    if st.button("Log Out", key="log_out_button", help="Log out and return to the login page"):
        st.session_state.page = "login"
    st.markdown('</div>', unsafe_allow_html=True)

import streamlit as st

def insight_page():
    st.title("Insight Page")

    for i in range(1, 11):
        st.markdown(f"### Insight {i}")
        st.text(f"This is your {i} insight.")

        # Create five columns for buttons
        col1, col2, col3, col4, col5 = st.columns(5)

        # Add unique keys to the buttons
        like_button = col1.button(f"Like {i}", key=f"like_button_{i}")
        dislike_button = col2.button(f"Dislike {i}", key=f"dislike_button_{i}")
        share_button = col3.button(f"Share {i}", key=f"share_button_{i}")
        bookmark_button = col4.button(f"Bookmark {i}", key=f"bookmark_button_{i}")
        comment_button = col5.button(f"Comment {i}", key=f"comment_button_{i}")


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

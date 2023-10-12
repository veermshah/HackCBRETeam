import streamlit as st
from gpt import promptGPT  # Import the GPT function from the gpt module

def insight_page():
    st.title("Insight Page")

    # Call your GPT function here and store the generated insights in a variable
    insights = promptGPT(1)

    for i, insight in enumerate(insights, start=1):
        st.header(f"Insight {i}")  # Use header for a standard text format

        if "choices" in insight and len(insight["choices"]) > 0:
            content = insight["choices"][0].get("message", {}).get("content", "")
            # Display the AI-generated content in multiple lines with the same font
            st.text(content)
        else:
            st.text("No insights available for this item.")

        # Create a row to contain the buttons for this insight
        col1, col2, col3, col4, col5 = st.columns(5)

        # Add buttons to the columns
        like_button = col1.button("Like", key=f"like_button_{i}")
        dislike_button = col2.button("Dislike", key=f"dislike_button_{i}")
        share_button = col3.button("Share", key=f"share_button_{i}")
        bookmark_button = col4.button("Bookmark", key=f"bookmark_button_{i}")
        comment_button = col5.button("Comment", key=f"comment_button_{i}")

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

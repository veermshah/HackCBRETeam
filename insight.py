import streamlit as st

# Define the button images with their paths
button_images = {
    "Like": "like.png",
    "Dislike": "dislike.png",
    "Share": "share.png",
    "Bookmark": "save.tiff",
    "Comment": "comment.png",
}

# Set the common image size
image_size = 50  # Adjust the size as needed

# Mock AI-generated insights (replace with your actual data)
insights = ["AI Insight 1", "AI Insight 2", "AI Insight 3", "AI Insight 4", "AI Insight 5"]

def insight_page():
    st.title("Insight Page")

    for i in range(5):  # Adjust the number of insights as needed
        st.header(f"Insight {i+1}")

        # AI-generated insight
        st.write(insights[i])

        # Create a row to contain the image buttons
        col1, col2, col3, col4, col5 = st.columns(5)

        # Add images without captions
        col1.image(button_images["Like"], use_column_width=False, width=image_size)
        col2.image(button_images["Dislike"], use_column_width=False, width=image_size)
        col3.image(button_images["Share"], use_column_width=False, width=image_size)
        col4.image(button_images["Bookmark"], use_column_width=False, width=image_size)
        col5.image(button_images["Comment"], use_column_width=False, width=image_size)

        # Add buttons with text under each image
        if col1.button("Like", key=f"like_button_{i}"):
            # Handle the Like action for insight i
            pass

        if col2.button("Dislike", key=f"dislike_button_{i}"):
            # Handle the Dislike action for insight i
            pass

        if col3.button("Share", key=f"share_button_{i}"):
            # Handle the Share action for insight i
            pass

        if col4.button("Bookmark", key=f"bookmark_button_{i}"):
            # Handle the Bookmark action for insight i
            pass

        if col5.button("Comment", key=f"comment_button_{i}"):
            # Handle the Comment action for insight i
            pass

    # Centered and styled "Log Out" button
    st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
    if st.button("Log Out", key="log_out_button", help="Log out and return to the login page"):
        st.session_state.page = "login"
    st.markdown('</div>', unsafe_allow_html=True)

# Run the Streamlit app
if __name__ == "__main__":
    insight_page()

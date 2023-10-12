import streamlit as st
import login
import myGPT

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

def insight_page():
    # Get the user's role
    role = login.getRole()

    # Set the role as the title
    st.title(role)

    st.title("Insights")
    
    # Ranking *****************************************************************************
    
    # By Jobs
    if login.getRole() == "Technician":
        priority = ["Energy Usage", "Work Orders", "Accessibility", "Saftey Incidents"]
        print(priority)
    elif login.getRole() == "Building Manager":
        priority = ["Leases", "Energy Usage", "Compliance", "Budgets", "Tenant Satisfaction", "Occupancy"]
    elif login.getRole() == "Account Director":
        priority = ["Budgets", "Compliance", "Occupancy", "Leases", "Tenant Satisfaction"]
    elif login.getRole() == "Chief Engineer":
        priority = ["Work Orders", "Saftey Incidents", "Energy Usage", "Accessibility"]
    elif login.getRole() == "Portfolio Manager":
        priority = ["Budgets"]
    elif login.getRole() == "Asset Manager":
        priority = ["Budgets"]
    elif login.getRole() == "Leasing Manager":
        priority = ["Leases", "Occupancy"]
    elif login.getRole() == "Facility Coordinator":
        priority = ["Tenant Satisfaction", "Compliance"]
    elif login.getRole() == "Maintenance Supervisor":
        priority = ["Compliance", "Work Orders"]
        
    priorities1 = myGPT.getPriorities()
    print(priorities1)
    criticalities = myGPT.getCriticality()
    indexes = []
    critIndexes = []
    for i in range(len(priorities1)):
        if priorities1[i] in priority:
            indexes.append(i)
            
    for i in range(len(indexes)):
        if criticalities[indexes[i]] == "Critical":
            critIndexes.append(indexes[i])
   
    # END RANKING *******************************************************************

    # Limit the number of displayed insights to 10
    max_insights = min(10, len(critIndexes))

    # Call your GPT function here and store the generated insights in a variable
    for i in range(max_insights):
        insights = myGPT.promptGPT(critIndexes[i])
        
        # Add the title "Insight {i+1}"
        st.header(f"Insight {i+1}")

        st.markdown("Company: " + myGPT.getAccount(i))  # Use header for a standard text format
        st.markdown(myGPT.getInsight2(critIndexes[i]))
        st.write(f'<div style="white-space: pre-line;">{insights}</div>', unsafe_allow_html=True)
        st.write(" ")
    
        # Create a row to contain the buttons for this insight
        col1, col2, col3, col4, col5 = st.columns(5)

        # Add images above buttons
        col1.image(button_images["Like"], width=image_size, use_column_width=False)
        col2.image(button_images["Dislike"], width=image_size, use_column_width=False)
        col3.image(button_images["Share"], width=image_size, use_column_width=False)
        col4.image(button_images["Bookmark"], width=image_size, use_column_width=False)
        col5.image(button_images["Comment"], width=image_size, use_column_width=False)

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

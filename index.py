import streamlit as st
# Create a sidebar
sidebar = st.sidebar
# Add a title to the sidebar
sidebar.title("Admin Template Panel")
# Add a menu to the sidebar
sidebar.menu(
    [
        "Dashboard",
        "Users",
        "Products",
        "Orders",
        "Settings",
    ]
)
# Create a main content area
main_content = st.main_content
# Add a title to the main content area
main_content.title("Dashboard")
# Add some content to the main content area
main_content.write("This is the dashboard.")
# Add a footer to the main content area
main_content.footer("Copyright 2023")
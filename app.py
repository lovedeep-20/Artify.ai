import streamlit as st
from streamlit_option_menu import option_menu

# Set the page title and configuration
st.set_page_config(page_title="Artify.ai", page_icon=":rainbow:", layout="wide")

# Define the available pages
pages = {
    "Home": "screens/home.py",
    "Flux Schnell": "screens/flux_schnell.py",
    "Contact": "screens/contact.py",
    "About": "screens/about.py",
}

# Sidebar navigation using option_menu for a modern look
with st.sidebar:
    selected = option_menu(
        "Main Menu", 
        list(pages.keys()),  # Page names from dictionary keys
        icons=["house", "lightning", "envelope", "info-circle"],  # Icons for each page
        menu_icon="cast", 
        default_index=0, 
    )

# Load and display the selected page
if selected:
    with open(pages[selected]) as f:
        code = f.read()
        exec(code)
else:
    st.write("Please select a page from the navigation menu.")

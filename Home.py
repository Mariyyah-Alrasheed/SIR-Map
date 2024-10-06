import streamlit as st
import leafmap.foliumap as leafmap
st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)
st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
A Streamlit map template
"""


st.sidebar.title("SIR-Map")
st.sidebar.info(markdown)
# logo = "https://i.imgur.com/UbOXYAU.png"

logo = "./image-removebg-preview (1).png"
st.image(logo, width=300)# Customize page title
st.title("Smart Infrastructure and Roads")


st.header("Welcome to SIR!")


st.markdown(
    """
This app utilizes TIFF files to accurately detect and segment roads,
 contributing to proper network mapping. You can use it to draw the network map 
 and explore interactive features designed to enhance your understanding of smart infrastructure.
    """
)

st.sidebar.image(logo)

 
# st.markdown(markdown)



st.image('road_network_image.jpg')

import streamlit as st
from streamlit_option_menu import option_menu
from dotenv import load_dotenv
import os
from Models.SDFv2 import display_SDFv2
from dotenv import load_dotenv

load_dotenv()
# HUGGINGFACE_API_KEY = st.secrets['HUGGINGFACE_API_KEY']
# HUGGINGFACE_API_KEY1 = st.secrets['HUGGINGFACE_API_KEY']
HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API_KEY')
HUGGINGFACE_API_KEY1 = os.getenv('HUGGINGFACE_API_KEY')


st.set_page_config(
        page_title="Generative Image",
)

# Define the sidebar
with st.sidebar:
    # Create the options menu
    selected = option_menu(menu_title="Image-Gen Models",
                           options=["Stable Diffusion XL",],
                           icons=["box", "box","box","box"],
                           menu_icon="boxes",
                           default_index=0
                           )
    
if selected == "Stable Diffusion XL":
    display_SDFv2(HUGGINGFACE_API_KEY)



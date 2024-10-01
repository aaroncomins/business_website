# How to Deploy Your App to Streamlit Community Cloud
# https://www.youtube.com/watch?v=HKoOBiAaHGg&t=127s
import streamlit as st

st.write("Future business website")

import streamlit as st
import pandas as pd
import toml
import json
from PIL import Image
import streamlit_option_menu
from streamlit_option_menu import option_menu
import numpy as np
# from modules.pages import pages

        
class main():
    def __init__(self):
        self.main()
    
    def main(self):
        # st.set_page_config(layout="wide")
        with st.sidebar:
            # st.sidebar.image("media/IDST.png") 
            selected = option_menu(
                menu_title = "Rag, Tin, and Roll Designs",
                options = ["Home",  
                "3D Prints", 
                "Future Page", 
                "Page Information",
                "About"],
                menu_icon = "house",
                default_index = 0,
                )
        page_methods = {
            "Home": self.home,
            "3D Prints": self.prints,
            "Future Page": self.future_page,
            "Page Information": self.page_info,
            "About": self.about
            }
        page_methods[selected]()


if __name__ == '__main__':
    main()

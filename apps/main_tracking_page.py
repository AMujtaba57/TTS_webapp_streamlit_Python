import streamlit as st
from apps.keyword_page import *

class TwitterTracking:
    def __init__(self, menu_items) -> None:
        self.mainSection = st.container()
        self.menu_items = menu_items
        self.page_dict = {}
        self.selected_page = None

        
    def add_page(self, page_name, page_content):
        self.page_dict[page_name] = page_content


    def keywords(self):
        st.write("This is the Keywords page.")
        keyword_action()

    def description(self):
        st.write("This is the description page.")

    def tracker_output(self):
        st.write("This is the tracker_output page.")

    def tracker_input(self):
        st.write("This is the tracker_inpput page.")

    def run(self):
        with self.mainSection:
            st.sidebar.write("<div class='header'><b>Twitter Tracking Service</b></div>", unsafe_allow_html=True)
            
            st.markdown("""
            <style>
                .sidebar .radio {
                    margin: 5px;
                    font-weight: bold;
                }
                .sidebar .radio-box input:checked + label {
                    color: blue;
                }
            </style>
            """, unsafe_allow_html=True)
            
            self.selected_page = st.sidebar.radio("", self.menu_items)
            self.page_dict[self.selected_page]()

            
            st.sidebar.write("<div class='header'><b>Portfolio</b></div>", unsafe_allow_html=True)
            st.sidebar.write("<div class='header' id='admin'><b>Admin</b></div>", unsafe_allow_html=True)
            # Add custom CSS
            st.markdown("""
                <style>
                    .header {
                        margin: 0px;
                        font-size: 18px;
                    }#admin {
                        margin-bottom: 10px;
                    }
                </style>
            """, unsafe_allow_html=True)

    



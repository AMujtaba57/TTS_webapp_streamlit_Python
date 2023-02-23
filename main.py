# import module
import json
import sqlite3
import hashlib
import requests
import streamlit as st
from pathlib import Path
from streamlit_lottie import st_lottie
from streamlit_extras.switch_page_button import switch_page
from streamlit.source_util import _on_pages_changed, get_pages


DEFAULT_PAGE = "main.py"
# SECOND_PAGE_NAME = "main.py"

# all pages request
def get_all_pages():
    default_pages = get_pages(DEFAULT_PAGE)

    pages_path = Path("pages.json")

    if pages_path.exists():
        saved_default_pages = json.loads(pages_path.read_text())
    else:
        saved_default_pages = default_pages.copy()
        pages_path.write_text(json.dumps(default_pages, indent=4))

    return saved_default_pages

# clear all page but not login page
def clear_all_but_first_page():
    current_pages = get_pages(DEFAULT_PAGE)

    if len(current_pages.keys()) == 1:
        return

    get_all_pages()

    # Remove all but the first page
    key, val = list(current_pages.items())[0]
    current_pages.clear()
    current_pages[key] = val

    _on_pages_changed.send()

# show all pages
def show_all_pages():
    current_pages = get_pages(DEFAULT_PAGE)
    saved_pages = get_all_pages()
    for key in saved_pages:
        if key not in current_pages:
            current_pages[key] = saved_pages[key]

    _on_pages_changed.send()

# Hide default page
def hide_page(name: str):
    current_pages = get_pages(DEFAULT_PAGE)

    for key, val in current_pages.items():
        if val["page_name"] == name:
            del current_pages[key]
            _on_pages_changed.send()
            break

# calling only default(login) page  
clear_all_but_first_page()

# session state 
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
    

def main():
    if st.session_state['logged_in'] == False:
        st.write("""
        <style>
            .center {
                display: flex;
                justify-content: center;
            }
            .center img{
                border-radius: 20px;
                width: 300px;
            }
        </style>
        """, unsafe_allow_html=True)
        image_url = """https://images.indianexpress.com/2022/08/Untitled-design-2022-08-13T172027.830-1.jpg"""
        st.write(f'<div class="center"><img src="{image_url}" alt="banner image"/></div> <br>', unsafe_allow_html=True)

        with st.form('Login'):
            st.write("""
            <style>
                input[type=text], input[type=password] {
                    border: 2px solid #ccc;
                    border-radius: 10px;
                    box-sizing: border-box;
                }
                
            </style>
            """, unsafe_allow_html=True)
            st.write("Login")
            username = st.text_input("Username", placeholder="")
            password = st.text_input("Password", type="password")
            login_button = st.form_submit_button('Login')
            
            if login_button:
                if username=='ahmad' and password=='1234':
                    st.session_state["logged_in"] = True
                    st.success("Logged In Sucessfully")
                else:
                    st.warning("Incorrect username Id/Password")
    
    
    if st.session_state["logged_in"] == True:
          # call all page
        show_all_pages()
        hide_page(DEFAULT_PAGE.replace(".py", ""))  # hide first page
        
    else:
        clear_all_but_first_page()  # clear all page but show first page


if __name__ == "__main__":
    main()
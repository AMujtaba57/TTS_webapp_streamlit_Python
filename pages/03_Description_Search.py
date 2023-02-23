import streamlit as st
import pandas as pd


def description_search():
    data = {"Name": ["John", "Mary", "Bob", "Alice"],
        "Age": [25, 30, 40, 35],
        "Gender": ["Male", "Female", "Male", "Female"]}
    df = pd.DataFrame(data)

    st.write("<h3>Search Description</h3>", unsafe_allow_html=True)
    with st.form('Login'):
        st.write("""
        <style>
            input[type=text] {
                border: 2px solid #ccc;
                border-radius: 10px;
                box-sizing: border-box;
            }
            
        </style>
        """, unsafe_allow_html=True)

        search_input = st.text_input("Enter Text to Search", placeholder="Input")
        
        col_btn1, col_btn2, col_radio, col_space1  = st.columns(4)
        primary_btn1 = col_btn1.form_submit_button('Primary')
        primary_btn2 = col_btn2.form_submit_button('Primary2')

        st.write('<style> div[data-testid=column] > div > div > div > div.stRadio > div{flex-direction: row;}</style>', unsafe_allow_html=True)
        col_radio.radio("Search Type", options=['And', 'Or'])
        # select_radio = col_radio.radio("Search Type", options=['And', 'Or'],horizontal=True)

    st.table(df)


if __name__ == '__main__':
    description_search()
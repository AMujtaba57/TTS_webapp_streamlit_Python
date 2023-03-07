import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder


def show_table_disable(df):
    gd = GridOptionsBuilder.from_dataframe(df)
    gd.configure_pagination(enabled=True)
    gd.configure_default_column(editable=False ,groupable=True)
    gd.configure_selection(selection_mode='Single', use_checkbox=False)
    gridoptions = gd.build()
    AgGrid(df, gridOptions=gridoptions, editable=False,
            update_mode=GridUpdateMode.SELECTION_CHANGED,
            allow_unsafe_jscode=True,
            theme='alpine')

def description_search():
    df = pd.read_csv("data/example_data.csv")

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
        
    show_table_disable(df)


if __name__ == '__main__':
    if st.session_state["logged_in"] == True:
        st.sidebar.button("Logout")
        description_search()
    else:
        st.subheader("session has been logout")
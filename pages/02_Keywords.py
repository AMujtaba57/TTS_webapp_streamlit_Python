import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder


editing_enabled = False
data = pd.DataFrame({
        'category': ['Books', 'Movies', 'Games'],
        'keyword': ['Science Fiction', 'Comedy', 'Adventure'],
        'search method': ['Title', 'Actor', 'Genre']
    })

def show_table():
    gd = GridOptionsBuilder.from_dataframe(data)
    gd.configure_pagination(enabled=True)
    gd.configure_default_column(editable=True)
    gd.configure_selection(selection_mode='single', use_checkbox=True)
    gridoptions = gd.build()
    AgGrid(data, gridOptions=gridoptions, editable=True)


def keyword_action():
    
    space1, input2 = st.columns(2)
    st.write("""
    <style>
    input[type=text] {
        padding:  10px 10px;
        border: 1px solid gray;
    }
    </style>
    """, unsafe_allow_html=True)
    disabled_input = input2.text_input("", value=" Current timestamp: date-time", disabled=True)


    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    def show_edit_buttons():
        if col5.button("Add"):
            pass
        if col6.button("Delete"):
            pass
        if col7.button("Save"):
            pass

    if col1.button("Edit"):
        global editing_enabled
        editing_enabled = not editing_enabled
        show_edit_buttons()
        show_table()

        

    col2.button("Reset")
    col3.button("Confirm")
    col4.button("Upload")


if __name__ == "__main__":
    keyword_action()
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder


df = pd.read_csv("data/example_data.csv")

if "editing_enabled" not in st.session_state:
    st.session_state["editing_enabled"] = False

if "show_table_disable" not in st.session_state:
    st.session_state["show_table_disable"] = True

if "show_table_editable" not in st.session_state:
    st.session_state["show_table_editable"] = False


def show_table_editable(df):
    if st.session_state["show_table_editable"] and st.session_state['editing_enabled'] and st.session_state["show_table_disable"] == False:
        gd = GridOptionsBuilder.from_dataframe(df)
        gd.configure_pagination(enabled=True)
        gd.configure_default_column(editable=True ,groupable=True)
        gd.configure_selection(selection_mode='Multiple', use_checkbox=True)
        
        gridoptions = gd.build()
        grid_table = AgGrid(df, gridOptions=gridoptions, editable=True,
                update_mode=GridUpdateMode.SELECTION_CHANGED,
                height=500,
                allow_unsafe_jscode=True,
                theme='alpine')

        return grid_table["selected_rows"]


def show_table_disable(df):
    if st.session_state["show_table_disable"] and st.session_state["show_table_editable"]==False:
        gd = GridOptionsBuilder.from_dataframe(df)
        gd.configure_pagination(enabled=True)
        gd.configure_default_column(editable=False ,groupable=True)
        gd.configure_selection(selection_mode='Single', use_checkbox=False)
        gridoptions = gd.build()
        AgGrid(df, gridOptions=gridoptions, editable=False,
                update_mode=GridUpdateMode.SELECTION_CHANGED,
                height=500,
                allow_unsafe_jscode=True,
                theme='alpine')

    


def tracker_input_action():
    space1, input2 = st.columns(2)
    st.write("""
    <style>
    input[type=text] {
        padding:  10px 10px;
        border: 1px solid gray;
    }
    </style>
    """, unsafe_allow_html=True)
    space1.write("Signal Input")
    disabled_input = input2.text_input("Project Input", value=" Current timestamp: date-time", 
                    disabled=True, label_visibility='visible')


    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    
    edit_btn =  col1.button("Edit")
    reset_btn = col2.button("Reset")
    cnf_btn = col3.button("Confirm")
    upload_btn = col4.button("Upload")

    
    show_table_disable(df)


    if edit_btn:
        st.session_state['editing_enabled'] = True
        st.session_state["show_table_editable"] = True
        st.session_state["show_table_disable"] = False


    if reset_btn and st.session_state['editing_enabled']:
        st.session_state["show_table_disable"] = True
        st.session_state["show_table_editable"] = False
        st.session_state['editing_enabled'] = False
        show_table_disable(df)
        
        

    if st.session_state['editing_enabled']:
        selected_row = show_table_editable(df)
        add_btn = col5.button("Add")
        delete_btn = col6.button("Delete")
        
        if add_btn:
            pass


        if delete_btn:           
            df.drop(selected_row[0]['Unnamed: 0'], axis=0, inplace=True)
            st.session_state['editing_enabled'] = False
            st.session_state["show_table_editable"] = False
            st.session_state["show_table_disable"] = True
            show_table_disable(df)
            
    
    st.write(st.session_state)

if __name__ == "__main__":
    tracker_input_action()
    
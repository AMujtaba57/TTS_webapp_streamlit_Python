import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder

st.button("Upload Selection")

df = pd.read_csv("data/example_data.csv")

gd = GridOptionsBuilder.from_dataframe(df)
gd.configure_pagination(enabled=True)
gd.configure_default_column(editable=True ,groupable=True)


gridoptions = gd.build()
grid_table = AgGrid(df, gridOptions=gridoptions, editable=True,
        update_mode=GridUpdateMode.SELECTION_CHANGED,
        allow_unsafe_jscode=True,
        theme='alpine')




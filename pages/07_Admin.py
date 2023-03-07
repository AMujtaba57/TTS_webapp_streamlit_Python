import streamlit as st

if st.session_state["logged_in"] == True:
    st.sidebar.button("Logout")
    st.write("admin")
else:
        st.subheader("session has been logout")
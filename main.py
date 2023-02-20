import streamlit as st
from apps.login_page import LoginPage
from apps.main_tracking_page import *

def main():
    login_obj = LoginPage()

    if 'loggedIn' not in st.session_state:
        st.session_state['loggedIn'] = False
        login_obj.login()
    
    else:
        if st.session_state['loggedIn']:
            tt_object = TwitterTracking(["Keywords", "Description Search", "Tracker Output", "Tracker Input"])
            tt_object.add_page("Keywords", tt_object.keywords)
            tt_object.add_page("Description Search", tt_object.description)
            tt_object.add_page("Tracker Output", tt_object.tracker_output) 
            tt_object.add_page("Tracker Input", tt_object.tracker_input)    
            tt_object.run() 
            login_obj.show_logout_page() 
        else:
            login_obj.login()

if __name__ == '__main__':
    main()

import streamlit as st

class LoginPage:
    def __init__(self):
        self.logged_in = False
        self.headerSection = st.container()
        self.loginSection = st.container()
        self.logOutSection = st.container()


    def LoggedIn_Clicked(self, userName, password):
        print(type(userName), type(password))
        if userName=="ahmad" and password=="12345":
            st.session_state['loggedIn'] = True
        else:
            st.session_state['loggedIn'] = False
            st.error("Invalid user name or password")

    def login(self):
        with self.loginSection:
            if st.session_state['loggedIn'] == False:
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

                with st.form(key='my_form'):
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
                    username = st.text_input("Username")
                    password = st.text_input("Password", type="password")
                    st.form_submit_button("Login", on_click=self.LoggedIn_Clicked, args=(username, password))

    def LoggedOut_Clicked(self):
        st.session_state['loggedIn'] = False
        
    def show_logout_page(self):
        self.loginSection.empty()
        with self.logOutSection:
            st.sidebar.button ("Log Out", key="logout", on_click=self.LoggedOut_Clicked)

import streamlit as st
import webbrowser

# Set up the username and password
username = "admin"
password = "12345"

# Create the login page
st.title("Login Page")
user_input = st.text_input("Username")
password_input = st.text_input("Password", type="password")

if st.button("Login"):
    # If the credentials are correct, redirect to the specified page
    if user_input == username and password_input == password:
        webbrowser.open_new_tab("http://localhost:8505")
    else:
        # If the credentials are incorrect, display an error message
        st.error("The credentials you entered are incorrect.")

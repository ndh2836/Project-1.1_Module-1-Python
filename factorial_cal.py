import streamlit as st
import os

def fact(n):
    """Calculate the factorial of a non-negative integer n."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)


def load_user():
    """Load the user data from a file."""
    try:
        if os.path.exists("user.txt"):
            with open("user.txt", "r", encoding="utf-8") as f:
                users = [line.strip() for line in f.readlines() if line.strip()]
                return users
        else:
            st.error("File user.txt not found. ")
            return []
    except Exception as e:
        st.error(f"Error loading user data: {e}")
        return []

def login_page():
    """Login Page""
    st.title("Login Page")"""

    # Input username
    username = st.text_input("Input Username:")

    if st.button("Login"):
        if username:
            users = load_user()
            if username in users:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()
            else:
                st.warning("Please input username!")

def factorial_calculator():
    """Factorial Calculator Page"""
    st.title("Factorial Calculator")

    # Display users that logged in
    st.write(f"Logged in as: {st.session_state.username}")

    # Logout button
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()

    st.divider()

    # Input number for factorial calculation
    number = st.number_input("Input a number:", min_value=0, max_value=900)

    if st.button("Calculate Factorial"):
        result = fact(number)
        st.write(f"The factorial of {number} is: {result}")

def greeting_page():
    """Greeting Page"""
    st.title("Welcome to the Factorial Calculator Page!")
    st.write(f"Hello! {st.session_state.username}!")
    st.write("You don't have the permission to access the factorial calculation function.")

    if st.button("Back to login page"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()

def main():
    # Initialize session state
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'username' not in st.session_state:
        st.session_state.username = ""
    if 'show_greeting' not in st.session_state:
        st.session_state.show_greeting = False

    # Page navigation based on login status
    if st.session_state.logged_in:
        factorial_calculator()
    elif st.session_state.show_greeting:
        greeting_page()
    else:
        login_page()

if __name__ == "__main__":
    main()


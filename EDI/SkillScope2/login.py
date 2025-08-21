import streamlit as st
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))
from auth_manager import AuthManager

st.set_page_config(page_title="SkillScope - Login", page_icon="🎯", layout="centered")

def show_login_form():
    st.subheader("Sign In to SkillScope")
    with st.form("login_form"):
        email = st.text_input("Email", placeholder="your.email@example.com")
        password = st.text_input("Password", type="password")
        col1, col2 = st.columns(2)
        with col1:
            login_button = st.form_submit_button("Sign In", type="primary", use_container_width=True)
        with col2:
            if st.form_submit_button("Create Account", use_container_width=True):
                st.session_state.show_signup = True
                st.rerun()
        if login_button:
            if email and password:
                auth_manager = AuthManager()
                user = auth_manager.authenticate_user(email, password)
                if user:
                    st.session_state.authenticated = True
                    st.session_state.user = user
                    st.success(f"Welcome back, {user['name']}!")
                    st.switch_page("Home.py")
                else:
                    st.error("Invalid email or password")
            else:
                st.error("Please enter both email and password")

def show_signup_form():
    st.subheader("Create Your SkillScope Account")
    with st.form("signup_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        current_role = st.text_input("Current Role")
        experience_level = st.selectbox("Experience Level", ["Entry", "Mid", "Senior", "Executive"])
        industry = st.selectbox("Industry", ["Technology", "Finance", "Healthcare", "Marketing", "Other"])
        col1, col2 = st.columns(2)
        with col1:
            signup_button = st.form_submit_button("Create Account", type="primary")
        with col2:
            if st.form_submit_button("Back to Sign In"):
                st.session_state.show_signup = False
                st.rerun()
        if signup_button:
            if not all([name, email, password, confirm_password]):
                st.error("Please fill in all required fields")
            elif password != confirm_password:
                st.error("Passwords do not match")
            else:
                auth_manager = AuthManager()
                if auth_manager.create_user(email, name, password):
                    profile_data = {
                        'current_role': current_role,
                        'experience_level': experience_level,
                        'industry': industry,
                        'signup_date': st.session_state.get('signup_date', None)
                    }
                    user = auth_manager.authenticate_user(email, password)
                    if user:
                        auth_manager.update_user_profile(user['id'], profile_data)
                        st.session_state.authenticated = True
                        st.session_state.user = user
                        st.session_state.user['profile_data'] = profile_data
                        st.success(f"Welcome, {name}!")
                        st.switch_page("Home.py")
                else:
                    st.error("Account creation failed (email may already exist).")

def main():
    if st.session_state.get('authenticated', False):
        st.success("You are already logged in!")
        if st.button("Go to Dashboard", type="primary"):
            st.switch_page("Home.py")
        return
    st.title("🎯 SkillScope")
    st.markdown("### Job Market Skill Trend Analyzer")
    st.markdown("---")
    if st.session_state.get('show_signup', False):
        show_signup_form()
    else:
        show_login_form()

if __name__ == "__main__":
    main()

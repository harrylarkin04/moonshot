import streamlit as st
import time

st.set_page_config(page_title="Quant Moonshot Platform", page_icon="📈", layout="wide")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

def login():
    st.title("Quant Moonshot Platform")
    st.subheader("Secure Access")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        username = st.text_input("Username", placeholder="demo")
        password = st.text_input("Password", type="password", placeholder="quant2026")
        
        if st.button("Login", type="primary", use_container_width=True):
            if username == "demo" and password == "quant2026":
                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()
            else:
                st.error("Invalid credentials")

if not st.session_state.logged_in:
    login()
else:
    st.sidebar.success(f"Logged in as {st.session_state.username}")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()
    
    st.title("Quant Moonshot Platform")
    st.caption("Autonomous quantitative systems • February 2026")

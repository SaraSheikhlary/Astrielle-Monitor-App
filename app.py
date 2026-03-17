import streamlit as st
import librosa
import pandas as pd
import numpy as np
from transformers import pipeline

# --- 1. CONFIG ---
st.set_page_config(layout="wide", page_title="Astrielle AI")

# Initialize the "Logged In" state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# --- 2. LOGIN PAGE ---
if st.session_state.authenticated == False:
    st.markdown("""
        <style>
            .stApp {
                background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.7)), 
                            url('https://images.unsplash.com/photo-1462331940025-496dfbfc7564?auto=format&fit=crop&q=80&w=2000');
                background-size: cover;
                display: flex; align-items: center; justify-content: center;
            }
            .auth-card {
                text-align: center; color: white; padding: 40px;
                background: rgba(0, 0, 0, 0.5); border-radius: 20px;
                backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.1);
            }
        </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown('<div class="auth-card">', unsafe_allow_html=True)
        st.title("🛰️ ASTRIELLE AI")
        st.write("Autonomous Mission Intelligence")
        
        user = st.text_input("Astronaut ID")
        pw = st.text_input("Access Key", type="password")
        
        if st.button("INITIALIZE UPLINK", use_container_width=True):
            st.session_state.authenticated = True
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop() 

# --- 3. MAIN DASHBOARD (This runs after you click Login) ---
else:
    # Sidebar for Logout
    with st.sidebar:
        st.title("👨‍🚀 Command")
        if st.button("TERMINATE SESSION"):
            st.session_state.authenticated = False
            st.rerun()
        st.divider()
        st.write("**System Status:** Nominal")

    # Muted Dashboard Background
    st.markdown("""
        <style>
            .stApp {
                background: linear-gradient(rgba(10,10,15,0.95), rgba(10,10,15,0.95)), 
                            url('https://images.unsplash.com/photo-1462331940025-496dfbfc7564?auto=format&fit=crop&q=80&w=2000');
                background-size: cover;
            }
            .stTabs [data-baseweb="tab-panel"] {
                background: rgba(255, 255, 255, 0.05); padding: 25px; border-radius: 15px;
            }

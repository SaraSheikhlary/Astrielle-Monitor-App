import streamlit as st
import librosa
import pandas as pd
import numpy as np
from transformers import pipeline

# --- 1. CONFIGURATION ---
st.set_page_config(layout="wide", page_title="Astrielle AI")

# Initialize session states
if 'entered' not in st.session_state:
    st.session_state.entered = False
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# --- 2. LOGIN & LANDING PAGE ---
if not st.session_state.entered:
    st.markdown("""
        <style>
            .stApp {
                background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                            url('https://images.unsplash.com/photo-1462331940025-496dfbfc7564?auto=format&fit=crop&q=80&w=2000');
                background-size: cover; display: flex; align-items: center; justify-content: center;
            }
            .landing-card {
                text-align: center; color: white; padding: 40px;
                background: rgba(255, 255, 255, 0.05); border-radius: 30px;
                backdrop-filter: blur(15px); border: 1px solid rgba(255,255,255,0.1);
            }
            .title-text { font-size: 70px; font-weight: 800; letter-spacing: 10px; }
        </style>
        <div class="landing-card">
            <div class="title-text">ASTRIELLE</div>
            <p>Autonomous Edge Intelligence for Deep Space</p>
        </div>
    """, unsafe_allow_html=True)

    # Login / Signup UI
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        choice = st.radio("Access", ["Login", "Create Account"], horizontal=True)
        if choice == "Login":
            st.text_input("Astronaut ID")
            st.text_input("Password", type="password")
            if st.button("INITIALIZE MISSION CONTROL", use_container_width=True):
                st.session_state.entered = True
                st.rerun()
        else:
            st.text_input("Full Name")
            st.text_input("Agency (NASA/SpaceX)")
            st.button("Request Mission Credentials")
    st.stop() 

# --- 3. THE MAIN DASHBOARD (Visible only after Login) ---
else:
    with st.sidebar:
        st.title("🛰️ Command")
        if st.button("Log Out"):
            st.session_state.entered = False
            st.rerun()
        st.divider()

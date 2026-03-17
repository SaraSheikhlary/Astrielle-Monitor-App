import streamlit as st
import librosa
import pandas as pd
import numpy as np
from transformers import pipeline

# --- 1. CONFIGURATION ---
st.set_page_config(layout="wide", page_title="Astrielle AI | Mission Control")

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# --- 2. LOGIN PAGE ---
if not st.session_state.authenticated:
    # Single-line CSS to prevent "unterminated string" errors
    style = '<style>.stApp { background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.8)), url("https://images.unsplash.com/photo-1462331940025-496dfbfc7564?auto=format&fit=crop&q=80&w=2000"); background-size: cover; display: flex; align-items: center; justify-content: center; } .auth-card { text-align: center; color: white; padding: 40px; background: rgba(0, 0, 0, 0.6); border-radius: 20px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.1); }</style>'
    st.markdown(style, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown('<div class="auth-card"><h1>🛰️ ASTRIELLE AI</h1><p>Autonomous Mission Intelligence</p></div>', unsafe_allow_html=True)
        user = st.text_input("Astronaut ID")
        pw = st.text_input("Access Key", type="password")
        if st.button("INITIALIZE UPLINK", use_container_width=True):
            st.session_state.authenticated = True
            st.rerun()
    st.stop() 

# --- 3. MAIN DASHBOARD ---
else:
    with st.sidebar:
        st.title("👨‍🚀 Command")
        if st.button("TERMINATE SESSION"):
            st.session_state.authenticated = False
            st.rerun()
        st.divider()
        st.info("System Status: Nominal")
        st.write("Latency: 0.004ms")

    # Muted Dashboard Theme
    dash_style = '<style>.stApp { background: #0e1117; } .stTabs [data-baseweb="tab-panel"] { background: rgba(255, 255,

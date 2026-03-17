import streamlit as st
import librosa
import pandas as pd
import numpy as np
from transformers import pipeline

# --- 1. CONFIG ---
st.set_page_config(layout="wide", page_title="Astrielle AI | HSI")

# --- 2. SESSION STATE ---
if 'entered' not in st.session_state:
    st.session_state.entered = False

# --- 3. LANDING PAGE (Vibrant & Colorful) ---
if not st.session_state.entered:
    # Using a simpler string format to prevent the syntax error
    landing_css = '''
        <style>
            .stApp {
                background: linear-gradient(rgba(0,0,0,0.2), rgba(0,0,0,0.5)), 
                            url("https://images.unsplash.com/photo-1462331940025-496dfbfc7564?auto=format&fit=crop&q=80&w=2000");
                background-size: cover;
                display: flex; align-items: center; justify-content: center;
            }
            .landing-card {
                text-align: center; color: white; padding: 50px;
                background: rgba(0, 0, 0, 0.3); 
                border-radius: 25px; backdrop-filter: blur(10px); 
                border: 1px solid rgba(255,255,255,0.2);
            }
            .title-text { font-size: 75px; font-weight: 800; letter-spacing: 10px; margin: 0; }
            .subtitle-text { font-size: 20px; color: #00f2ff; letter-spacing: 4px; margin-bottom: 30px; }
        </style>
        <div class="landing-card">
            <div class="title-text">ASTRIELLE</div>
            <div class="subtitle-text">AUTONOMOUS EDGE INTELLIGENCE</div>
            <p style="max-width:500px; margin:0 auto; font-size:18px; opacity:0.9;">
                Localized AI diagnostics for Deep Space Human-Systems Integration.
            </p>
        </div>
    '''
    st.markdown(landing_css, unsafe_allow_html=True)

    if st.button("INITIALIZE MISSION CONTROL", use_container_width=True):
        st.session_state.entered = True
        st.rerun()
    st.stop() 

# --- 4. THE MAIN DASHBOARD (Darker & Muted) ---
else:
    with st.sidebar:
        st.title("🛰️ Command")
        if st.button("Log Out"):
            st.session_state.entered = False
            st.rerun()
        st.divider()
        st.write("**Latency:** 0.004ms")

    # Muted Dashboard CSS
    dashboard_css = '''
        <style>
            .stApp {
                background: linear-gradient(rgba(10, 10, 15, 0.93), rgba(10, 10, 15, 0.93)), 
                            url("https://images.unsplash.com/photo-1462331940025-496dfbfc7564?auto=format&fit=crop&q=80&w=2000");
                background-size: cover;
                background-attachment: fixed;
            }
            .stTabs [data-baseweb="tab-panel"] {
                padding: 25px; border-radius: 15px;
                background: rgba(255, 255, 255, 0.04);
                backdrop-filter: blur(15px);
                border: 1px solid rgba(255, 255,

import streamlit as st
import librosa
import pandas as pd
import numpy as np
from transformers import pipeline

# --- 1. CONFIGURATION ---
st.set_page_config(layout="wide", page_title="Astrielle AI | HSI")

# --- 2. SESSION STATE ---
if 'entered' not in st.session_state:
    st.session_state.entered = False
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# --- 3. THE SPLASH SCREEN & LOGIN ---
if not st.session_state.entered:
    st.markdown("""
        <style>
            .stApp {
                background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                            url('https://images.unsplash.com/photo-1462331940025-496dfbfc7564?auto=format&fit=crop&q=80&w=2000');
                background-size: cover;
                display: flex; align-items: center; justify-content: center;
            }
            .landing-card {
                text-align: center; color: white; padding: 40px;
                background: rgba(255, 255, 255, 0.05); 
                border-radius: 30px;
                backdrop-filter: blur(15px); 
                border: 1px solid rgba(255,255,255,0.1);
            }
            .title-text { font-size: clamp(40px, 8vw, 85px); font-weight: 800; letter-spacing: 12px; margin-bottom: 0px; }
            .subtitle-text { font-size: 20px; color: #00f2ff; letter-spacing: 3px; margin-bottom: 20px; }
        </style>
        <div class="landing-card">
            <div class="title-text">ASTRIELLE</div>
            <div class="subtitle-text">Autonomous Edge Intelligence</div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if not st.session_state.authenticated:
            mode = st.radio("Access Control", ["Sign In", "Create Mission Account"], horizontal=True)
            if mode == "Sign In":
                st.text_input("Astronaut ID")
                st.text_input("Access Key", type="password")
                if st.button("INITIALIZE SECURE UPLINK", use_container_width=True):
                    st.session_state.authenticated = True
                    st.rerun()
            else:
                st.text_input("Full Name")
                st.text_input("Agency (NASA/SpaceX)")
                st.button("REQUEST CREDENTIALS")
        else:
            if st.button("ENTER MISSION CONTROL", use_container_width=True):
                st.session_state.entered = True
                st.rerun()
    st.stop() 

# --- 4. THE MAIN DASHBOARD ---
else:
    with st.sidebar:
        st.title("🛰️ Command Center")
        st.write("**Astro_01** | Mission Active")
        if st.button("Log Out / Reset View"):
            st.session_state.entered = False
            st.session_state.authenticated = False
            st.rerun()
        st.divider()
        st.write("**System:** Edge Computing")
        st.write("**Local Latency:** 0.004ms")
        st.write("**Earth Sync:** 22m Delay (Bypassed)")

    # THEME GUARD CSS
    st.markdown("""
        <style>
            .stApp {
                background: url('https://images.unsplash.com/photo-1462331940025-496dfbfc7564?auto=format&fit=crop&q=80&w=2000');
                background-size: cover;
                background-attachment: fixed;
            }
            [data-theme="dark"] .stApp {
                background-image: linear-gradient(rgba(14, 17, 23, 0.85), rgba(14, 17, 23, 0.85)), 
                                  url('https://images.unsplash.com/photo-1462331940025-496dfbfc7564?auto=format&fit=crop&q=80&w=2000');
            }
            .stTabs [data-baseweb="tab-panel"] {
                padding: 30px; border-radius: 20px; backdrop-filter: blur(20px);
                border: 1px solid rgba(128, 128, 128, 0.2); margin-top: 20px;
                background: rgba(30, 30, 30, 0.65);
            }
            .footer {
                position: fixed; left: 0; bottom: 0; width: 100%;
                text-align: center; font-size: 0.8em; padding: 12px 0; z-index: 999;
                background: black; color: white; border-top: 1px solid #333;
            }
        </style>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["🎙️ Vocal AI", "🛰️ Structural Health", "🧠 HSI Synergy", "📑 Mission Summary"])

    with tab1:
        st.title("✨ Vocal Biomarker Monitor")
        @st.cache_resource
        def load_voice_model():
            return pipeline("audio-classification", model="superb/wav2vec2-base-superb-er")

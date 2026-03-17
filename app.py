import streamlit as st
import librosa
import pandas as pd
import numpy as np
from transformers import pipeline

# --- 1. CONFIG ---
st.set_page_config(layout="wide", page_title="Astrielle AI")

# --- 2. INITIALIZE SESSION STATE ---
# This part is CRITICAL. It tells the app "Remember I clicked Enter!"
if 'entered' not in st.session_state:
    st.session_state.entered = False

# --- 3. THE SPLASH SCREEN (Logic) ---
if not st.session_state.entered:
    # Everything inside this 'if' block is ONLY the Landing Page
    st.markdown("""
        <style>
            .stApp {
                background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), 
                            url('https://images.unsplash.com/photo-1462331940025-496dfbfc7564?auto=format&fit=crop&q=80&w=2000');
                background-size: cover;
                display: flex; align-items: center; justify-content: center;
            }
            .landing-card {
                text-align: center; color: white; padding: 50px;
                background: rgba(0,0,0,0.4); border-radius: 20px;
                backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.1);
            }
            h1 { font-size: 70px; letter-spacing: 8px; margin-bottom: 10px; }
            p { font-size: 20px; opacity: 0.8; margin-bottom: 40px; }
        </style>
        <div class="landing-card">
            <h1>ASTRIELLE AI</h1>
            <p>Autonomous Edge Intelligence for Deep Space Missions</p>
        </div>
    """, unsafe_allow_html=True)

    # When this button is clicked, st.session_state.entered becomes True
    if st.button("ENTER MISSION CONTROL", use_container_width=True):
        st.session_state.entered = True
        st.rerun() # This REFRESHES the page to show the dashboard!

else:
    # --- 4. THE MAIN DASHBOARD (Only runs if st.session_state.entered is True) ---
    
    # Custom Theme CSS (Dark mode font = white, Light mode font = black)
    st.markdown("""
        <style>
            [data-theme="light"] { color: #000000 !important; }
            [data-theme="dark"] { color: #ffffff !important; }
            .stApp {
                background: linear-gradient(rgba(14, 17, 23, 0.85), rgba(14, 17, 23, 0.85)), 
                            url('https://images.unsplash.com/photo-1462331940025-496dfbfc7564?auto=format&fit=crop&q=80&w=2000');
                background-size: cover;
            }
        </style>
    """, unsafe_allow_html=True)

    # --- TABS ---
    tab1, tab2, tab3 = st.tabs([
        "🎙️ Vocal Biomarker Monitor", 
        "🛰️ Structural Health Monitoring", 
        "🧠 Human-Systems Integration"
    ])

    with tab1:
        st.title("Human State Analysis")
        # PASTE YOUR VOCAL AI CODE HERE
        st.write("Vocal Analysis active...")

    with tab2:
        st.title("Asset Integrity Analysis")
        # PASTE YOUR STRUCTURAL AI CODE HERE
        st.write("Structural Monitoring active...")

    with tab3:
        st.title("HSI: Synergy Guardian")
        # THIS IS THE REAL-TIME MARS DELAY SOLUTION
        st.info("Local Edge Computing Mode: Active. (0ms Latency)")
        st.write("This dashboard provides instant feedback, bypassing the 20-minute Earth communication delay.")

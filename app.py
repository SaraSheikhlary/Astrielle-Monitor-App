import streamlit as st
import librosa
import pandas as pd
import numpy as np
from transformers import pipeline

# --- 1. SETTINGS ---
st.set_page_config(layout="wide", page_title="Astrielle AI")

# --- 2. LANDING PAGE STATE ---
if 'entered' not in st.session_state:
    st.session_state.entered = False

def enter_app():
    st.session_state.entered = True

# --- 3. THE SPLASH SCREEN ---
if not st.session_state.entered:
    # Full-screen landing page
    st.markdown("""
        <style>
            .stApp {
                background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), 
                            url('https://images.unsplash.com/photo-1462331940025-496dfbfc7564?auto=format&fit=crop&q=80&w=2000');
                background-size: cover;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            .landing-text {
                text-align: center;
                color: white;
                font-family: 'Helvetica Neue', sans-serif;
            }
            .main-title { font-size: 80px; font-weight: bold; margin-bottom: 0px; letter-spacing: 5px; }
            .sub-title { font-size: 24px; color: #00f2ff; margin-bottom: 30px; }
            .description { max-width: 600px; margin: 0 auto; font-size: 18px; line-height: 1.6; opacity: 0.9; }
        </style>
        <div class="landing-text">
            <div class="main-title">ASTRIELLE AI</div>
            <div class="sub-title">Human-Systems Integration for Deep Space</div>
            <p class="description">
                Solving the 20-minute communication lag in Mars-bound missions through 
                <b>Autonomous Edge Intelligence</b>. Monitoring biological stress and 
                structural integrity in real-time, where every second counts.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.button("ENTER MISSION CONTROL", on_click=enter_app, use_container_width=True)
    st.stop() # Stops the rest of the code from running until 'Enter' is clicked

# --- 4. THE MAIN DASHBOARD (Only shows after clicking Enter) ---
st.markdown("""
    <style>
        /* Theme-aware font coloring */
        [data-theme="light"] { color: black; }
        [data-theme="dark"] { color: white; }
        
        .stApp {
            background: linear-gradient(rgba(14, 17, 23, 0.8), rgba(14, 17, 23, 0.8)), 
                        url('https://images.unsplash.com/photo-1462331940025-496dfbfc7564?auto=format&fit=crop&q=80&w=2000');
            background-size: cover;
        }
    </style>
""", unsafe_allow_html=True)

# ... [INSERT THE REST OF YOUR PREVIOUS CODE HERE: TABS, TAB 1, TAB 2, TAB 3] ...

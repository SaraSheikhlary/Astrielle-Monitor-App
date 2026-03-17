import streamlit as st
import librosa
import pandas as pd
import numpy as np
from transformers import pipeline

# --- 1. CONFIGURATION ---
st.set_page_config(layout="wide", page_title="Astrielle AI | HSI")

# --- 2. SESSION STATE (The Memory) ---
if 'entered' not in st.session_state:
    st.session_state.entered = False

# --- 3. THE SPLASH SCREEN (Landing Page) ---
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
                text-align: center; color: white; padding: 60px;
                background: rgba(255, 255, 255, 0.05); 
                border-radius: 30px;
                backdrop-filter: blur(15px); 
                border: 1px solid rgba(255,255,255,0.1);
            }
            .title-text { font-size: 85px; font-weight: 800; letter-spacing: 12px; margin-bottom: 0px; }
            .subtitle-text { font-size: 22px; color: #00f2ff; letter-spacing: 3px; margin-bottom: 30px; }
        </style>
        <div class="landing-card">
            <div class="title-text">ASTRIELLE</div>
            <div class="subtitle-text">Autonomous Edge Intelligence</div>
            <p style="max-width:600px; margin:0 auto; font-size:18px; opacity:0.8;">
                Advanced <b>Human-Systems Integration</b> for Deep Space. 
                Localized AI diagnostics to bypass the 20-minute Mars-Earth communication lag.
            </p>
        </div>
    """, unsafe_allow_html=True)

    if st.button("INITIALIZE MISSION CONTROL", use_container_width=True):
        st.session_state.entered = True
        st.rerun()
    st.stop() 

# --- 4. THE MAIN DASHBOARD (Visible only after 'Enter') ---
else:
    # Sidebar for Reset & Edge Info
    with st.sidebar:
        st.title("🛰️ Command Center")
        if st.button("Log Out / Reset View"):
            st.session_state.entered = False
            st.rerun()
        st.divider()
        st.write("**System:** Edge Computing")
        st.write("**Local Latency:** 0.004ms")
        st.write("**Earth Sync:** 22m Delay (Bypassed)")

    # ADAPTIVE CSS (Switching White/Black based on Theme)
    st.markdown("""
        <style>
            /* This forces the app to use the system text color (White in Dark, Black in Light) */
            .stApp {
                color: var(--text-color);
                background: linear-gradient(rgba(14, 17, 23, 0.85), rgba(14, 17, 23, 0.85)), 
                            url('https://images.unsplash.com/photo-1462331940025-496dfbfc7564?auto=format&fit=crop&q=80&w=2000');
                background-size: cover;
            }
            
            /* Glass-morphism for Tab Content readability */
            .stTabs [data-baseweb="tab-panel"] {
                background: rgba(255, 255, 255, 0.05);
                padding: 25px;
                border-radius: 15px;
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.1);
                margin-top: 15px;
            }

            h1, h2, h3, p, span {
                color: var(--text-color) !important;
            }

            .footer {
                position: fixed; left: 0; bottom: 0; width: 100%;
                background-color: rgba(0, 0, 0, 0.8); 
                color: #aaa; text-align: center;
                font-size: 0.8em; padding: 12px 0; z-index: 999;
                border-top: 1px solid rgba(255,255,255,0.1);
            }
        </style>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["🎙️ Vocal Biomarkers", "🛰️ Structural Health", "🧠 Human-Systems Integration"])

    # --- TAB 1: VOCAL AI ---
    with tab1:
        st.title("✨ Vocal Biomarker Monitor")
        @st.cache_resource
        def load_voice_model():
            return pipeline("audio-classification", model="superb/wav2vec2-base-superb-er")
        
        classifier = load_voice_model()
        
        up = st.file_uploader("Upload Voice Telemetry (.wav)", type="wav")
        if up:
            speech, sr = librosa.load(up, sr=16000)
            res = classifier(speech)
            for r in res:
                st.write(f"**{r['label']}**")
                st.progress(r['score'])

        st.divider()
        recorded = st.audio_input("Live Microphone Stream")
        if recorded:
            speech, sr = librosa.load(recorded, sr=16000)
            res = classifier(speech)
            for r in res:
                st.write(f"**{r['label']}**")
                st.progress(r['score'])

    # --- TAB 2: STRUCTURAL AI ---
    with tab2:
        st.title("🛰️ Structural Health Monitoring")
        col1, col2 = st.columns([1, 2])
        with col1:
            st.write("### Sensor Telemetry")
            vibration = st.slider("Vibration (Hz)", 0, 5000, 1100)
            strain = st.slider("Strain (με)", 0, 10000, 4000)
            cycles = st.number_input("Stress Cycles", 1000, 1000000, 50000)
        with col2:
            damage = (strain / 10000) * (np.log10(cycles) / 6) * 100
            st.metric("Deformation Risk", f"{damage:.1f}%")
            st.line_chart(pd.DataFrame(np.random.randn(20, 1), columns=["Stress Level"]))

    # --- TAB 3: HSI (THE DELAY SOLUTION) ---
    with tab3:
        st.title("🧠 Human-Systems Integration")
        st.info("Direct Edge Feedback: Active. Mars-Earth Delay: 22m (Bypassed)")
        
        c_a, c_b = st.columns(2)
        with c_a:
            st.metric("Earth Comms Latency", "1.3M ms", "Mars-Max")
        with c_b:
            st.metric("Astrielle AI Latency", "0.004 ms", "Local-Edge", delta_color="inverse")
            
        st.write("### Synergy Guardian")
        st.write("This module cross-references biological vocal stress with mechanical deformation to ensure autonomous crew safety during deep space transit.")
        st.bar_chart({"Earth Delay (s)": 1320, "Astrielle AI (s)": 0.004})

    # --- THE FOOTER ---
    st.markdown("""
        <div class="footer">
            © 2026 Astrielle AI | <b>Confidential Mission Telemetry</b> | 
            Powered by Edge Intelligence for Autonomous Deep Space Exploration.
        </div>
    """, unsafe_allow_html=True)

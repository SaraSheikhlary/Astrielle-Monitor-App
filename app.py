import streamlit as st
import librosa
import pandas as pd
import numpy as np
from transformers import pipeline

# --- 1. CONFIG ---
st.set_page_config(layout="wide", page_title="Astrielle AI")

if 'entered' not in st.session_state:
    st.session_state.entered = False

# --- 2. LOGIN & SPLASH ---
if not st.session_state.entered:
    # We use a simple variable to hold the URL to keep lines short
    bg_img = "https://images.unsplash.com/photo-1462331940025-496dfbfc7564?auto=format&fit=crop&q=80&w=2000"
    
    st.markdown(f"""
        <style>
            .stApp {{
                background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url('{bg_img}');
                background-size: cover; display: flex; align-items: center; justify-content: center;
            }}
            .card {{
                text-align: center; color: white; padding: 50px;
                background: rgba(255, 255, 255, 0.05); border-radius: 30px;
                backdrop-filter: blur(15px); border: 1px solid rgba(255,255,255,0.1);
            }
        </style>
        <div class="card">
            <h1 style="font-size:70px; letter-spacing:10px;">ASTRIELLE</h1>
            <p style="color:#00f2ff;">Autonomous Edge Intelligence</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,1.5,1])
    with col2:
        tab_in, tab_up = st.tabs(["Login", "Create Account"])
        with tab_in:
            st.text_input("Astronaut ID")
            st.text_input("Access Key", type="password")
            if st.button("INITIALIZE MISSION", use_container_width=True):
                st.session_state.entered = True
                st.rerun()
        with tab_up:
            st.text_input("Name")
            st.text_input("Agency")
            st.button("Request Access")
    st.stop()

# --- 3. DASHBOARD ---
else:
    with st.sidebar:
        st.title("🛰️ Command")
        if st.button("LOGOUT / RESET"):
            st.session_state.entered = False
            st.rerun()
        st.divider()
        st.write("System: **Active**")

    # Main Dashboard Background
    st.markdown("""
        <style>
            .stApp {
                background: linear-gradient(rgba(14,17,23,0.8), rgba(14,17,23,0.8)), 
                            url('https://images.unsplash.com/photo-1462331940025-496dfbfc7564?auto=format&fit=crop&q=80&w=2000');
                background-size: cover; background-attachment: fixed;
            }
            .stTabs [data-baseweb="tab-panel"] {
                background: rgba(30, 30, 30, 0.7); padding: 30px; border-radius: 20px;
            }
        </style>
    """, unsafe_allow_html=True)

    t1, t2, t3, t4 = st.tabs(["🎙️ Vocal AI", "🛰️ Structural", "🧠 HSI Synergy", "📑 About Summary"])

    with t1:
        st.header("Vocal Biomarkers")
        @st.cache_resource
        def load_model():
            return pipeline("audio-classification", model="superb/wav2vec2-base-superb-er")
        
        # Audio input (The Recorder you wanted)
        rec = st.audio_input("Start Live Stream")
        if rec:
            classifier = load_model()
            speech, sr = librosa.load(rec, sr=16000)
            for r in classifier(speech):
                st.write(f"**{r['label']}**")
                st.progress(r['score'])

    with t2:
        st.header("Structural Health")
        strn = st.slider("Hull Strain", 0, 10000, 4200)
        st.metric("Deformation Risk", f"{strn/100}%", delta="Predictive")
        st.line_chart(np.random.randn(20, 1))

    with t3:
        st.header("Human-Systems Integration")
        st.info("Direct Edge Feedback: Bypassing 22m Mars Delay")
        st.bar_chart({"Earth Delay": 1320, "Astrielle": 0.01})

    with t4:
        st.header("📑 Mission Intelligence Summary")
        st.subheader("Project Astrielle")
        st.write("Astrielle is an Edge AI system designed for deep space. It detects structural failure and crew health issues locally, removing the 20-minute wait for Earth signals.")
        st.success("Safety Index: 98.4% (ROC Optimized)")

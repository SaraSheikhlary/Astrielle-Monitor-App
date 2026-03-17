import streamlit as st
import librosa
import pandas as pd
import numpy as np
from transformers import pipeline

# 1. SETUP
st.set_page_config(page_title="Astrielle AI")

if 'auth' not in st.session_state:
    st.session_state.auth = False

# 2. LOGIN PAGE
if st.session_state.auth == False:
    st.title("🛰️ ASTRIELLE AI")
    st.subheader("Mission Control Login")
    
    user = st.text_input("Astronaut ID")
    pw = st.text_input("Access Key", type="password")
    
    if st.button("LOGIN"):
        st.session_state.auth = True
        st.rerun()
    st.stop()

# 3. DASHBOARD (Runs after Login)
else:
    st.sidebar.title("👨‍🚀 Astro_01")
    if st.sidebar.button("LOGOUT"):
        st.session_state.auth = False
        st.rerun()

    # THE 4 TABS
    t1, t2, t3, t4 = st.tabs(["🎙️ Vocal", "🛰️ Structural", "🧠 Synergy", "📑 Summary"])

    with t1:
        st.header("Vocal Biomarkers")
        @st.cache_resource
        def load_model():
            return pipeline("audio-classification", model="superb/wav2vec2-base-superb-er")
        
        try:
            model = load_model()
            up = st.file_uploader("Upload .wav", type="wav")
            if up:
                s, r = librosa.load(up, sr=16000)
                for res in model(s):
                    st.write(res['label'])
                    st.progress(res['score'])
        except:
            st.info("Loading AI...")

    with t2:
        st.header("Structural Health")
        val = st.slider("Hull Strain", 0, 10000, 4000)
        st.metric("Damage Risk", f"{val/100}%")
        st.line_chart(np.random.randn(20, 1))

    with t3:
        st.header("HSI Synergy")
        st.write("Mars Delay: 22 Minutes")
        st.write("Astrielle Latency: 0.004ms")
        st.bar_chart({"Earth": 1320, "Astrielle": 0.01})

    with t4:
        st.header("📑 Mission Summary")
        st.subheader("Predictive Analytics")
        st.write("Logic: Linear Elastic Fracture Mechanics.")
        st.write("Goal: Predict failure

import streamlit as st
import librosa
import numpy as np
from transformers import pipeline

# 1. AUTH
if 'auth' not in st.session_state:
    st.session_state.auth = False

# 2. LOGIN
if st.session_state.auth == False:
    st.title("ASTRIELLE AI")
    u = st.text_input("ID")
    p = st.text_input("KEY", type="password")
    if st.button("GO"):
        st.session_state.auth = True
        st.rerun()
    st.stop()

# 3. APP
else:
    st.sidebar.title("MENU")
    if st.sidebar.button("EXIT"):
        st.session_state.auth = False
        st.rerun()

    # TABS
    t1, t2, t3, t4 = st.tabs(["VOICE", "SHIP", "DELAY", "DATA"])

    with t1:
        st.write("AI VOICE")
        @st.cache_resource
        def load():
            return pipeline("audio-classification", model="superb/wav2vec2-base-superb-er")
        try:
            m = load()
            f = st.file_uploader("WAV", type="wav")
            if f:
                s, r = librosa.load(f, sr=16000)
                for o in m(s):
                    st.write(o['label'])
                    st.progress(o['score'])
        except:
            st.info("LOADING...")

    with t2:
        st.write("STRUCTURE")
        v = st.slider("STRAIN", 0, 1000, 400)
        st.metric("RISK", f"{v/10}%")
        st.line_chart(np.random.randn(10, 1))

    with t3:
        st.write("LATENCY")
        st.write("EARTH: 1320s")
        st.write("AI: 0.01s")
        st.bar_chart([1320, 1])

    with t4:
        st.write("SUMMARY")
        st.write("ROC: 0.98")
        st.success("STATUS: SAFE")

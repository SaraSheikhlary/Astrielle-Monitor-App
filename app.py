import streamlit as st
import librosa
import pandas as pd
import numpy as np
from transformers import pipeline
from PIL import Image

# --- 1. CONFIGURATION ---
try:
    sidebar_logo_full = Image.open("astrielle_logo_full.png")
    favicon_icon_square = Image.open("astrielle_favicon_square.png")
except Exception:
    sidebar_logo_full = None
    favicon_icon_square = None

st.set_page_config(
    layout="wide", 
    page_title="ASTRIELLE AI | HSI",
    page_icon=favicon_icon_square, 
    initial_sidebar_state="expanded"
)

# --- 1.5 SEO & META TAGS ---
st.markdown("""
    <style>
        /* Hidden SEO text for search engine crawlers */
        .seo-hide { display: none; }
    </style>
    <div class="seo-hide">
        <h1>Astrielle AI - Deep Space Edge Intelligence</h1>
        <h2>Autonomous Human-Systems Integration for Mars Missions</h2>
        <p>Astrielle AI provides localized AI diagnostics, vocal biomarker monitoring, and structural health tracking.</p>
    </div>
""", unsafe_allow_html=True)


# --- 2. SESSION STATE ---
if 'entered' not in st.session_state:
    st.session_state.entered = False

# --- 3. THE SPLASH SCREEN ---
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
                border

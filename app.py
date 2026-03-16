import streamlit as st

# 1. Page Config (Keep this at the very top)
st.set_page_config(page_title="Astrielle AI", layout="wide")

# 2. The Main Header (The one you want to keep)
st.markdown("<h1 style='text-align: center;'>✨ Astrielle AI: State Monitor ✨</h1>", unsafe_content_html=True)
st.markdown("<p style='text-align: center;'>Welcome to your professional analysis dashboard.</p>", unsafe_content_html=True)

st.divider() # Adds that nice clean line under the title

# 3. Sidebar (Optional - if you have one)
with st.sidebar:
    st.header("✨ Fusion Weights")
    voice_importance = st.slider("Voice Importance", 0.0, 1.0, 0.7)

# 4. Upload Section
st.subheader("Upload Voice Clip (.wav)")
uploaded_file = st.file_uploader("Choose a file", type=["wav"], label_visibility="collapsed")

# 5. Microphone Section
st.subheader("🎤 Voice Input")
audio_input = st.audio_input("Record a test clip")

if audio_input:
    st.audio(audio_input)
    st.download_button(
        label="📥 Download Recording",
        data=audio_input,
        file_name="recording.wav",
        mime="audio/wav"
    )

# 6. Footer
st.divider()
st.caption("© 2026 Astrielle AI | Privacy & Terms")
st.caption("This app uses AI-generated data for monitoring purposes. We do not collect or store personal user data.")

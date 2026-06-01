import streamlit as st
import base64

def get_image_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def header_home():
    img_base64 = get_image_base64("src/assets/SnapLogo.png")
    
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center;">
            <img src="data:image/png;base64,{img_base64}" width="100" style="
                border-radius: 20px; margin:20px;">
            <h1 style="margin:0; padding:0; text-align:center;">SNAP</h1>
            <h1 style="margin:0; padding:0; text-align:center;">CLASS</h1>
        </div>
    """, unsafe_allow_html=True)
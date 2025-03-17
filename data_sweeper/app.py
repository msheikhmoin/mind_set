import streamlit as st
import json
import pandas as pd
import random
import os

# File Paths
affirmations_file = "data/affirmations.json"
user_data_file = "data/user_data.csv"
css_file = "style/style.css"  # Ensure correct path

# Load affirmations
if os.path.exists(affirmations_file):
    with open(affirmations_file, "r") as file:
        affirmations = json.load(file)
else:
    affirmations = ["Believe in yourself!", "Stay positive!", "Every challenge is an opportunity to grow!"]

# Ensure CSV file exists
if not os.path.exists(user_data_file):
    pd.DataFrame(columns=["Negative", "Positive"]).to_csv(user_data_file, index=False)

st.set_page_config(page_title="🧹 Data Sweeper", layout="wide")

# Load Custom CSS
if os.path.exists(css_file):
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Title with better styling
st.markdown("<h1 style='color: #333; text-align: center;'>🧹 Data Sweeper - Clear Your Negative Thoughts</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #555; text-align: center;'>Convert negative self-talk into positive energy! 🚀</h2>", unsafe_allow_html=True)

# User Input
negative_thought = st.text_area("✍ Write your negative thought here:")

if st.button("Sweep It Away!"):
    if negative_thought.strip():
        positive_replacement = random.choice(affirmations)

        # Read existing data
        df = pd.read_csv(user_data_file)
        
        # Append new data safely
        new_data = pd.DataFrame({"Negative": [negative_thought], "Positive": [positive_replacement]})
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_csv(user_data_file, index=False)

        # Display Thoughts
        st.markdown(f'<div class="thought-box">❌ <b>Negative:</b> {negative_thought}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="positive-box">✅ <b>Positive:</b> {positive_replacement}</div>', unsafe_allow_html=True)

    else:
        st.warning("⚠️ Please enter a thought before sweeping!")

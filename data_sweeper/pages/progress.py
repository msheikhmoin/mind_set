import streamlit as st
import pandas as pd

user_data_file = "data/user_data.csv"

st.title("📊 Your Data Sweeper Progress")

df = pd.read_csv(user_data_file)

if not df.empty:
    st.write(f"### 🌟 You've swept away {len(df)} negative thoughts!")
    st.dataframe(df)
else:
    st.write("No data yet. Start sweeping now! 🚀")

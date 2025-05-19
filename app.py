import streamlit as st
import pandas as pd
import os
from datetime import date
from utils import predict_mood, visualize_mood

st.title("🧠 Mood & Wellness Tracker")
st.write("Track your mood, habits, and get AI-powered feedback.")

# Input form
with st.form("mood_form"):
    mood = st.slider("Your mood today (1=bad, 5=great)", 1, 5)
    sleep = st.slider("Hours of sleep", 0, 12)
    stress = st.slider("Stress level (1=low, 5=high)", 1, 5)
    notes = st.text_area("Optional journal/thoughts")
    submitted = st.form_submit_button("Log Entry")

if submitted:
    new_data = {
        "date": date.today(),
        "mood": mood,
        "sleep": sleep,
        "stress": stress,
        "notes": notes
    }
    df = pd.read_csv("mood_data.csv") if os.path.exists("mood_data.csv") else pd.DataFrame(columns=new_data.keys())
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    df.to_csv("mood_data.csv", index=False)
    st.success("Entry saved!")

# Visualize data
if os.path.exists("mood_data.csv"):
    df = pd.read_csv("mood_data.csv")
    st.subheader("📈 Mood Over Time")
    visualize_mood(df)

    st.subheader("🔍 Mood Insight")
    if submitted:
        insight = predict_mood(sleep, stress)
        st.info(insight)
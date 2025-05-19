import matplotlib.pyplot as plt
import streamlit as st
import pickle

def visualize_mood(df):
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')
    plt.figure(figsize=(10, 4))
    plt.plot(df['date'], df['mood'], marker='o', label='Mood')
    plt.plot(df['date'], df['sleep'], marker='x', linestyle='--', label='Sleep (hrs)')
    plt.legend()
    plt.xticks(rotation=45)
    plt.title("Mood & Sleep Trends")
    plt.tight_layout()
    st.pyplot(plt)

def predict_mood(sleep, stress):
    try:
        with open("mood_model.pkl", "rb") as f:
            model = pickle.load(f)
        pred = model.predict([[sleep, stress]])[0]
        return "🙂 Likely Good Mood" if pred else "😕 Might Feel Low"
    except:
        return "No prediction available (model missing)."
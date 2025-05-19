# 🧠 Mental Health Mood Tracker with ML Insights

A simple, interactive app to track daily mood, sleep, stress, and journaling — with AI-powered mood insights and trend visualization.

## Features
- Daily logging of mood, sleep, stress, notes
- Trend visualization over time
- ML model predicts mood quality based on inputs
- Optional journaling field

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## File Descriptions
- `app.py`: Main Streamlit app
- `utils.py`: Helper functions for ML and visualization
- `mood_data.csv`: Local storage of user entries
- `mood_model.pkl`: (Optional) Pretrained ML model

## Optional
Train your own model:
```bash
python train_model.py
```
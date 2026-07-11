import streamlit as st
import pandas as pd
import joblib
import re
from urllib.parse import urlparse

# Feature Extraction Function (Must match the training script exactly)
def extract_features(url):
    features = {}
    features['url_length'] = len(url)
    features['num_dots'] = url.count('.')
    features['num_hyphens'] = url.count('-')
    features['num_digits'] = sum(c.isdigit() for c in url)
    
    parsed_url = urlparse(url)
    features['has_https'] = 1 if parsed_url.scheme == 'https' else 0
    features['has_ip'] = 1 if re.match(r'\d+\.\d+\.\d+\.\d+', parsed_url.netloc) else 0
    
    suspicious_words = ['login', 'update', 'free', 'urgent', 'secure', 'billing']
    for word in suspicious_words:
        features[f'has_{word}'] = 1 if word in url.lower() else 0
        
    return features

# Load the trained model
@st.cache_resource
def load_model():
    try:
        return joblib.load('models/phishing_rf_model.pkl')
    except:
        return None

model = load_model()

# Streamlit UI
st.set_page_config(page_title="Phishing URL Detector", page_icon="🛡️")

st.title("🛡️ AI Phishing & Malware URL Detector")
st.write("Enter a suspicious link below to calculate the probability of it being a cyber threat.")

url_input = st.text_input("Enter URL:", placeholder="e.g., http://secure-update-account-now.com")

if st.button("Analyze URL"):
    if not url_input:
        st.warning("Please enter a URL to analyze.")
    elif model is None:
        st.error("Model not found! Please run train_model.py first.")
    else:
        # Extract features and predict
        features = extract_features(url_input)
        features_df = pd.DataFrame([features])
        
        prediction = model.predict(features_df)[0]
        probability = model.predict_proba(features_df)[0][1] # Probability of being class 1 (Phishing)
        
        st.divider()
        
        # Display Results
        if prediction == 1:
            st.error(f"🚨 **DANGER:** This URL is likely a Phishing attempt or malicious.")
        else:
            st.success(f"✅ **SAFE:** This URL appears to be safe.")
            
        st.metric(label="Threat Probability Score", value=f"{probability * 100:.1f}%")
        
        # Show the features the AI looked at
        with st.expander("View Extracted URL Features"):
            st.json(features)
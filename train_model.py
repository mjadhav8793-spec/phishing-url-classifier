import pandas as pd
import re
from urllib.parse import urlparse
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

# 1. Create a dummy dataset (Replace this with a real dataset from Kaggle later)
data = {
    'url': [
        'https://www.google.com', 'http://secure-login-update-account.com', 
        'https://github.com', 'http://free-minecraft-coins-now.net',
        'https://en.wikipedia.org', 'http://192.168.1.1/login.php',
        'https://www.youtube.com', 'http://netflix-billing-update-urgent.info',
        'https://www.apple.com', 'http://win-f1-tickets-monza-free.xyz'
    ],
    'label': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1] # 0 = Safe, 1 = Phishing
}
df = pd.DataFrame(data)

# 2. Feature Extraction Function
def extract_features(url):
    features = {}
    
    # Lexical Features
    features['url_length'] = len(url)
    features['num_dots'] = url.count('.')
    features['num_hyphens'] = url.count('-')
    features['num_digits'] = sum(c.isdigit() for c in url)
    
    # Network Features
    parsed_url = urlparse(url)
    features['has_https'] = 1 if parsed_url.scheme == 'https' else 0
    features['has_ip'] = 1 if re.match(r'\d+\.\d+\.\d+\.\d+', parsed_url.netloc) else 0
    
    # NLP / Keyword Features
    suspicious_words = ['login', 'update', 'free', 'urgent', 'secure', 'billing']
    for word in suspicious_words:
        features[f'has_{word}'] = 1 if word in url.lower() else 0
        
    return features

# 3. Apply feature extraction to our dataset
print("Extracting features...")
features_df = df['url'].apply(lambda x: pd.Series(extract_features(x)))
X = features_df
y = df['label']

# 4. Train the Model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training Random Forest Model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. Evaluate the Model
predictions = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, predictions) * 100:.2f}%\n")
print(classification_report(y_test, predictions))

# 6. Save the Model
os.makedirs('models', exist_ok=True)
joblib.dump(model, 'models/phishing_rf_model.pkl')
print("Model saved to models/phishing_rf_model.pkl")
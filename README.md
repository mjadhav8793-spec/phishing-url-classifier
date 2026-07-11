# 🛡️ AI-Powered Phishing URL Classifier

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange.svg)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red.svg)

## 📌 Overview
This project bridges **Data Science, Machine Learning, and Cybersecurity**. It is a full-stack web application that utilizes a Random Forest classifier to analyze URLs in real-time and predict whether they are safe or malicious phishing attempts. 

Instead of relying on a static blocklist, this tool extracts **Lexical, Network, and Keyword features** from a URL to detect zero-day phishing links.

## ⚙️ Features
* **Real-time Feature Extraction:** Parses URLs to calculate string entropy, domain age characteristics, and suspicious keyword presence.
* **Random Forest Algorithm:** High-accuracy ensemble learning model trained on safe and malicious URLs.
* **Interactive Dashboard:** Built with Streamlit, allowing users to input URLs and instantly view a Threat Probability Score and the underlying JSON feature data.

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YourUsername/phishing-url-classifier.git](https://github.com/YourUsername/phishing-url-classifier.git)
   cd phishing-url-classifier

# 📰 Fake News Detector

This is my first **Machine Learning project** where I used **Google Colab** to build and train a model that can detect whether a news article is **Real or Fake**.  

I mainly used concepts like **linear models, regression techniques, and classification** to get this working.  
Finally, I deployed it on **Streamlit Cloud** so anyone can test it directly online 🚀  

---

## 🔗 Live Demo
👉 [Click here to try the app](https://news-detector-keeezfkvaryoqeytnkiegp.streamlit.app/)

---

## 📌 Features
- Enter any news text (headline or paragraph).  
- Model predicts **Real** ✅ or **Fake** ❌.  
- Shows **confidence percentage** (probability).  
- Clean and simple **Streamlit UI**.  

---

## ⚙️ Tech Stack
- **Google Colab** (for training the model)  
- **Python**  
- **Scikit-learn** (linear models, regression, classification)  
- **Streamlit** (for deployment & frontend)  

---

## 🚀 How I Trained the Model
1. Used **TF-IDF vectorization** to convert news text into numbers.  
2. Trained a **linear classification model** (logistic regression).  
3. Saved both the **model** and **vectorizer** as `.pkl` files in Colab.  
4. Created a `app.py` file to load them.  
5. Deployed everything using **Streamlit Cloud**.  

---

## 🖥️ How to Run Locally
Clone the repo and install requirements:
```bash
pip install -r requirements.txt
streamlit run app.py

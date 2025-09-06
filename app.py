import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("📰 Fake News Detector")
st.write("Enter a news headline or article and the app will predict if it's **True** or **False**.")

# User input
user_input = st.text_area("Paste news text here:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        # Transform input
        input_vec = vectorizer.transform([user_input])
        prediction = model.predict(input_vec)[0]

        if prediction == 1:
            st.success("✅ The news is **TRUE**")
        else:
            st.error("❌ The news is **FAKE**")

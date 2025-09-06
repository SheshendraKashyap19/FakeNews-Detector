import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("📰 Fake News Detector")
st.write("Enter news text and check if it's Fake or Real with probability score.")

user_input = st.text_area("Paste news text here:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        input_vec = vectorizer.transform([user_input])
        prediction = model.predict(input_vec)[0]
        probability = model.predict_proba(input_vec)[0]

        if prediction == 1:
            st.success(f"✅ The news is REAL with {probability[1]*100:.2f}% confidence.")
        else:
            st.error(f"❌ The news is FAKE with {probability[0]*100:.2f}% confidence.")

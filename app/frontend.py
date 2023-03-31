import streamlit as st
from flask import Flask, request
import requests


def predict(text):
    response = requests.post('http://localhost:6000/predict', json={'text': text})
    predictions = response.json()
    return predictions



st.title("Docker template")
text = st.text_input("Enter your text:")

if text:
    result = predict(text)
    st.write("Text:", result)
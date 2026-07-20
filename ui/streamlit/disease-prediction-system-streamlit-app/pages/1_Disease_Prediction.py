import streamlit as st
from api.api_client import predict
from components.sidebar import render_sidebar
from components.request_form import render_request_form
from components.response_view import render_prediction
render_sidebar()
st.title("Disease Prediction")
payload=render_request_form()
if st.button("Predict Disease",use_container_width=True):
    with st.spinner("Predicting..."):
        resp=predict(payload)
    if resp["success"]:
        render_prediction(resp["data"])
    else:
        st.error(resp["message"])

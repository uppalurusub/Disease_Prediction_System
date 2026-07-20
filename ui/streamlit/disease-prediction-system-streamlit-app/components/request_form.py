import streamlit as st
def render_request_form():
    return {
        "age":st.number_input("Age",1,120,52),
        "bp":st.number_input("Blood Pressure",60,250,145),
        "glucose":st.number_input("Glucose",40,500,180),
        "cholesterol":st.number_input("Cholesterol",50,500,240),
        "bmi":st.number_input("BMI",10.0,60.0,31.5),
        "heart_rate":st.number_input("Heart Rate",30,220,92),
        "oxygen_level":st.number_input("Oxygen Level",50,100,96),
        "symptoms":st.text_area("Symptoms"),
        "doctor_notes":st.text_area("Doctor Notes")
    }

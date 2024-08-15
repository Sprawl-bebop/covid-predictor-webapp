import streamlit as st
import pandas as pd
import pickle as pk

filename = "model.pickle"

st.image("cov19.jpg", width=350)
st.title("Covid Prediction System")

st.text('Please fill the form')

Cough_symptoms = st.radio("Cough symptoms", [True, False])
Fever = st.radio("Fever", [True, False])
Sore_throat = st.radio("Sore throat", [True, False])
Shortness_of_breath = st.radio("Shortness of breath", [True, False])
Headache = st.radio("Headache", [True, False])

Age_60_above = st.selectbox("Age_60_above", ["Yes", "No"])
Sex = st.selectbox("Gender", ["male", "female"])
Known_contact = st.selectbox("Known_contact", ["Other", "Abroad", "Contact with confirmed"])

if st.button("Submit"):

    file = open(filename,'rb')
    model = pk.load(file)

    if Age_60_above == "Yes":
        ag = 1
    else:
        ag = 0

    if Sex == "male":
        s = 1
    else:
        s = 0

    if Known_contact == 'Abroad':
        k = 0
    elif Known_contact == 'Other':
        k = 2
    else:
        k = 1

    df = pd.DataFrame({
        "Cough_symptoms":[Cough_symptoms],
        "Fever":[Fever],
        "Sore_throat":[Sore_throat],
        "Shortness_of_breath":[Shortness_of_breath],
        "Headache":[Headache],
        "Age_60_above":[ag],
        "Sex":[s],
        "Known_contact":[k]
        })
    
    df

    # st.write(df['Cough_symptoms'])
    st.write("Form Submitted")
    st.success("Submitted Successfully")
    st.write()
    
    result = model.predict(df)
    if result == 1:
        df["result"] = "positive"
    else:
        df["result"] = "negative"

    # st.write("Form Submitted")

    st.write("Output = ",df["result"])

    df
    # result = predict()
    # st.success("Submitted Successfully")
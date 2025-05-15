import streamlit as st
import pickle

st.title("Iris Flower Prediction App")
sepal_length = st.number_input("Enter Sepal Length")
sepal_width = st.number_input("Enter Sepal Width")
petal_length = st.number_input("Enter Petal Length")
petal_width = st.number_input("Enter Petal Width")
button = st.button("Predict")
if button:
    model=pickle.load(open('iris.pkl','rb'))
    result=model.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]       
    st.markdown(f"The predicted class is: {result}")

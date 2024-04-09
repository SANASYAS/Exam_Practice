import streamlit as st
import numpy as np
import pickle00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
model_pkl_file = "C:\\Users\\sanasya s\\Downloads\\trained_model.sav"
with open(model_pkl_file, 'rb') as file:
    loaded_model = pickle.load(file)
st.title("Water Potability Predictor")
st.write("This app predicts whether water is potable for human consumption or not.")
st.sidebar.header("Enter Water Attributes")
ph = st.sidebar.slider("pH", min_value=0.0, max_value=14.0, step=0.1, value=7.0)
hardness = st.sidebar.slider("Hardness", min_value=0.0, max_value=500.0, value=100.0)
solids = st.sidebar.slider("Solids", min_value=0.0, max_value=1000.0, value=200.0)
chloramines = st.sidebar.slider("Chloramines", min_value=0.0, max_value=20.0, value=10.0)
sulfate = st.sidebar.slider("Sulfate", min_value=0.0, max_value=400.0, value=100.0)
conductivity = st.sidebar.slider("Conductivity", min_value=0.0, max_value=2000.0, value=500.0)
organic_carbon = st.sidebar.slider("Organic Carbon", min_value=0.0, max_value=50.0, value=10.0)
trihalomethanes = st.sidebar.slider("Trihalomethanes", min_value=0.0, max_value=150.0, value=50.0)
turbidity = st.sidebar.slider("Turbidity", min_value=0.0, max_value=10.0, value=5.0)
if st.sidebar.button("Predict"):
    input_data = np.array([ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]).reshape(1, -1)
    prediction = loaded_model.predict(input_data)
    if prediction[0] == 0:
        st.success("The water is not potable for human consumption.")
    else:
        st.success("The water is potable for human consumption.")

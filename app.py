import streamlit as st
import joblib

def main():
    html_temp = """
    <div style="background-color:lightblue;padding:16px">
    <h2 style="color:black";text-align:center> Diabetes Prediction System</h2>
    </div>
    
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    
    model = joblib.load('diabetes_pred_finalmodel')
    
    p1 = st.slider('Enter your Pregnancies count',0,12)
    p2 = st.number_input("Enter Your Glucose")
    p3 = st.number_input("Enter Your Blood Pressure")
    p4 = st.number_input("Enter Your Skin Thickness")
    p5 = st.number_input("Enter Your Insulin")
    p6 = st.number_input("Enter Your BMI value")
    p7 = st.number_input("Enter Your Diabetes Pedigree Function(<1)")
    p8 = st.slider("Enter Your Age",1,120)
    
    if st.button('Predict'):
        pred = model.predict([[p1,p2,p3,p4,p5,p6,p7,p8]])
        if pred[0] == 0:
            #res = 'non-diabetic' 
            st.success('Your Diabetes test result is negative')
        else: 
            #res = 'diabetic'
            st.success('Your Diabetes test result is positive')
       
    
if __name__ == '__main__':
    main()
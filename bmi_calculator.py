import streamlit as st

def calculate_bmi(weight, height):
    # BMI formula: weight (kg) / (height (m))^2
    bmi = weight / ((height/100) ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    st.title('BMI Calculator')

    weight = st.number_input('Enter your weight (kg):', min_value=0.0, step=0.1)
    height = st.number_input('Enter your height (cm):', min_value=0.0, step=0.1)

    if st.button('Calculate BMI'):
        bmi = calculate_bmi(weight, height)
        st.write(f'Your BMI is: {bmi:.2f}')
        interpretation = interpret_bmi(bmi)
        st.write(f'Interpretation: {interpretation}')

if __name__ == '__main__':
    main()
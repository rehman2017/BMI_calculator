import streamlit as st

# BMI Calculate Function
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

# Streamlit Web App
def main():
    st.title("BMI King of Calculation 🏋️‍♂️")
    st.write("Enter your weight and height to calculate your BMI.")

    # User Input
    weight = st.number_input("Enter your weight (kg)", min_value=1.0, step=0.1)
    height = st.number_input("Enter your height (m)", min_value=0.5, step=0.01)

    if st.button("Calculate BMI"):
        if weight > 0 and height > 0:
            bmi = calculate_bmi(weight, height)
            st.success(f"Your BMI is: {bmi}")

            # BMI Categories
            if bmi < 18.5:
                st.info("You are underweight.")
            elif 18.5 <= bmi < 24.9:
                st.success("You have a normal weight.")
            elif 25 <= bmi < 29.9:
                st.warning("You are overweight.")
            else:
                st.error("You are obese.")
        else:
            st.error("Please enter valid values.")

    # Red Footer
    st.markdown("""
        <hr>
        <p style="text-align: center; color: red; font-size: 16px;">
            <b>Made by S. Farzana Shah</b>
        </p>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def main():
    st.set_page_config(page_title="BMI Calculator", page_icon="🏋️‍♂️", layout="centered")
    
    st.title("BMI Calculator 🏋️‍♂️")
    st.write("Calculate your Body Mass Index (BMI) by entering your details below.")
    
    # Sidebar for input
    with st.sidebar:
        st.header("User Input")
        weight = st.number_input("Weight (kg)", min_value=1.0, step=0.1, value=60.0)
        height = st.number_input("Height (m)", min_value=0.5, step=0.01, value=1.7)
        if st.button("Calculate BMI"):
            bmi = calculate_bmi(weight, height)
            st.session_state.bmi = bmi

    # Display results
    if "bmi" in st.session_state:
        st.subheader(f"Your BMI is: {st.session_state.bmi}")
        
        if st.session_state.bmi < 18.5:
            st.info("🔵 You are underweight.")
        elif 18.5 <= st.session_state.bmi < 24.9:
            st.success("✅ You have a normal weight.")
        elif 25 <= st.session_state.bmi < 29.9:
            st.warning("🟠 You are overweight.")
        else:
            st.error("🔴 You are obese.")
    
    # Footer
    st.markdown("""
        <hr>
        <p style="text-align: center; color: red; font-size: 16px;"><b>Made by Engr Sir Abdul Rehman Ansari full stack web developer</b></p>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

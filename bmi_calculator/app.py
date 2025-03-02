import streamlit as st


def calculate_bmi(weight, height):
    """Calculate BMI given weight in kg and height in meters."""
    return weight / (height**2)


def get_bmi_category(bmi):
    """Return BMI category based on the BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    # Set page title and configuration
    st.set_page_config(page_title="BMI Calculator", layout="centered")

    # Add a title
    st.title("BMI Calculator")

    # Add description
    st.write("Enter your weight and height to calculate your Body Mass Index (BMI)")

    # Create input fields
    weight = st.number_input(
        "Enter your weight (kg)", min_value=1.0, max_value=500.0, value=70.0
    )
    height = st.number_input(
        "Enter your height (m)", min_value=0.1, max_value=3.0, value=1.70
    )

    # Calculate BMI when button is pressed
    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)

        # Display results
        st.write("---")
        st.write(f"Your BMI is: **{bmi:.1f}**")
        st.write(f"Category: **{category}**")

        # Add a color-coded indicator
        if category == "Normal weight":
            st.success(f"Your BMI is within the normal range!")
        elif category == "Underweight":
            st.warning(f"Your BMI indicates you are underweight.")
        else:
            st.error(f"Your BMI indicates you are {category.lower()}.")


if __name__ == "__main__":
    main()

import streamlit as st


def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    BMI = weight_kg / (height_m * height_m)
    BMI = round(BMI, 2)

    result = {"BMI": BMI}

    if BMI < 18.5:
        recommended_weight = 18.5 * (height_m ** 2)
        weight_to_gain = round(recommended_weight - weight_kg, 2)
        result["category"] = "Lean"
        result["advice"] = f"Gain at least {weight_to_gain} kg to reach normal BMI."
    elif 18.5 <= BMI < 25:
        result["category"] = "Normal"
        result["advice"] = "Keep it up!"
    elif 25 <= BMI < 30:
        recommended_weight = 24.9 * (height_m ** 2)
        weight_to_lose = round(weight_kg - recommended_weight, 2)
        result["category"] = "Overweight"
        result["advice"] = f"Consider losing at least {weight_to_lose} kg."
    else:
        result["category"] = "Obesity"
        result["advice"] = "It's recommended to reduce your weight for health reasons."

    return result


st.title("🧍 BMI Calculator")

st.write("Enter your height and weight to calculate your Body Mass Index (BMI):")

height_cm = st.number_input("Height (cm)", min_value=50.0, max_value=300.0, value=170.0)
weight_kg = st.number_input("Weight (kg)", min_value=10.0, max_value=500.0, value=60.0)

if st.button("Calculate BMI"):
    if height_cm > 0 and weight_kg > 0:
        result = calculate_bmi(height_cm, weight_kg)
        st.success(f"Your BMI: {result['BMI']}")
        st.info(f"Category: {result['category']}")
        st.write(f"Advice: {result['advice']}")
    else:
        st.error("Please enter valid positive values for height and weight.")

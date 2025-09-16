from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class BMIRequest(BaseModel):
    height_cm: float
    weight_kg: float


@app.post("/calculate_bmi")
def calculate_bmi(data: BMIRequest):
    height_m = data.height_cm / 100
    weight = data.weight_kg
    BMI = weight / (height_m * height_m)

    result = {"BMI": round(BMI, 2)}

    if BMI < 18.5:
        recommended_weight = 18.5 * (height_m ** 2)
        weight_to_gain = recommended_weight - weight
        result["category"] = "Lean"
        result["advice"] = f"Gain at least {round(weight_to_gain, 2)} kg to reach normal BMI."
    elif 18.5 <= BMI < 25:
        result["category"] = "Normal"
        result["advice"] = "Keep it up!"
    elif 25 <= BMI < 30:
        recommended_weight = 24.9 * (height_m ** 2)
        weight_to_lose = weight - recommended_weight
        result["category"] = "Overweight"
        result["advice"] = f"Consider losing at least {round(weight_to_lose, 2)} kg."
    else:
        result["category"] = "Obesity"
        result["advice"] = "It's recommended to reduce your weight for health reasons."

    return result

def calculate_bmi(weight, height_feet, height_inches):
    """
    Calculate the Body Mass Index (BMI) using the weight (in kg) and height (in feet and inches).
    Formula: BMI = (weight / ((height_feet * 12 + height_inches) * 0.0254) ** 2)
    """
    height_meters = (height_feet * 12 + height_inches) * 0.0254
    return weight / (height_meters ** 2)

def interpret_bmi(bmi):
    """
    Interpret the BMI value and return a corresponding interpretation.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("BMI Calculator")
    print("-------------")
    weight = float(input("Enter your weight in kg: "))
    height_feet = int(input("Enter your height in feet: "))
    height_inches = int(input("Enter the remaining inches: "))

    bmi = calculate_bmi(weight, height_feet, height_inches)
    interpretation = interpret_bmi(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"Interpretation: {interpretation}")

if __name__ == "__main__":
    main()

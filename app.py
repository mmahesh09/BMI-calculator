from flask import Flask, request, jsonify
import matplotlib.pyplot as plt
import io
import base64
import numpy as np

app = Flask(__name__)

class BMI_Calculator:
    def __init__(self):
        self.users = {}

    def calculate_bmi(self, weight, height_cm):
        return weight / ((height_cm / 100) ** 2)

    def interpret_bmi(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def track_progress(self, user_id, weight, height_feet, height_inches):
        height_cm = height_feet * 30.48 + height_inches * 2.54
        bmi = self.calculate_bmi(weight, height_cm)
        bmi_category = self.interpret_bmi(bmi)

        if user_id not in self.users:
            self.users[user_id] = {"weights": [], "bmi_values": [], "bmi_categories": []}

        self.users[user_id]["weights"].append(weight)
        self.users[user_id]["bmi_values"].append(bmi)
        self.users[user_id]["bmi_categories"].append(bmi_category)

        return bmi, bmi_category

    def get_physical_advice(self, bmi_category):
        advice = {
            "Underweight": "Focus on consuming calorie-dense foods and strength training exercises to build muscle mass.",
            "Normal weight": "Maintain a balanced diet and incorporate a mix of cardiovascular and strength training exercises.",
            "Overweight": "Reduce calorie intake and focus on aerobic exercises to burn excess fat.",
            "Obese": "Consult with a healthcare professional for personalized weight loss advice."
        }
        return advice.get(bmi_category, "Consult with a healthcare professional for personalized advice.")

bmi_calculator = BMI_Calculator()

@app.route('/calculate_bmi', methods=['POST'])
def calculate_bmi():
    data = request.json
    weight = data['weight']
    height_feet = data['heightFeet']
    height_inches = data['heightInches']
    username = data['username']
    password = data['password']
    
    bmi, bmi_category = bmi_calculator.track_progress(username, weight, height_feet, height_inches)
    advice = bmi_calculator.get_physical_advice(bmi_category)
    
    # Prepare chart data
    chart_data = {
        'labels': list(range(len(bmi_calculator.users.get(username, {}).get("weights", [])))),
        'data': bmi_calculator.users.get(username, {}).get("bmi_values", [])
    }
    
    return jsonify({
        'bmi': bmi,
        'bmiCategory': bmi_category,
        'advice': advice,
        'chartData': chart_data
    })

if __name__ == '__main__':
    app.run(debug=True)

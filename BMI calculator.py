import matplotlib.pyplot as plt

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

    def authenticate_user(self, username, password):
        # Implement real authentication logic here
        return True

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

    def plot_progress(self, user_id):
        if user_id in self.users:
            weights = self.users[user_id]["weights"]
            bmi_values = self.users[user_id]["bmi_values"]
            bmi_categories = self.users[user_id]["bmi_categories"]

            plt.plot(weights, bmi_values, marker='o', linestyle='-')
            plt.title('BMI Progress Over Time')
            plt.xlabel('Weight (kg)')
            plt.ylabel('BMI')
            plt.grid(True)

            # Highlight BMI categories
            for i, category in enumerate(bmi_categories):
                plt.text(weights[i], bmi_values[i], f'{category}', fontsize=8, ha='right', va='bottom')

            plt.show()
        else:
            print("User ID not found.")

    def get_physical_advice(self, bmi_category):
        advice = {
            "Underweight": "Focus on consuming calorie-dense foods and strength training exercises to build muscle mass. Include healthy fats, proteins, and carbohydrates in your diet.",
            "Normal weight": "Maintain a balanced diet rich in fruits, vegetables, lean proteins, and whole grains. Incorporate a mix of cardiovascular and strength training exercises for overall fitness.",
            "Overweight": "Reduce calorie intake and focus on aerobic exercises like walking, running, or cycling to burn excess fat. Gradually increase exercise intensity and duration over time.",
            "Obese": "Consult with a healthcare professional for personalized weight loss advice. Focus on a combination of diet control and regular exercise to achieve a healthy weight. Consider joining a support group or seeking counseling for emotional support."
        }
        return advice.get(bmi_category, "Consult with a healthcare professional for personalized advice.")

def main():
    print("BMI Calculator")
    print("-------------")
    weight = float(input("Enter your weight in kg: "))
    height_feet = int(input("Enter your height in feet: "))
    height_inches = int(input("Enter the remaining inches: "))

    height_cm = height_feet * 30.48 + height_inches * 2.54
    bmi_calc = BMI_Calculator()
    bmi = bmi_calc.calculate_bmi(weight, height_cm)
    interpretation = bmi_calc.interpret_bmi(bmi)
    
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Interpretation: {interpretation}")

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if bmi_calc.authenticate_user(username, password):
        user_id = username  # For simplicity, use username as user_id
        weight = float(input("Enter your weight in kilograms: "))
        height_feet = float(input("Enter your height in feet: "))
        height_inches = float(input("Enter your height in inches: "))

        bmi, bmi_category = bmi_calc.track_progress(user_id, weight, height_feet, height_inches)
        print(f"Your BMI is: {bmi:.2f}")
        print(f"You are categorized as: {bmi_category}")

        bmi_calc.plot_progress(user_id)

        physical_advice = bmi_calc.get_physical_advice(bmi_category)
        print("Physical advice:", physical_advice)
    else:
        print("Authentication failed. Please check your username and password.")

if __name__ == "__main__":
    main()

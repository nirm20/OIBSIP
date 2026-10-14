"""
BMI Calculator (Beginner Tier)
OIBSIP - Python Programming Internship, Task 2

Calculates Body Mass Index: BMI = weight (kg) / height (m)^2
and classifies the result into a health category.
"""


def get_positive_number(prompt):
    """Keep asking until the user enters a valid positive number."""
    while True:
        value = input(prompt).strip()
        try:
            number = float(value)
        except ValueError:
            print("Error: please enter a numeric value (e.g. 65 or 1.72).")
            continue
        if number <= 0:
            print("Error: value must be greater than zero.")
            continue
        return number


def calculate_bmi(weight, height):
    """Return BMI using the formula weight / (height ** 2)."""
    return weight / (height ** 2)


def classify_bmi(bmi):
    """Return the BMI category."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("=" * 36)
    print("          BMI CALCULATOR")
    print("=" * 36)

    while True:
        weight = get_positive_number("\nEnter your weight in kg: ")
        height = get_positive_number("Enter your height in metres (e.g. 1.72): ")

        if height > 3:
            print("Error: height looks too large. Please enter it in metres, not cm.")
            continue

        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        print("\n----------- RESULT -----------")
        print(f"Your BMI      : {bmi:.2f}")
        print(f"Category      : {category}")
        print("------------------------------")

        again = input("\nCalculate again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("Thank you for using the BMI Calculator. Stay healthy!")
            break


if __name__ == "__main__":
    main()

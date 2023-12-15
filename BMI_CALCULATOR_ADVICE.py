def calculate_bmi(weight, height):
    return weight / (height * height)

def classify_bmi_and_advice(weight, height):
    bmi = calculate_bmi(weight, height)

    if bmi < 18.5:
        print("Your BMI is {:.2f}, classified as 'Underweight'.".format(bmi))
        print("Diet:")
        print("- Caloric Surplus: Consume more calories than you burn to gain weight.")
        print("- Nutrient-Dense Foods: Focus on high-calorie foods like nuts, seeds, avocados, lean meats.")
        print("\nExercise:")
        print("- Strength Training: Focus on muscle-building exercises like squats, push-ups.")
        print("- Compound Exercises: Perform movements targeting multiple muscle groups.")
        print("- Here are some exercise links for underweight individuals:")
        print("   - Exercise 1: [15 min exercise for boys ](https://www.youtube.com/watch?v=HKPrBRvLPBo)")
        print("   - Exercise 2: [15 min exercise for girl](https://www.youtube.com/watch?v=IZuXLEdYcXU)")
        print("- For more exercises, check out these YouTube videos:")
        print("   - [diet you should take properly for women](https://www.youtube.com/watch?v=1Q6ij1qSrrw)")
        print("   - [diet you should take properly for men](https://www.youtube.com/watch?v=6cPvi21GhU8)")

    elif 18.5 <= bmi < 25:
        print("Your BMI is {:.2f}, classified as 'Normal'.".format(bmi))
        # You can add specific advice for normal BMI here if needed

    else:
        print("Your BMI is {:.2f}, classified as 'Overweight/Obese'.".format(bmi))
        print("Diet:")
        print("- Caloric Deficit: Consume fewer calories than you burn to lose weight gradually.")
        print("- Balanced Diet: Prioritize whole, unprocessed foods like fruits, vegetables.")
        print("\nExercise:")
        print("- Cardiovascular Exercise: Engage in activities like brisk walking, cycling.")
        print("- Strength Training: Incorporate exercises to build muscle.")
        print("- Here are some exercise links for overweight/obese individuals:")
        print("   - Exercise 1: [15 minutes workout with BullyJuice](https://www.youtube.com/watch?v=xngUfoWLkFw)")
        print("   - Exercise 2: [15 min strength training by juice and toya](https://www.youtube.com/watch?v=xqVBoyKXbsA)")
        print("- For effective diet, watch these YouTube videos:")
        print("   - [ diet for boys](https://www.youtube.com/watch?v=CxktmQ3zJOA)")
        print("   - [diet for gir](https://www.youtube.com/watch?v=I4DbxaN033k)")

    print("\nGeneral Tips:")
    print("- Consult Professionals: Seek advice from a healthcare provider or trainer.")
    print("- Consistency is Key: Be consistent in both diet and exercise.")

def main():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    classify_bmi_and_advice(weight, height)

if __name__ == "__main__":
    main()



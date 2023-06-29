height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))


BMI = weight / (height/100)**2
print(f"You BMI is {BMI}")

if BMI < 18:
    print("underweight")
elif BMI >= 18.5 and BMI < 29:
    print("normal weight")
elif BMI >= 29.1 and BMI < 34 :
    print("overweight")
elif BMI >= 34:
    print("obese")

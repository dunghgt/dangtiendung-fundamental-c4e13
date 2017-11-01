h = int(input("height(cm): "))
w = int(input("weight(kg): "))

h = h / 100

BMI = w / (h * h)

print("BMI = ", BMI)
if BMI < 16:
    print("Severely underweight")
elif BMI < 18.5:
    print("Underweight")
elif BMI < 25:
    print("Normal")
elif BMI < 30:
    print("Overweight")
else:
    print("Obese")

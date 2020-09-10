#bmi calculator

#bmi function
def bmi_calculator(height, weight):
    bmi = round(weight / ((height / 100) ** 2), 2)
    if bmi < 18.5:
        status = "underweight"
    elif 18.5 <= bmi < 24:
        status = "normal"
    elif 24 <= bmi < 27:
        status = "overweight"
    else:
        status = "obesity"
    return [bmi, status]

#main
name = input("input your name: ")
bmi, status = bmi_calculator(int(input("input your height in cm: ")), int(input("input your weight in kg: ")))
print("Hi {}! Your bmi is {} and it is {}.".format(name, bmi, status))

#CalorieCount Example

#''' Calories = ((Age x 0.2757) + (Weight x 0.03295) + (Heart Rate x 1.0781) — 75.4991) x Time / 8.368 ''' formula

age = int(input("Enter your age: "))
weight = int(input("Enter your weight: "))
hr = int(input("Enter your current heart rate: "))
time = int(input("Enter the amount of time spent: "))


calories = (( age * 0.2757) + (weight * 0.03295) + (hr * 1.0781) - 75.4991) * time / 8.368

#Because we use decimals in the equation, we can output the true float value
print(f'Calories: {calories:.2f} calories')
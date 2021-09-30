# Programmers: Callie Walker and Lesdy Galvez
# Course: CS151, Dr. Rajeev
# Date: 9/30/21
# Lab Number: 3
# Program Inputs: The weight of the package and the distance
# Program Outputs: The charges for the package

weight = int(input("Enter the weight of the package "))
distance = int(input("Enter the distance the package must travel "))
weight_rate = (distance / 500)
charge = 1


if distance <= 10 or distance > 3000:
    print("package cannot be shipped")
elif (weight > 0 and weight < 2):
    charge = weight_rate * 1.10
    print("For ", distance, " miles, it will cost ", charge, "for the package to ship")
elif (weight >= 2 and weight < 6):
    charge = weight_rate * 2.20
    print("For ", distance, " miles, it will cost ", charge, "for the package to ship")
elif (weight >= 6 and weight < 10):
    charge = weight_rate * 3.70
    print("For ", distance, " miles, it will cost ", charge, "for the package to ship")
elif (weight >= 10 and weight < 20):
    charge = weight_rate * 4.80
    print("For ", distance, " miles, it will cost $", charge, "for the package to ship")
else:
    print("Package cannot be shipped")



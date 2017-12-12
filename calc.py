'''
Created on Dec 10, 2017

@author: b00st3d
'''
print("Welcome to the Elite Dangerous Gravity Calculation Toolkit")
print()
MR = float(input("Please enter the (Earth) Mass Ratio: "))
PR = float(input("Please enter the Planet Radius in km: "))
PR = PR/1000
G = 6.67 * pow(10, -11)
EM = 5.98 * pow(10, 24)
PR = PR * pow(10, 6)
#print()
#print("Gravity =",G)
#print("Earth Mass =", EM)
#print("(Earth) Mass Ratio =", MR)
#print("Planet Radius =", PR)
output = float((G * (EM * MR)) / PR ** 2)
gravity = output/9.807
gravity = round(gravity, 2)
print()
print("The gravity on this planet:",gravity)
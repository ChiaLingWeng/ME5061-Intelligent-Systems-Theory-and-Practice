from fuzzy_system import FuzzyVariableInput, FuzzyVariableOutput, FuzzySystem
from fuzzy_system import FuzzySet
import matplotlib.pyplot as plt
import numpy as np
# Define the fuzzy set with trapezoidal membership function

'''
s = FuzzySet.create_trapezoidal(name='S', domain_min=1, domain_max=100, res=100, a=20, b=30, c=50, d=80)

fig, axs = plt.subplots(1, 1)
s.plot_set(axs)
plt.show()
t = FuzzySet.create_triangular('T', 1, 100, 100, 30, 50, 100)

fig, axs = plt.subplots(1, 1)
t.plot_set(axs)
plt.show()
fig, axs = plt.subplots(1, 1)
s.union(t).complement().intersection(s).min_scalar(0.2).plot_set(axs)
plt.show()
'''

temp = FuzzyVariableInput('Temperature', 10, 40, 100)
temp.add_triangular('Cold', 10, 10, 25)
temp.add_triangular('Medium', 15, 25, 35)
temp.add_triangular('Hot', 25, 40, 40)

humidity = FuzzyVariableInput('Humidity', 20,100,100)
humidity.add_triangular('Wet',20,20,60)
humidity.add_trapezoidal('Normal', 30,50,70,90)
humidity.add_triangular('Dry',60,100,100)


motor_speed = FuzzyVariableOutput('Speed', 0,100,100)
motor_speed.add_triangular('Slow',0,0,50)
motor_speed.add_triangular('Moderate',10,50,90)
motor_speed.add_triangular('Fast', 50,100,100)


system = FuzzySystem()
system.add_input_variable(temp)
system.add_input_variable(humidity)
system.add_output_variable(motor_speed)

system.add_rule(antecedent_clauses={'Temperature':'Cold','Humidity':'Wet'},
                consequent_clauses={'Speed':'Slow'})
# TODO: Write the remaining rules and add to the system
# Write your code below
system.add_rule(antecedent_clauses={'Temperature':'Medium','Humidity':'Dry'},
                consequent_clauses={'Speed':'Slow'})
system.add_rule(antecedent_clauses={'Temperature':'Cold','Humidity':'Normal'},
                consequent_clauses={'Speed':'Slow'})

system.add_rule(antecedent_clauses={'Temperature':'Hot','Humidity':'Dry'},
                consequent_clauses={'Speed':'Moderate'})
system.add_rule(antecedent_clauses={'Temperature':'Medium','Humidity':'Normal'},
                consequent_clauses={'Speed':'Moderate'})
system.add_rule(antecedent_clauses={'Temperature':'Cold','Humidity':'Wet'},
                consequent_clauses={'Speed':'Moderate'})

system.add_rule(antecedent_clauses={'Temperature':'Hot','Humidity':'Normal'},
                consequent_clauses={'Speed':'Fast'})
system.add_rule(antecedent_clauses={'Temperature':'Hot','Humidity':'Wet'},
                consequent_clauses={'Speed':'Fast'})
system.add_rule(antecedent_clauses={'Temperature':'Medium','Humidity':'Wet'},
                consequent_clauses={'Speed':'Fast'})

output = system.evaluate_output(input_values={"Temperature":18, "Humidity":60})
output
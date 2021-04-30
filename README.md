# Master-s-Project-Code
This contains the code, for the master's project "Modelling the Cardiovascular System to Improve the Effectiveness of Mechanical Ventilators" by Philip W. Bond.

DefEqnV200: this file defines the equation of the differential equations used in the Runge-Kutta method

DefUpdateV200: this file defines the fourth order Runge-Kutta update method for the simulation

SimulationV400_Process: this file impliments the fourth order Runge-Kutta update method defined in DefUpdateV200. As well as this, it defines some code which allows the variable 
kappa2 be changed after a certain number of iterations

SimulationV200: this file allows the whole simulation to be run, it is where the parameters are defined as well as the time-step, number of iterations, and number of values that
kappa2 will take.

SimulationV200_Analysis: this file plots the data from the .npy files that are created when the simulation runs.

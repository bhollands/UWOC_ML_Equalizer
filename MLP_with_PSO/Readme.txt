Author - Bernard Hollands

MLP_with_PSO was oringally written for F20BC at Heriot-Watt and adapted for final year project

This is a Feed forward Multi-Layer Perceptron Neural Network optimised with a  
Particel Swarm Optimiser for solving mathematical functions with the option of changing the activation function.

In current configuration data can be seen in the 'Data' folder. The current configuration is setup to run on the first 20000 PAM UWOC data points. This can be set upto 1004040 in the 'configure()' function. This however may take a long time to run.

once run this results are recored in 'NN_output_data' folder in the form .xlsx (excel files) fitness is also printed to terminal

---Requirments---
Python3 (3.8.6) - Older versions may work
Numpy (1.18.5)
Pandas (1.1.3)
openpyxl (3.0.5)
scipy (1.5.2)

---To run projcect--- 
Please run main.py.
You can adjust parameters all parameters from the 'singleRun()' function 

---Choise of Data---
Sine wave - "sine"
Linear Function - "linear"
Hyperbolic Tangent - "tanh"
Complex Function - "complex"
XOR Funcion - "xor"
UWOC Data - "uwoc" : Dissertation Specific


---choice of activation functions---
Cosine - "cosine"
Hyperbolic Tangent - "hypertangent"
Gaussian function - "gaussian"
Sigmoid Function - "sigmoid"


You can select either any of the excel files in the <Data> directory 
or equ to run on the 600Mpbs dataset.

---Results---
Results are stored in the 'NN_ouput data' folder
singlerun() - This simply trains the network for the specified settings. The network output and fitness are recorded.
In the singleRun files the columns are as follows 

for "_results_<file>_<activation function>"
0 - Neural Network output for that run
1 - What the network is trying to achive


For "_fitness_results_<file>_<activation function>"
 0 - fitness per epoch


Author - Bernard Hollands

Written for final year project at Heriot-Watt

This is a Feed forward Multi-Layer Perceptron neural network optimised with Gradient descent using the keras API

---Requirments---
Python3 (3.8.6) - Older versions may work
keras (2.4.3)
tensorflow (2.3.1)
Numpy (1.18.5)
Pandas (1.1.3)
openpyxl (3.0.5)
scipy (1.5.2)

---To run--- 
Please run 'mlp_train_test.py' - This uses the 600Mbps sinlge column dataset for training and testing
To use trained model on the larger 600Mbps dataset run 'mlp_load_model.py' 

---Results---
MSE Loss and Accuracy will print out to terminal

Once run this results are recored in 'Results' folder in the form .xlsx (excel files) that can be graphed
Each column is labled as 0,1,2 they are as follows
0 - Network output
1 - What was input to the NN
2 - A perfect Output

Best Achived loss - 0.68 

So far, have been unable to beat this platue disite many sizes of network, amaount of training data, number of epochs etc...

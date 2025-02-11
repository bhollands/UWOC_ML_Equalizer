from data_reader import *
from network import *
import pandas as pd
import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler


'''
saves the results of a run
'''
def saveResults(predict, actual, activeFunc, file, fitness):
    newArr = np.column_stack((predict,actual))
    predict = pd.DataFrame(newArr)
    fitness = pd.DataFrame(fitness)

    output_filepath = 'MLP_with_PSO/NN_output data/_results_'+file +'_'+activeFunc+'.xlsx'
    fitness_filepath = 'MLP_with_PSO/NN_output data/_fitness_results_'+file +'_'+activeFunc+'.xlsx'
    predict.to_excel(output_filepath, index = False)
    fitness.to_excel(fitness_filepath, index = False)
    
    plt.plot(predict,'r-o',markersize=4, label = "output")#linestyle = '-')
    plt.plot(actual,'b-o',markersize=4, label = "ideal")#linestyle = '-')
    #plt.plot(np_in, 'r-o',markersize=4, label = "input", linestyle = '--', linewidth = '1')
    plt.xlabel('Number of Bits')
    plt.ylabel('Bit State')
    plt.grid(True)
    plt.xlim(0,50)
    plt.legend(loc='upper right')
    plt.show()





'''
configures some aspects of the network
'''
def configure(file_select):
    scaler = MinMaxScaler(feature_range=(0,1))
    if file_select == "uwoc":
        myData = loadmat('POF60m_PAMExp_2PAM_DR600Mbps(single column).mat')   
        Rx = myData['PAMsymRx']
        Tx = myData['PAMsymTx']
        X = Rx[0:2000]#1004040] #set to 1004040 for full dataset
        y = Tx[0:2000]#1004040]
        X = scaler.fit_transform(X)
        y = scaler.fit_transform(y)
        #X = X/y
        single_input = True
    else: 
        data = data_reader() #Create new data reader
        single_input = data.select(file_select) #select the file and it returns if it is single input
        X = data.input_array() #input input array
        
        print(X)
        y = data.expected_output_array() #get function output
        

    if single_input: #if network is single input one input we only need single input neuron
        input_layer = 1
    else: #else it is 2 
        input_layer = 2
    return(X,y,input_layer) #return relavent data


'''
runs a single specificed configuration
'''
def singleRun(file, activationFunc, hiddenLayersSize, numOfHidden, save, epochs,numParticels,posRange, velRange, coef, iWeightRange):
    config = configure(file) #configure the network

    nn = FeedForwardNeuralNetwork(inLayerSize=config[2] ,outLayerSize=1,hiddenLayersSize=hiddenLayersSize,
                                    numOfHiddenLayers=numOfHidden, activationFunc=activationFunc, fileSelect = file) # creat the network
    nn.initNetwork() #initalise the network
    result = nn.train(X = config[0], y = config[1],numParticels=numParticels, posRange=posRange, 
                    velRange=velRange, iWeightRange=iWeightRange,
                    c=coef, epochs= epochs, print_step=epochs/10) #train on x and y for given number of iterations

    if save == True:
        saveResults(result[0], config[1], activationFunc, file, result[1]) #save the results of the run
        #saveFitness(result[1], file)

def main():
    singleRun(file="uwoc", activationFunc="cosine", hiddenLayersSize = 40, 
                numOfHidden = 2, save=True, epochs=50, numParticels=200,  
                posRange=(-2.0,2.0), velRange=(-2.0, 2.0), 
                coef = (0.5,0.3), iWeightRange = (0.9, 0.9))



if __name__ == "__main__":
    main()
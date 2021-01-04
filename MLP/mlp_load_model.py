import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split #to make a % of the dataset for quicker testing
import tensorflow as tf
from scipy.io import loadmat
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop
from sklearn.preprocessing import MinMaxScaler

in_file = os.path.dirname(os.path.abspath(__file__)) #fix later

checkpoint_path = "MLP\model_checkpoints\cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

myData = loadmat('POF60m_PAMExp_2PAM_DR600Mbps.mat')   

Rx = myData['PAMsymRxMat'].reshape((-1,1))
Tx = myData['PAMsymTxMat'].reshape((-1,1))

PAMsymRx_Array = Rx[0:150]#60300] #set to 15060300 for full dataset
PAMsymTx_Array = Tx[0:150]#60300]
scalar = MinMaxScaler(feature_range=(0,1))

datasetRx = scalar.fit_transform(PAMsymRx_Array)
datasetTx = scalar.fit_transform(PAMsymTx_Array)

def saveResults(predicted, input_values, perfect):
    newArr = np.column_stack((predicted,input_values, perfect))
    predict = pd.DataFrame(newArr)

    output_filepath = 'MLP\Results\_results_keras_trained_model.xlsx'
    predict.to_excel(output_filepath, index = False)

def create_model():
    model = Sequential()
    model.add(Dense(1, activation='tanh'))
    model.add(Dense(16, activation='tanh'))
    model.add(Dense(16, activation='tanh'))
    model.add(Dense(16, activation='tanh'))
    
    model.add(Dense(1, activation='tanh'))
    model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])
    return model


model = create_model()
model.load_weights(checkpoint_path)
loss, acc = model.evaluate(datasetRx,datasetTx)
print("Trained model:", loss)
y_pred = model.predict(PAMsymRx_Array, batch_size=128, verbose=0)
saveResults(y_pred,datasetRx, datasetTx)

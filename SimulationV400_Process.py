import numpy as np
import copy as cp
import math as ma
from DefUpdateV200 import update as up
import pandas as pd
import scipy.io

class Process:
    '''Defining the parameters of the simulatoin.'''
    def __init__(self,step,itersperkappa2,Situation,valuenum,valueincrease,kappa2init):
        '''This is the step size, in seconds'''
        self.step = step
        '''This is the amount of iterations that will be completed in the simulation - per value of kappa2'''
        self.itersperkappa2 = itersperkappa2
        '''This is where the system will be entered'''
        self.Situation = Situation
        '''The number of values kappa will take throughout the simulation'''
        self.valuenum = valuenum
        '''The amount that kappa2 should be increased by'''
        self.valueincrease = valueincrease
        '''Setting the initial value of kappa2'''
        self.kappa2init = kappa2init

    def movementvarkappa (self):
        '''This is an empty list where the data for the xc data at every iteration will be added'''
        x1Elapse = []
        '''This is an empty list where the data for the xr data at every iteration will be added'''
        x2Elapse = []
        '''This is an empty list where the time point at every iteration will be added'''

        x3Elapse = []

        y1Elapse = []

        y2Elapse = []

        y3Elapse = []

        TimeElapse = []

        '''This ensure that the update function is performed the amount of times specified when defining it.'''
        for j in range(self.valuenum):

            lb = j * ( self.itersperkappa2 )    
            ub = ( ( j + 1) * ( self.itersperkappa2 ) ) - 1
        
            for i in range( lb , ub , 1 ):

                self.Situation.kappa2 = self.kappa2init + ( j * self.valueincrease )

                '''This applies the Runge-Kutta method to the the defined system'''
                self.Situation.RunKut(self.step)
                '''this makes of copy of the xc componenet at a given iteration'''
                datax1 = cp.deepcopy(self.Situation.x1)
                '''this makes of copy of the xr componenet at a given iteration'''
                datax2 = cp.deepcopy(self.Situation.x2)
                datax3 = cp.deepcopy(self.Situation.x3)
                datay1 = cp.deepcopy(self.Situation.y1)
                datay2 = cp.deepcopy(self.Situation.y2)
                datay3 = cp.deepcopy(self.Situation.y3)

                '''This is the time in seconds at a particular iteration'''
                dataTime = i*self.step
                '''This adds the xc data for a particular time to it's respective list'''
                x1Elapse.append(datax1)      
                '''This adds the xr data for a particular time to it's respective list'''         
                x2Elapse.append(datax2)

                x3Elapse.append(datax3)

                y1Elapse.append(datay1)

                y2Elapse.append(datay2)

                y3Elapse.append(datay3)
                '''This adds the time in seconds of a given iteration to the liste containing time data'''
                TimeElapse.append(dataTime)

            '''This saves the xrElapse list as a .npy file so it can be called upon in the analysis'''
            np.save("x1Data",x1Elapse)
            '''This saves the xcElapse list as a .npy file so it can be called upon in the analysis'''
            np.save("x2Data",x2Elapse)

            np.save("x3Data",x3Elapse)

            np.save("y1Data",y1Elapse)

            np.save("y2Data",y2Elapse)

            np.save("y3Data",y3Elapse)
            '''This saves the time progression list as a .npy file so it can be called upon for analysis'''
            np.save("timeData",TimeElapse)



            '''This saves the respective list as a data frame using the pandas function, this then converts them into a cvs file, this then saves them in the file described by the file path'''
            '''If anyone else is having to use this to put collected data into MODA, you will have to change the file directory so that it saves in a file on your computer.'''
            '''The none part of the header and index is so that the .cvs file is just the information, and no index, this is so it can be inputted into MODA, as it produces a column form'''
            pd.DataFrame(x1Elapse).to_csv(r'C:\Users\Admin\Documents\SimulationData\x1dataframe.csv', header = None, index = None)
            pd.DataFrame(x2Elapse).to_csv(r'C:\Users\Admin\Documents\SimulationData\x2dataframe.csv', header = None, index = None)
            pd.DataFrame(x3Elapse).to_csv(r'C:\Users\Admin\Documents\SimulationData\x3dataframe.csv', header = None, index = None)
            pd.DataFrame(y1Elapse).to_csv(r'C:\Users\Admin\Documents\SimulationData\y1dataframe.csv', header = None, index = None)
            pd.DataFrame(y2Elapse).to_csv(r'C:\Users\Admin\Documents\SimulationData\y2dataframe.csv', header = None, index = None)
            pd.DataFrame(y3Elapse).to_csv(r'C:\Users\Admin\Documents\SimulationData\y3dataframe.csv', header = None, index = None)
            pd.DataFrame(TimeElapse).to_csv(r'C:\Users\Admin\Documents\SimulationData\timedataframe.csv', header = None, index = None)
            pd.DataFrame(x1Elapse).to_csv(r'C:\Users\Admin\Google Drive\Degree\Masters Project\Simulations\x1dataframe.csv', header = None, index = None)
            pd.DataFrame(x2Elapse).to_csv(r'C:\Users\Admin\Google Drive\Degree\Masters Project\Simulations\x2dataframe.csv', header = None, index = None)
            pd.DataFrame(TimeElapse).to_csv(r'C:\Users\Admin\Google Drive\Degree\Masters Project\Simulations\timedataframe.csv', header = None, index = None)
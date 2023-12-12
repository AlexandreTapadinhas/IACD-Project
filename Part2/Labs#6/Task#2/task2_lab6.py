'''
import pandas as pd
import numpy as np

data = pd.read_csv('1800.csv')

column_names = ['Station', 'Date', 'Type' , 'Temperature' , 'Uncertainty' , 'Observations' , 'Time' , 'Random']
data.columns = column_names
grouped = data.groupby('Station')
min_temp = grouped['Temperature'].min()

print(min_temp)
'''

'''
Station
EZE00100082   -135
GM000010962      0
ITE00100554   -148
Name: Temperature, dtype: int64
'''

from mrjob.job import MRJob
from mrjob.step import MRStep

class MinTemperatureByCaptital(MRJob):
    def steps(self):
        return [
            MRStep(mapper = self.mapper_get_min,reducer=self.reducer_get_min)
        ]
    
    def mapper_get_min(self, _, line):
        columns = line.strip().split(',')

        weather_station = columns[0]
        temperature = columns[3]

        yield weather_station, int(temperature)

    def reducer_get_min(self, key, values):
        yield key, min(values)

if __name__ == '__main__':
    MinTemperatureByCaptital.run()    

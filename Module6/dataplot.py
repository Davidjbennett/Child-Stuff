import glob
import numpy as np
import matplotlib.pyplot as plt

def analyze(fname):
    #! read raw data
    raw_data = np.loadtxt(fname)

    #! smooth raw data
    smooth_data = smooth(raw_data)

    #! find pulses
    

    #! plot the data
    plt.plot(raw_data)
    plt.show()

    #! calculate area adn write to file

    #len(raw_data)

def smooth(data):
    '''Smoothing filter returns a smoothed copy of the input'''
    res = data.copy()

    for i in range(3, len(data)-3):
        res[n] = (data[i-3] + 2*data[i-2] + 3*data[i-1] + 3*data[i] 
                  + 3*data[i+1] + 2*data[i+2] + data[i+3])

def main():
    for fname in glob.glob('*.dat'):
        analyze(fname)

if __name__ == "__main__":
    pass
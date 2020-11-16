import glob
import numpy as np
import matplotlib.pyplot as plt

def analyze(fname):
    vT = 100

    #! read raw data
    raw_data = np.loadtxt(fname)

    #! smooth raw data
    smooth_data = smooth(raw_data)

    #! find pulses
    pulseList = []
    for i in range(0,len(smooth_data)-3):
        if (smooth_data[i+2]-smooth_data[i]) >= 100:
            pulseList.append(smooth_data[i])
        else:
            pulseList.append(0)

    #! plot the data
    # plt.plot(raw_data,label="Raw")
    # plt.plot(smooth_data,label="Smooth")
    plt.plot(pulseList,label="Pulses")
    plt.legend()
    plt.show()

    #! calculate area and write to file
    

    #len(raw_data)

def smooth(data):
    '''Smoothing filter returns a smoothed copy of the input'''
    res = data.copy()

    for i in range(3, len(res)-3):
        res[i] = ((data[i-3] + 2*data[i-2] + 3*data[i-1] + 3*data[i] 
                  + 3*data[i+1] + 2*data[i+2] + data[i+3])//15)
    return res

def main():
    # for fname in glob.glob('2*.dat'):
    #     analyze(fname)
    analyze('2_Record2308.dat')
    # raw = np.loadtxt('2_Record2308.dat')
    # plt.plot(raw)

if __name__ == "__main__":
    main()
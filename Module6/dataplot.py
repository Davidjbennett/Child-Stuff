import glob
import numpy as np
import matplotlib.pyplot as plt

VT = 100
WIDTH = 50

def analyze(fname):
    

    #! read raw data
    raw_data = np.loadtxt(fname)

    #! smooth raw data
    smooth_data = smooth(raw_data)

    #! find pulses
    pulseList = []
    pulseCount = 0
    pulseArea = 0
    pulseStart = 0
    counter = 1

    for i in range(0,len(smooth_data)-2):
        if (smooth_data[i+2]-smooth_data[i]) > VT:
            pulseList.append(i)
            

            i += 1
            while i < len(smooth_data) and smooth_data[i+1] > smooth_data[i]:
                i += 1
                pulseArea += raw_data[i]

    # print("Pulse " + pulseCount + ": " + pulseStart + " (" + pulseArea + ")")
        
                
    #! plot the data
    _,axes = plt.subplots(nrows=2)

    axes[0].plot(raw_data, color ='r')
    axes[0].set(title=fname, ylabel="Raw Data", xticks=[])
    axes[1].plot(smooth_data, color ='y')
    axes[1].set(title=fname, ylabel= "Smooth Data")
    # axes[2].plot(pulseList, color ='b')
    # axes[2].set(title=fname, ylabel= "Pulse Data")

    pdf_file = fname[0:-3] + "pdf"
    #! calculate area and write to file
    plt.savefig(pdf_file)
    plt.tight_layout()
    # plt.show()

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
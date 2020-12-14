import requests
import time
from multiprocessing import cpu_count

def download(flag):
    prefix = 'https://www.cia.gov/library/publications/resources/the-world-factbook/graphics/flags/large/'
    flagUrl = prefix + flag + "-lgflag.gif"
    response = requests.get(flagUrl).content
  
    if response:
        with open("flags/" + flag + ".gif","wb") as f:
            f.write(response)
        return len(response)
  
def main():
    with open("flags.txt") as f_file:
        flags = (line.strip() for line in f_file)
    
        numBytes = 0
        startTime = time.perf_counter()
        numBytes = sum(map(download,flags))
        endTime = time.perf_counter()
        
    
    with open("flags_a_results.txt", "w") as results:
        timeString = "Elapsed time: " + str(endTime - startTime) + "\n"
        results.write(timeString)
        bytesString = str(numBytes) + " bytes downloaded"
        results.write(bytesString)
        results.close()
    
    print("Elapsed Time:", endTime-startTime)
    print(numBytes, "bytes downloaded")
    
    
    
if __name__ == "__main__":
    main()



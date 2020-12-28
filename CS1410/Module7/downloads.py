import requests
import time
from multiprocessing import cpu_count

prefix = 'https://www.cia.gov/library/publications/resources/the-world-factbook/graphics/flags/large/'
suffix = "-lgflag.gif"

def download(flag):
    furl = prefix + flag + suffix
    resp = requests.get(prefix + flag + suffix).content
    # print(furl)

    with open("flags/" + flag + ".gif", "wb") as f:
        print(f)
        # f.write(resp)
    return(len(resp))


def main():
    with open("flags.txt", "r") as f:
        flags = (line.strip() for line in f)
        print(flags)


        # bytes = 0
        # start = time.perf_counter()
        # bytes = sum(map(download, flags))
        # stop = time.perf_counter()
    
    # print(stop-start)
    # print(bytes)

    # flagsURL = []
    
    # for i in flags:
    #     flagsURL.append(prefix + i + suffix)
    

    # for i in flags:
    #     print(i + '\n')


if __name__ == "__main__":
    main()
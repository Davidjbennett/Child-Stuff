import math
from math import e

def main():
    num_lyst = [math.pi, e, -math.pi, -e]
    num_names = ["pi", "e", "pi", "e"]
    for num in range(len(num_lyst)):
        print(f"{num_names[num]} is {num_lyst[num]}")
        print(f"Ceiling of {num_names[num]} is {math.ceil(num_lyst[num])}")
        print(f"Floor of {num_names[num]} is {math.floor(num_lyst[num])}")
        print(f"Round of {num_names[num]} is {round(num_lyst[num])}")
        print(f"Truncate of {num_names[num]} is {math.trunc(num_lyst[num])}")

if __name__ == "__main__":
    main()
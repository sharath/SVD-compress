import numpy as np
import matplotlib.pyplot as plt
import time
from PIL import Image
import sys

def compress(file):
    im = Image.open(file)




if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid Parameters")
        exit(0)
    compress(sys.argv[1])

import numpy as np
from PIL import Image
import sys
import os


def compress(file, n):
    img = Image.open(file)
    imgbw = img.convert('LA')

    #imgbw.convert('RGB').save("bw.jpg")

    # convert to matrix
    imgmat = np.array(list(imgbw.getdata(band=0)), float)
    imgmat.shape = (imgbw.size[1], imgbw.size[0])
    imgmat = np.matrix(imgmat)

    U, sigma, V = np.linalg.svd(imgmat)
    reconstimg = np.matrix(U[:, :n] * np.diag(sigma[:n]) * np.matrix(V[:n, :]))

    img = Image.fromarray(reconstimg).convert('RGB')
    if not os.path.exists("processed"):
        os.mkdir("processed")
    img.save("processed/processed%d.jpg"%n)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Invalid Parameters")
        exit(0)
    for i in range(0, int(sys.argv[2])+1):
        compress(sys.argv[1], i)



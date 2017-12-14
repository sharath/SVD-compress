import numpy as np
from PIL import Image
import sys
import os


def compress(file, n):
    img = Image.open(file)
    imgbw = img.convert('LA')

    if not os.path.exists("processed"):
        os.mkdir("processed")
    imgbw.convert('RGB').save("processed/bw.png")

    # convert to matrix
    imgmat = np.array(list(imgbw.getdata(band=0)), float)
    imgmat.shape = (imgbw.size[1], imgbw.size[0])
    imgmat = np.matrix(imgmat)

    U, sigma, V = np.linalg.svd(imgmat)
    for i in range(0, n, 10):
        reconstimg = np.matrix(U[:, :i] * np.diag(sigma[:i]) * np.matrix(V[:i :]))
        img = Image.fromarray(reconstimg).convert('RGB')
        img.save("processed/processed%d.png"%i)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Invalid Parameters")
        exit(0)
    compress(sys.argv[1], int(sys.argv[2])+1)



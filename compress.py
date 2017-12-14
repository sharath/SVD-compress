import numpy as np
from PIL import Image, ImageFont, ImageDraw
import sys
import os


def compress(file, n, s):
    img = Image.open(file)
    imgbw = img.convert('LA')

    font = ImageFont.truetype("Prototype.ttf", 30)
    yellow = 255, 255, 0
    imgbw.convert('RGB').save("processed/bw.png", compress_level=1)

    # convert to matrix
    imgmat = np.array(list(imgbw.getdata(band=0)), float)
    imgmat.shape = (imgbw.size[1], imgbw.size[0])
    imgmat = np.matrix(imgmat)

    U, sigma, V = np.linalg.svd(imgmat)

    for i in range(0, n, s):
        if i == 0:
            continue
        reconstimg = np.matrix(U[:, :i] * np.diag(sigma[:i]) * np.matrix(V[:i:]))
        img = Image.fromarray(reconstimg).convert('RGB')
        draw = ImageDraw.Draw(img)
        draw.text((10, 10), "%d" % i, yellow, font=font)

        img.save("processed/processed%d.png" % i, compress_level=1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Invalid Parameters")
        exit(0)
    if not os.path.exists("processed"):
        os.mkdir("processed")
    compress(sys.argv[1], int(sys.argv[2])+1, int(sys.argv[3]))



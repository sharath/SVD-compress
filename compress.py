import numpy as np
from PIL import Image, ImageFont, ImageDraw
import sys
import os


def compress(file, n, s):
    img = np.array(Image.open(file))
    row, col, _ = img.shape
    img = img / 255
    img_r = img[:, :, 0]
    img_g = img[:, :, 1]
    img_b = img[:, :, 2]

    print("Computing SVD for R")
    U_r, sigma_r, V_r = np.linalg.svd(img_r)
    print("Computing SVD for G")
    U_g, sigma_g, V_g = np.linalg.svd(img_g)
    print("Computing SVD for B")
    U_b, sigma_b, V_b = np.linalg.svd(img_b)

    font = ImageFont.truetype("Prototype.ttf", 30)
    yellow = 255, 255, 0

    for i in range(0, n, s):
        if i == 0:
            continue

        print("Reconstructing R for Term %d" % i)
        reconst_r = np.dot(U_r[:, :i], np.dot(np.diag(sigma_r[:i]), np.matrix(V_r[:i, :])))
        print("Reconstructing G for Term %d" % i)
        reconst_g = np.dot(U_g[:, :i], np.dot(np.diag(sigma_g[:i]), np.matrix(V_g[:i, :])))
        print("Reconstructing B for Term %d" % i)
        reconst_b = np.dot(U_b[:, :i], np.dot(np.diag(sigma_b[:i]), np.matrix(V_b[:i, :])))

        reconstimg = np.zeros((row, col, 3), dtype='uint8')
        reconstimg[:, :, 0] = reconst_r*255
        reconstimg[:, :, 1] = reconst_g*255
        reconstimg[:, :, 2] = reconst_b*255

        reconstimg[reconstimg < 0] = 0
        reconstimg[reconstimg > 255] = 255

        img = Image.fromarray(reconstimg)
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



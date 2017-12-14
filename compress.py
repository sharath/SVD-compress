import numpy as np
from PIL import Image, ImageFont, ImageDraw
import sys
import os


def compress(file, n, s):
    img = np.array(Image.open(file))
    Image.fromarray(np.uint8(img)).save("processed/unprocessed.png", compress_level=1)
    row, col, _ = img.shape
    img = img / 255

    print("Computing SVD for R")
    U_r, sigma_r, V_r = np.linalg.svd(img[:, :, 0])
    print("Computing SVD for G")
    U_g, sigma_g, V_g = np.linalg.svd(img[:, :, 1])
    print("Computing SVD for B")
    U_b, sigma_b, V_b = np.linalg.svd(img[:, :, 2])

    font = ImageFont.truetype("Prototype.ttf", 30)
    font_col = 255, 255, 0

    for i in range(0, n, s):
        if i == 0:
            continue
        print("Reconstructing R for Term %d" % i)
        reconst_r = np.dot(U_r[:, :i], np.dot(np.diag(sigma_r[:i]), V_r[:i, :]))
        print("Reconstructing G for Term %d" % i)
        reconst_g = np.dot(U_g[:, :i], np.dot(np.diag(sigma_g[:i]), V_g[:i, :]))
        print("Reconstructing B for Term %d" % i)
        reconst_b = np.dot(U_b[:, :i], np.dot(np.diag(sigma_b[:i]), V_b[:i, :]))

        reconstimg = np.zeros((row, col, 3))
        reconstimg[:, :, 0] = reconst_r
        reconstimg[:, :, 1] = reconst_g
        reconstimg[:, :, 2] = reconst_b
        reconstimg[reconstimg < 0] = 0
        reconstimg[reconstimg > 1] = 1

        print("Converting np Matrix to PIL Image")
        img = Image.fromarray(np.uint8(reconstimg*255))
        draw = ImageDraw.Draw(img)
        draw.text((10, 10), "%d" % i, font_col, font=font)
        img.save("processed/processed%d.png" % i, compress_level=1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Invalid Parameters")
        exit(0)
    if not os.path.exists("processed"):
        os.mkdir("processed")
    compress(sys.argv[1], int(sys.argv[2])+1, int(sys.argv[3]))



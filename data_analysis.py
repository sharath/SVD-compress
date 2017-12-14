import matplotlib
import numpy as np
matplotlib.use('agg')
import matplotlib.pyplot as plt
import sys
import re
import os


def graph(filename):
    f = open(filename, "r")
    lines = f.read().splitlines()
    f.close()
    name = []
    size = []
    comp = []
    diff = []
    for line in lines:
        pair = line.split(",")
        size.append(float(pair[0])/1024.0)
        name.append(pair[1])
        comp.append(re.findall('\\d+', pair[1]))
    uncompressed = int(size[name.index("unprocessed.png")])
    for s in size:
        diff.append(int(s) - uncompressed)

    objects = comp
    y_pos = np.arange(len(objects))
    performance = diff

    plt.figure(figsize=(10, 10))
    plt.bar(y_pos, performance)
    plt.xticks(y_pos, objects, size=1)
    plt.ylabel('Difference from Original (KB)', size=17)
    plt.title('SVD Compression Performance: "%s"' % os.path.split(filename)[1], size=17)

    if not os.path.exists("charts"):
        os.mkdir("charts")
    plt.savefig(os.path.join("charts", "%s.png" % os.path.split(filename)[1].split(".")[0]))


if __name__ == "__main__":
    graph(sys.argv[1])

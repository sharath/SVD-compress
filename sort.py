import os
import sys


def sort(directory):
    filelist = os.listdir(directory)
    pairs = []
    for file in filelist:
        location = os.path.join(directory, file)
        size = os.path.getsize(location)
        pairs.append((size, file))
    pairs.sort(key=lambda s: s[0])

    f = open("%s.csv" % dir, "w")
    for pair in pairs:
        f.write("%d, %s\n" % pair)
    f.close()


if __name__ == "__main__":
    sort(sys.argv[1])

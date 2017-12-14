# svd-compress
Final Project for MATH 545 at UMass Amherst.

Uses Singlar Value Decomposition on an Input Image and recomposes it with a different number of components in the diagonal

Warning: The script.sh will take a few hours to run.

#### Dependencies:
* numpy
* matplotlib
* pillow (Python Imaging Library)
* ffmpeg (for making animation from processed images)

#### Process valley.jpg in steps of 1 upto 500 components:

`python3 compress.py stock/valley.jpg 500 1`

#### Make animation from these processed images:

`cd valley`
`ffmpeg -framerate 24 -i processed%00d.png -c:v libx264 -profile:v high -crf 2 -preset veryslow -pix_fmt yuv420p valley.mp4`

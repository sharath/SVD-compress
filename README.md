# svd-compress
Final Project for MATH 545 at UMass Amherst

Dependencies:
* numpy
* matplotlib
* pillow (Python Imaging Library)
* ffmpeg (for making animation from processed images)

Process harold.jpg in steps of 1 upto 500 components:

`python3 compress.py stock/valley.jpg 500 1`

Make animation from these processed images:

`
cd valley
ffmpeg -framerate 24 -i processed%00d.png -c:v libx264 -profile:v high -crf 2 -preset veryslow -pix_fmt yuv420p valley.mp4
`

Warning: The script.sh will take a few hours to run.

# svd-compress
Final Project for MATH 545 at UMass Amherst

Process harold.jpg in steps of 5 upto 500 eigenvalues

`python3 compress.py stock/harold.jpg 500 5`

Make animation from processed images:

`ffmpeg -framerate 20 -i processed%00d.png -c:v libx264 -profile:v high -crf 2 -preset veryslow -pix_fmt yuv420p output.mp4`

Warning the script.sh will take a few hours to run.

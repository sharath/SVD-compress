python3 compress.py stock/valley_large.jpg 500 1
cd valley_large
ffmpeg -framerate 24 -i processed%00d.png -c:v libx264 -profile:v high -crf 10 -preset veryslow -pix_fmt yuv420p valley_large.mp4
cd ../
python3 compress.py stock/lgrt_night.jpg 500 1
cd lgrt_night
ffmpeg -framerate 24 -i processed%00d.png -c:v libx264 -profile:v high -crf 10 -preset veryslow -pix_fmt yuv420p lgrt_night.mp4
cd ../
python3 compress.py stock/dubois.jpg 500 1
cd dubois
ffmpeg -framerate 24 -i processed%00d.png -c:v libx264 -profile:v high -crf 10 -preset veryslow -pix_fmt yuv420p dubois.mp4
cd ../
python3 compress.py stock/red_galaxy.jpg 500 1
cd red_galaxy
ffmpeg -framerate 24 -i processed%00d.png -c:v libx264 -profile:v high -crf 10 -preset veryslow -pix_fmt yuv420p red_galaxy.mp4
cd ../

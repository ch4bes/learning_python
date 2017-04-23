from picamera import PiCamera
from time import sleep
from datetime import datetime

imageDir = '/home/pi/learning_python/deepsleep/images' # directory where images are saved
filename = imgDir + '/img-{timestamp:%Y-%m-%d-%H-%M}.jpg'

def main():
	camera = PiCamera()
	camera.resolution = (1024, 768)

	camera.start_preview()
	sleep(3) # time for camera to adjust
	camera.capture(filename)

if __name__ == '__main__':
	main()
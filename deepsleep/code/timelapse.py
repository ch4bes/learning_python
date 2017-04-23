from time import sleep
from picamera import PiCamera
from datetime import datetime, timedelta

def wait():
    # Calculate the delay to the start of the next min
    next_min = (datetime.now() + timedelta(minutes=1)).replace()
    delay = (next_min - datetime.now()).seconds
    sleep(delay)

camera = PiCamera()
camera.resolution = (1600, 1200)

camera.start_preview()
wait()
for filename in camera.capture_continuous('/home/pi/learning_python/deepsleep/images/img-{timestamp:%Y-%m-%d-%H-%M}.jpg'):
    print('Captured %s' % filename)
    wait()
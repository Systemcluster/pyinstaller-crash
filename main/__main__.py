import os

# setup Qt environment
if 'QT_DEVICE_PIXEL_RATIO' in os.environ:
    del os.environ['QT_DEVICE_PIXEL_RATIO']
os.environ['QT_AUTO_SCREEN_SCALE_FACTOR'] = '1'
os.environ['QT_API'] = 'pyside2'

def main():
	import qtpy
	print("Hello World!")
	print(qtpy.API_NAME)
	
main()

import os

os.environ['QT_API'] = 'pyside2'

def main():
	import qtpy
	print("Hello World!")
	print(qtpy.API_NAME)
	
main()

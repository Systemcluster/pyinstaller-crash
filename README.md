This project crashes PyInstaller 3.5+ on Windows. Test with Python 3.7 and recent Pipenv.

To reproduce, clone and navigate into this repo and run the following commands:

```cmd
pipenv install

pipenv run pip install https://github.com/pyinstaller/pyinstaller/archive/develop.zip

pipenv run pyinstaller --clean --log-level DEBUG  .\main.spec
```

You should see a stacktrace ending with `win32ctypes.pywin32.pywintypes.error: (2, 'LoadLibraryExW', 'The system cannot find the file specified.')`.

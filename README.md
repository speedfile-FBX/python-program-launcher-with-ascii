for those who don't know  to use pyinstaller with PYfiglet you have to write this
pyinstaller --onefile --add-data "C:\Users\<usernamehere>\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pyfiglet\fonts;pyfiglet\fonts" pythonappname.py
that worked for me

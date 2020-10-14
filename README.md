# py_microapps
Package of my Python's micro projects.
## List of apps
```
Graph ping
FTP Monitor
Math operations
Transcriptor
and other
```
# Requiments 
## Install from pip
```
win10toast (with fix)
configparser
pymsgbox
ftplib
consolemenu
math
matplotlib
pythonping
```
## Fixes
### Fix win10toast
you need to move file `__init__.py` to the directory of your python to support the action on click on the notification
For example, standart directory is: `%localappdata%\Programs\Python\Python39\Lib\site-packages\win10toast`

# FAQ and How-To-Use
## Python Ping FAQ
#### Requied packages
- matplotlib (link). To install type this command in your console - `pip install matplotlib`
- Python Ping (link). To install type this command in your console- `pip install pythonping`
#### Features
- Show Ping graph
- Set visible of graph`s grid
- Set your own ping time
- [in dev] Set your own timeout param
____
#### How to use?
You must follow directions by program in your console. In end of the test, program will show you window with Ping Graph. You can save image of graph on your PC.
## FTP Monitor FAQ
#### How to use
First, you need to open the ftp_settings.ini file and specify the settings for your file storage there. All instructions are inside the file
Then, just start the application and follow the instructions

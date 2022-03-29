#import PyInstaller.__main__, configparser, logging ; from easygui import *

#config = configparser.ConfigParser()

#def configs(author, version, release_date, compile_date, ):
 #   with open("packaged.ini"):
  #      pass
#version = textbox("Enter the new version of the software","Tools.py")
#root = fileopenbox("Please select the main file","Tools.py",filetypes=["*.py","*.pyw*"])

import PyInstaller.__main__, configparser, loggig ; from easygui import *

"""
Contains one mode currenntly:
Basiic.
This mode contains:
PytoExe (See planner)
Basic (uncustomisable) app installer

More might be added soonn but I'm 
very busy at the moment so there might not be!
Thannk you for using my tool!
"""

class normal:
    def pytoexe(onedir, onefile, specpath, name, console, icon):
        flags = ['main.py']
        if onedir == True:
            flags.append('--onedir')
        if onefile == True:
            flags.append('--onefile')
        flags.append('-n ', name)
        flags.append('--specpath ', specpath)
        if console == True:
            flags.append('-c')
        else:
            flags.append('-w')
        if icon != "":
            flags.append('-i ', icon)  
        PyInstaller.__main__.run([flags])
    
    def app_install_base(appname, version ,author, releasedate):
        pass

class basic:
    def __init__(self):
        pass
    
    def do_publish(self):
        pass
    
    

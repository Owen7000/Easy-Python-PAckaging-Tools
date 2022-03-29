import PyInstaller.__main__, configparser, logging ; from easygui import *

config = configparser.ConfigParser()

def configs(author, version, release_date, compile_date, ):
    with open("packaged.ini"):
        pass
version = textbox("Enter the new version of the software","Tools.py")
root = fileopenbox("Please select the main file","Tools.py",filetypes=["*.py","*.pyw*"])



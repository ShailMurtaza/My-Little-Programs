from distutils.core import setup
import py2exe
setup(
publisher = 'shail',
copyright = 'Coping is not allowed',
name = 'Windows Softwares',
description = 'This software is very valuable which is created by Shail HACKER',
version = '1.0',
#console=['python.py'],
console = [
{
"script": "vee.py",
"icon_resources": [(0, "F:\shail\Icon/html5.ico")]
}
],
# options = {'py2exe': {'bundle_files': 1,'packages':'ctypes','includes': 'base64,sys,socket,struct,time,code,platform,getpass,shutil',}},
options = {'py2exe': {'bundle_files': 1,}},
zipfile = None,
)
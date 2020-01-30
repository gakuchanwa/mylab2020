import os
import pprint
import time

sleep_time = 60

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

os.chdir(os.path.dirname(os.path.abspath(__file__)))
gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

photo_path = '/home/pi/googledrive/pydrive-example/src/rpiphoto.jpg'
ondo_path = '/home/pi/googledrive/pydrive-example/src/ondo.txt'

while True:
    f = drive.CreateFile()
    f.SetContentFile(photo_path)
    f['title'] = os.path.basename(photo_path)
    f.Upload()
    f_txt = drive.CreateFile()
    f_txt.SetContentFile(ondo_path)
    f_txt['title'] = os.path.basename(ondo_path)
    print(f_txt)
    f_txt.Upload()
    time.sleep(sleep_time)

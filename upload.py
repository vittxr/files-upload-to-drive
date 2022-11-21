from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth() 
# Automate the authentication. You need settings.yaml file.
gauth.LocalWebserverAuth() 
drive = GoogleDrive(gauth)

file = 'test.png'

# Create an instace of googleDriveFile. The arguments is the last part of url, the id of your drive folder. 
gfile = drive.CreateFile({'parents': [{'id': '1xL_BaXesXia0ykWkQNlfSIf4g59O9e2k'}]})

# Read file and set it as the content of this instance.
gfile.SetContentFile(file)
gfile.Upload() # Upload the file.
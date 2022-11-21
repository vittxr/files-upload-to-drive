from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()

# Automate the authentication. You need settings.yaml file.
gauth.LocalWebserverAuth() 

drive = GoogleDrive(gauth)

file = 'test.png'

# Create an instace of googleDriveFile. The argument is the file id.
fileList = drive.ListFile({'q': "'1xL_BaXesXia0ykWkQNlfSIf4g59O9e2k' in parents and trashed=false"}).GetList()
for file in fileList: 
   print(file)
   gfile = drive.CreateFile({'id': file['id']})
   # Read file and set it as the content of this instance.
   print(gfile)
   gfile.Delete()
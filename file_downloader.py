import requests
from io import BytesIO
from zipfile import ZipFile

def download_file(link, new_name):
  request = requests.get(link, allow_redirects=True)
  return unzip_content(request.content, new_name)


def unzip_content(content, new_name):
  with ZipFile(BytesIO(content)) as zip_file:
    for file in zip_file.namelist():
      file_bytes = zip_file.open(file).read()
      if open(new_name, 'wb').write(file_bytes) == 0:
        return False
    
    return True

import pywebio
from pywebio.input import *
import requests

def uploadFile():
  img = file_upload("Envie sua imagem:", accept="image/*")

  url = 'http://localhost:5000/processImage'
  myobj = {"id": "2", "name": "BBBB"}

  x = requests.post(url, data = myobj)

  print(x.text)

if __name__ == '__main__':
    pywebio.start_server(uploadFile, port=3000)
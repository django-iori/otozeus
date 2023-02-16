from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import FileResponse
from .models import *
import os
import subprocess
import re
from time import sleep
from pathlib import Path
import os
import datetime
from django.http import HttpResponse

#.mov -> .mp4
def MovToMp4(path,root):
    date = datetime.datetime.now()
    date = str(date.year) + "-" + str(date.month) + "-" + str(date.day) + "_" + str(date.hour) + "-" + str(date.minute) + "-" + str(date.second) + "-" + str(date.microsecond) + ".mp4"
    mp4 = os.path.join(root, date)
    print("ffmpeg -i \""+path+"\" \""+mp4+"\"")
    subprocess.run("ffmpeg -i \""+path+"\" \""+mp4+"\"", shell=True)
    return mp4

# -> .mp3
def M4aToMp3(origin_path,root):
    date = datetime.datetime.now()
    file_name = str(date.year) + "-" + str(date.month) + "-" + str(date.day) + "_" + str(date.hour) + "-" + str(date.minute) + "-" + str(date.second) + "-" + str(date.microsecond)
    extension = ".mp3"
    mp3_path = os.path.join(root, "mp3", file_name + extension)
    print("ffmpeg -i \""+origin_path+"\" \""+mp3_path+"\"")
    subprocess.run("ffmpeg -i \""+origin_path+"\" \""+mp3_path+"\"", shell=True)
    return mp3_path, file_name

def Mp3ToM4a(mp3_path):
    m4a_path = mp3_path.replace("mp3", "m4a")
    print("ffmpeg -i \""+mp3_path+"\" \""+m4a_path+"\"")
    subprocess.run("ffmpeg -i \""+mp3_path+"\" \""+m4a_path+"\"", shell=True)
    return m4a_path
    

class UploadFromIOS(APIView):
    def post(self, request, format=None):
        filename = str(request.data['audio'])
        upload = request.data['audio']
        filepath = os.path.join(Path(__file__).resolve().parent.parent, 'media', 'uploads', filename)
        rootpath = os.path.join(Path(__file__).resolve().parent.parent, 'media')
        # media/uploads/に保存
        with open(filepath, 'wb') as f:
            for chunk in upload.chunks():
                f.write(chunk)
        mp3_path, file_name = M4aToMp3(filepath, rootpath)
        sleep(3)
        deliverable_path = Mp3ToM4a(mp3_path)
        sleep(3)
        os.remove(filepath)
        deliverable = open(deliverable_path, "rb")
        return FileResponse(deliverable, filename=file_name)

class DeleteView(APIView):
    def post(self, request, format=None):
        filename = str(request.data['filename'])
        extensions = [".mp3", ".m4a"]
        mp3_path = os.path.join(Path(__file__).resolve().parent.parent, 'media', 'mp3', filename + extensions[0])
        m4a_path = os.path.join(Path(__file__).resolve().parent.parent, 'media', 'm4a', filename + extensions[1])
        os.remove(mp3_path)
        os.remove(m4a_path)
        return Response("delete completed!")

#動作確認用
def index_template(request):
    return render(request, 'index.html')

def test(request):
    return HttpResponse("Hello World")
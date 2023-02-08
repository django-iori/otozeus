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
def M4aToMp3(path,root):
    date = datetime.datetime.now()
    file_name = str(date.year) + "-" + str(date.month) + "-" + str(date.day) + "_" + str(date.hour) + "-" + str(date.minute) + "-" + str(date.second) + "-" + str(date.microsecond)
    extension = ".mp3"
    mp3 = os.path.join(root, file_name + extension)
    print("ffmpeg -i \""+path+"\" \""+mp3+"\"")
    subprocess.run("ffmpeg -i \""+path+"\" \""+mp3+"\"", shell=True)
    return mp3, file_name

class DemoView(APIView):
    def post(self, request, format=None):
        filename = str(request.data['stream'])
        demo = Demo()
        demo.video = request.data['stream']
        demo.save()
        sleep(1)
        filepath = os.path.join(Path(__file__).resolve().parent.parent, 'media', 'uploads', filename)
        rootpath = os.path.join(Path(__file__).resolve().parent.parent, 'media')
        """ MovToMp4(filepath, rootpath) """
        audio_path, file_name = M4aToMp3(filepath, rootpath)
        os.remove(filepath)
        audio = open(audio_path, "rb")
        return FileResponse(audio, filename=file_name)

class DeleteView(APIView):
    def post(self, request, format=None):
        filename = str(request.data['filename'])
        extension = ".mp3"
        filepath = os.path.join(Path(__file__).resolve().parent.parent, 'media', filename + extension)
        os.remove(filepath)
        return Response("delete completed!")

#動作確認用
def index_template(request):
    return render(request, 'index.html')

def test(request):
    return HttpResponse("Hello World")
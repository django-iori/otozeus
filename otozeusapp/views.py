from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
import os
import subprocess
import re
from time import sleep
from pathlib import Path
import os
import datetime

#.mov -> .mp4
def MovToMp4(path,root):
    date = datetime.datetime.now()
    date = str(date.year) + "-" + str(date.month) + "-" + str(date.day) + "_" + str(date.hour) + "-" + str(date.minute) + "-" + str(date.second) + "-" + str(date.microsecond) + ".mp4"
    mp4 = os.path.join(root, date)
    print("ffmpeg -i \""+path+"\" \""+mp4+"\"")
    subprocess.run("ffmpeg -i \""+path+"\" \""+mp4+"\"", shell=True)

# -> .mp3
def M4aToMp3(path,root):
    date = datetime.datetime.now()
    date = str(date.year) + "-" + str(date.month) + "-" + str(date.day) + "_" + str(date.hour) + "-" + str(date.minute) + "-" + str(date.second) + "-" + str(date.microsecond) + ".mp3"
    mp3 = os.path.join(root, date)
    print("ffmpeg -i \""+path+"\" \""+mp3+"\"")
    subprocess.run("ffmpeg -i \""+path+"\" \""+mp3+"\"", shell=True)

class DemoView(APIView):
    def post(self, request, format=None):
        filename = str(request.data['stream'])
        demo = Demo()
        demo.video = request.data['stream']
        demo.save()
        sleep(1)
        filepath = os.path.join(Path(__file__).resolve().parent.parent, 'media', 'uploads', filename)
        rootpath = os.path.join(Path(__file__).resolve().parent.parent, 'media')
        print(filepath)
        """ MovToMp4(filepath, rootpath) """
        M4aToMp3(filepath, rootpath)
        return Response({ 'success': 'file accepted' })

#動作確認用
def index_template(request):
    return render(request, 'index.html')


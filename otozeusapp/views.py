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
    """ print("ffmpeg.exe -i \""+path+"\"")
    result = subprocess.run("ffmpeg.exe -i \""+path+"\"", shell=True, stderr=subprocess.PIPE, universal_newlines=True)
    m = re.search("(?<=com.apple.quicktime.creationdate: )(.*)" , result.stderr)
    date = m.group(0)
    date = date[:-5]
    date = date.replace('T', ' ')
    date = date.replace(':', '.')
    date = date + ".mp4"
    mp4 = os.path.join(root,date) """
    date = datetime.datetime.now()
    date = str(date.year) + "-" + str(date.month) + "-" + str(date.day) + "_" + str(date.hour) + "-" + str(date.minute) + "-" + str(date.second) + "-" + str(date.microsecond) + ".mp4"
    mp4 = os.path.join(root, date)
    print("ffmpeg.exe -i \""+path+"\" \""+mp4+"\"")
    subprocess.run("ffmpeg.exe -i \""+path+"\" \""+mp4+"\"", shell=True)

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
        MovToMp4(filepath, rootpath)
        return Response({ 'success': 'file accepted' })

#動作確認用
def index_template(request):
    return render(request, 'index.html')


from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *

class DemoView(APIView):
    def post(self, request, format=None):
        demo = Demo()
        demo.video = request.data['stream']
        demo.save()
        print(request.data['stream'])
        return Response({ 'success': 'file accepted' })

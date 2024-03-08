from django.shortcuts import render

from django.views.decorators.http import require_http_methods
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.views import APIView
@api_view(['GET'])
# @renderer_classes((JSONRenderer))
def index(request):

    data = {'message': 'Rentoro Index'}
    return Response(data, status=status.HTTP_200_OK)

class RentalView(APIView):

    def get(self, request):
        pass


    def post(self, request):
        pass


    def put(self, request):
        pass

class LeasingView(APIView):


    def get(self, request):
        pass


    def post(self, request):
        pass


    def put(self, request):
        pass

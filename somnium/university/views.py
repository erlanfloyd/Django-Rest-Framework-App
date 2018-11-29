from django.shortcuts import render
from rest_framework import viewsets
from .models import University, Rectorat, Kafedra, Prorector
from .serializers import UniversitySerializer

class UniversityView(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer



class RectoratView(viewsets.ModelViewSet):
    queryset = Rectorat.objects.all()
    serializer_class = RectoratSerializer



class KafedraView(viewsets.ModelViewSet):
    queryset = Kafedra.objects.all()
    serializer_class = KafedraSerializer
    


class ProrectorView(viewsets.ModelViewSet):
    queryset = Prorector.objects.all()
    serializer_class = ProrectorSerializer
        
    
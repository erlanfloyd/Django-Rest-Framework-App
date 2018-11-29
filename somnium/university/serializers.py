from rest_framework import serializers
from .models import University, Rectorat, Kafedra

class UniversitySerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = University
        fields = ('id', 'url', 'rectorat', 'kafedra', 'prorector', 'director', 'audit')


class RectoratSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = Rectorat
        fields = ('id', 'url', 'name')


class KafedraSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = Kafedra
        fields = ('id', 'url', 'name', 'university')



class ProrectorSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = Prorector
        fields = ('id', 'url', 'name', 'university')
        
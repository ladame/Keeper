from django.shortcuts import render
from rest_framework import viewsets
from .serializers import KeeperSerializer
from .models import Keeper

# Create your views here.

class KeeperView(viewsets.ModelViewSet):
    serializer_class = KeeperSerializer
    queryset = Keeper.objects.all()

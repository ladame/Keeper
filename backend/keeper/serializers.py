from rest_framework import serializers
from .models import Keeper

class KeeperSerializer(serializers.ModelSerializer):

    class Meta:
        model = Keeper 
        fields = ('id', 'title', 'note')
from rest_framework import serializers
from .models import Model

class ModelSerializer(serializers.ModelSerializer):
    # roll = serializers.IntegerField()
    class Meta:
        model = Model
        fields = '__all__'
        # fields = ('name','age','email','phone','address')

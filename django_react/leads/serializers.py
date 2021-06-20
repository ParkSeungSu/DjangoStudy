from rest_framework import serializers
from .models import Lead

class LeadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lead
        exclude = ('id','name','email','message')
        depth = 4
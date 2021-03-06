from .models import Register
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ('url','id','student','offered_course','advisor_status')

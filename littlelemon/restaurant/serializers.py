from rest_framework.serializers import serializers, generics
from .models import Booking, Menu


class UserSerializer(serialiers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email','groups']
        
        
class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        felds = '__all__'
        
        
        
class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
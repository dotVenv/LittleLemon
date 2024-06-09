from rest_framework import serializers, generics
from .models import Booking, Menu, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email','groups']
        
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        felds = '__all__'
        
        
        
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
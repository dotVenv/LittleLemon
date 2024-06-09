from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from .serializers import * 


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class MenuItemsView(generics.ListCreateAPIView):
    
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    
        
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
   

class UserViewset(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    
    
    
    
    
    
"""def get(self, request):
    items = Booking.objects.all()
    serializer = bookingSerializer(items, many=True)
    return Response(serializer.data)
def post(self, request):
    serializer = bookingSerializer(request.data)
    if serializer.is_valid():
        return Response({'status': "success", 'data': serializer.data})
def get(self, request, id):
    items = Menu.objects.all(id=id)
    serializer = menuSerializer(items, many=True)
    return Response(serializer.data)

def post(self, request):
    serializer = menuSerializer(request.data)
    if serializer.is_valid():
        return Response({'status': "success", 'data': serializer.data})
def get(self, request):
    items = Menu.objects.all()
    serializer = menuSerializer(items, many=True)
    return Response(serializer.data)
def post(self, request):
    serializer = menuSerializer(request.data)
    if serializer.is_valid():
        return Response({'status': "success", 'data': serializer.data})"""
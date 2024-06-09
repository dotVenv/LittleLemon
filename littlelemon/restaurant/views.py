from django.shortcuts import render
from rest_framework.views import APIView
from rest_frameworkresponse import Response
from .serializers import * 
# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class MenuItemsView(generics.ListCreateAPIView):
    
    queryset = Menu.objects.all()
    serializer_class = menuSerializer()
    
    """def get(self, request):
        items = Menu.objects.all()
        serializer = menuSerializer(items, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = menuSerializer(request.data)
        if serializer.is_valid():
            return Response({'status': "success", 'data': serializer.data})"""
        
class SingleMenuIitemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer()
    """def get(self, request, id):
        items = Menu.objects.all(id=id)
        serializer = menuSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = menuSerializer(request.data)
        if serializer.is_valid():
            return Response({'status': "success", 'data': serializer.data})"""

class bookingview(generics.ListCreateAPIView):
    
    def get(self, request):
        items = Booking.objects.all()
        serializer = bookingSerializer(items, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = bookingSerializer(request.data)
        if serializer.is_valid():
            return Response({'status': "success", 'data': serializer.data})
        
        
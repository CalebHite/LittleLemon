from rest_framework import serializers
from .models import Menu, Booking

class MenuSerializer(serializers.ModelSerializer):  
    name = serializers.CharField()
    no_of_guests = serializers.IntegerField()
    booking_data = serializers.DateTimeField()
    class Meta:
        model = Menu
        fields = ('id', 'name', 'no_of_guests', 'booking_data')
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
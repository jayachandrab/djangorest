from django.shortcuts import render

from flightApp.models import Flight, Passenger, Reservation

from flightApp.serializers import FlightSerializer,PassengerSerializer, ReservationSerializer

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['POST'])
def findFlights(request):
    print(request.data['departureCity'])
   
    flights= Flight.objects.filter(departureCity=request.data['departureCity'],arrivalCity= request.data['arrivalCity'],dateOfDeparture=request.data['dateOfDeparture'])
    #print("====="+Response(serializer.data))
    serializer= FlightSerializer(flights, many=True)
    return Response(serializer.data)
    
@api_view(['POST'])
def save_reservation(request):
    flight=Flight.objects.get(id=request.data['flightId'])
    passenger=Passenger()
    passenger.firstName=request.data['firstName']
    passenger.lastName=request.data['lastName']
    passenger.middleName=request.data['middleName']
    passenger.email=request.data['email']
    passenger.phone=request.data['phone']
    passenger.save()
    reservation=Reservation()
    reservation.flight=flight
    reservation.passenger=passenger
    Reservation.save(reservation)
    return Response(status=status.HTTP_201_CREATED)







class FlightViewset(viewsets.ModelViewSet):
    queryset=Flight.objects.all()
    serializer_class=FlightSerializer

class PassengerViewset(viewsets.ModelViewSet):
    queryset=Passenger.objects.all()
    serializer_class=PassengerSerializer

class ReservationViewset(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer
    




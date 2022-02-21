from django.shortcuts import render
from flightApp.models import Flight, Passenger,Reservation
from flightApp.serializers import FlightSerializer,PassengerSerializer, ReservationSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated



@api_view(['GET','POST'])
def reservation_operations(request):
    if request.method == 'GET':
        students =Student.objects.filter(departureCity=departureCity,arrivalCity=arrivalCity,dateOfDeparture=dateOfDeparture)
        serializer=StudentSerializer(students.many==True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class FlightViewSet(viewsets.ModelViewSet):
    queryset=Flight.objects.all()
    serializer_class=FlightSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['departureCity','arrivalCity', 'dateOfDeparture']
    permission_classes = (IsAuthenticated,)

class PassengerViewSet(viewsets.ModelViewSet):
    queryset=Passenger.objects.all()
    serializer_class=PassengerSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer

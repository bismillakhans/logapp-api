from rest_framework import viewsets
from logapp.models import Entry,Vehicle
from .serializers import EntrySerializer,VehicleSerializer

class EntryViewSet(viewsets.ModelViewSet):
    serializer_class = EntrySerializer
    queryset = Entry.objects.all()


class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()


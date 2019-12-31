from rest_framework import serializers

from logapp.models import Vehicle,Entry


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('id', 'vehicle_number', 'time_arrival','time_leave','time_duration')


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('id', 'vehicle_number', 'vehicle_type', 'mobile_number', 'is_staff','status')



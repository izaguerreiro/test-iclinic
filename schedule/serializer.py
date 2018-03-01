""" API REST """

from rest_framework import serializers
from schedule.models import Schedule


class ScheduleSerializer(serializers.ModelSerializer):
    """ API to create, update, delete and list schedules """

    class Meta:
        """ Class Meta """
        model = Schedule
        fields = '__all__'

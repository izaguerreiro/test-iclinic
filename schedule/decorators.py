""" Validate date and time """

from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from schedule.models import Schedule


def is_range_conflict(date, start, end):
    """ Verify if time is conflict with other time """
    range_start = Schedule.objects.filter(
        date=date, start_time__range=(start, end)).exists()

    range_end = Schedule.objects.filter(
        date=date, end_time__range=(start, end)).exists()

    within_range = Schedule.objects.filter(
        date=date, start_time__lte=start, end_time__gte=end).exists()
    
    return range_start is True or range_end is True or within_range is True
    

def validate_date_time_exists(func):
    """ Decorator to validate date and time already exist """
    def validate(self, request, **kwargs):
        date = request.data['date']
        start = request.data['start_time']
        end = request.data['end_time']

        if is_range_conflict(date, start, end):
            return Response(
                'Horário indisponível', status=status.HTTP_400_BAD_REQUEST)
        return func(self, request, **kwargs)
    return validate

""" Validate date and time """

from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from schedule.models import Schedule


def validate_date_time_exists(func):
    """ Decorator to validate date and time already exist """
    def validate(self, request, **kwargs):
        start = request.data['start_time']
        end = request.data['end_time']
        date_exists = Schedule.objects.filter(
            Q(date=request.data['date']),
            Q(start_time__range=(start, end)) |
            Q(end_time__range=(start, end))
        ).exists()

        if date_exists:
            return Response(
                'Data e hora indisponíveis', status=status.HTTP_400_BAD_REQUEST
            )
        return func(self, request, **kwargs)
    return validate

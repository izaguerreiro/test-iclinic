""" Views file """

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from schedule.models import Schedule
from schedule.serializer import ScheduleSerializer


class ScheduleList(APIView):
    """ List all schedules or create a new schedule """

    def get(self, request, format=None):
        """ List all schedules """
        serializer = ScheduleSerializer(Schedule.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """ Create a new schedule """
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ScheduleDetail(APIView):
    """ Retrieve, update or delete a schedule instance """

    def get_object(self, pk):
        """ Returns a specific schedule or an error """
        try:
            return Schedule.objects.get(pk=pk)
        except Schedule.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """ Get a specific schedule """
        schedule = self.get_object(pk)
        serializer = ScheduleSerializer(schedule)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """ Update a schedule """
        schedule = self.get_object(pk)
        serializer = ScheduleSerializer(schedule, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """ Delete a schedule """
        schedule = self.get_object(pk)
        schedule.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

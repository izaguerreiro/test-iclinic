""" Test get in API """

from django.test import TestCase
from schedule.models import Schedule


class TestScheduleDetail(TestCase):
    """ Test get schedule detail """

    fixtures = ['schedule.json']

    def setUp(self):
        self.schedule = Schedule.objects.get(pk=1)
        self.response = self.client.get(
            '/api/schedules/{}/'.format(self.schedule.pk),
            content_type='application/json'
        )

    def test_status_code(self):
        """ Check request status """
        self.assertEqual(200, self.response.status_code)

    def test_date(self):
        """ Check if the date is correct """
        self.assertEqual(str(self.schedule.date), self.response.data['date'])

    def test_start_time(self):
        """ Check if the start time is correct """
        self.assertEqual(
            str(self.schedule.start_time), self.response.data['start_time'])

    def test_end_time(self):
        """ Check if the end time is correct """
        self.assertEqual(
            str(self.schedule.end_time), self.response.data['end_time'])

    def test_patient(self):
        """ Check if the patient is correct """
        self.assertEqual(self.schedule.patient, self.response.data['patient'])

    def test_procedure(self):
        """ Check if the procedure is correct """
        self.assertEqual(
            self.schedule.procedure, self.response.data['procedure'])

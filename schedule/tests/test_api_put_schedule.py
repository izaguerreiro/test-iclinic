""" Test put in API """

from json import dumps
from django.test import TestCase
from schedule.models import Schedule


class TestPutSchedule(TestCase):
    """ Test put schedule """

    fixtures = ['schedule.json']

    def setUp(self):
        self.schedule = Schedule.objects.get(pk=1)
        data = {
            'date': '2018-03-02', 'start_time': '10:00:00',
            'end_time': '11:00:00', 'patient': self.schedule.patient,
            'procedure': self.schedule.procedure
        }
        self.response = self.client.put(
            '/api/schedules/{}/'.format(self.schedule.pk), dumps(data),
            content_type='application/json'
        )
        self.schedule_update = Schedule.objects.get(pk=1)

    def test_status_code(self):
        """ Check request status """
        self.assertEqual(200, self.response.status_code)

    def test_date(self):
        """ Check if the date has changed """
        self.assertNotEqual(self.schedule.date, self.schedule_update.date)

    def test_start_time(self):
        """ Check if the start time has changed """
        self.assertNotEqual(
            self.schedule.start_time, self.schedule_update.start_time)

    def test_end_time(self):
        """ Check if the end time has changed """
        self.assertNotEqual(
            self.schedule.end_time, self.schedule_update.end_time)

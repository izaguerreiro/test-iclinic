""" Test post in API """

from json import dumps
from django.test import TestCase

from schedule.models import Schedule


class TestPostSchedule(TestCase):
    """ Test post schedule """

    def setUp(self):
        data = {
            'date': '2018-02-28', 'start_time': '10:00:00',
            'end_time': '11:00:00', 'patient': 'Izabela Guerreiro',
            'procedure': 'Consulta de rotina'
        }
        self.response = self.client.post(
            '/api/schedules/', dumps(data),
            content_type='application/json'
        )

    def test_status_code(self):
        """ Check request status """
        self.assertEqual(201, self.response.status_code)

    def test_response_content_type(self):
        """ Check the submitted content type """
        self.assertEqual('application/json', self.response.get('Content-Type'))

    def test_schedule_created(self):
        """ Check if object has created """
        self.assertTrue(Schedule.objects.exists())

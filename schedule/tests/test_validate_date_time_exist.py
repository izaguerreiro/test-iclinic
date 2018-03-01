""" Test validate data and time exists """

from json import dumps
from django.test import TestCase


class TestValidateDateTime(TestCase):
    """ Test validate date and time exists """

    fixtures = ['schedule.json']

    def setUp(self):
        data = {
            'date': '2018-02-28', 'start_time': '21:28:43',
            'end_time': '21:28:44', 'patient': 'Izabela Guerreiro',
            'procedure': 'Consulta de rotina'
        }
        self.response = self.client.post(
            '/api/schedules/', dumps(data),
            content_type='application/json'
        )

    def test_status_code(self):
        """ Check request status """
        self.assertEqual(400, self.response.status_code)

    def test_response_content_type(self):
        """ Check the submitted content type """
        self.assertEqual('application/json', self.response.get('Content-Type'))

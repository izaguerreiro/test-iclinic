""" Test delete in API """

from json import dumps
from django.test import TestCase
from schedule.models import Schedule


class TestPutSchedule(TestCase):
    """ Test delete schedule """

    fixtures = ['schedule.json']

    def setUp(self):
        self.response = self.client.delete(
            '/api/schedules/1/', content_type='application/json'
        )

    def test_status_code(self):
        """ Check request status """
        self.assertEqual(204, self.response.status_code)

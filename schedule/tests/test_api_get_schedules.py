""" Test get in API """

from django.test import TestCase


class TestScheduleList(TestCase):
    """ Test get schedule list """

    fixtures = ['schedule.json']

    def setUp(self):
        self.response = self.client.get(
            '/api/schedules/', content_type='application/json'
        )

    def test_status_code(self):
        """ Check request status """
        self.assertEqual(200, self.response.status_code)

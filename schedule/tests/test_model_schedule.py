""" Test model Schedule """

from datetime import datetime
from django.test import TestCase
from schedule.models import Schedule


class TestScheduleModel(TestCase):
    """ Class to test schedule model """
    def setUp(self):
        self.date = datetime.now().date()
        self.time = datetime.now().time()
        self.schedule = Schedule.objects.create(
            date=self.date, start_time=self.time,
            end_time=self.time, patient='Izabela Guerreiro',
            procedure='Consulta de rotina'
        )

    def test_create(self):
        """ Checks if a schedule exists  """
        self.assertTrue(Schedule.objects.exists())

    def test_date(self):
        """ Checks if date is correct """
        self.assertEqual(self.date, self.schedule.date)

    def test_start_time(self):
        """ Checks if start time is correct """
        self.assertEqual(self.time, self.schedule.start_time)

    def test_end_time(self):
        """ Checks if end time is correct """
        self.assertEqual(self.time, self.schedule.end_time)

    def test_patient(self):
        """ Checks if patient is correct """
        self.assertEqual('Izabela Guerreiro', self.schedule.patient)

    def test_procedure(self):
        """ Checks if procedure is correct """
        self.assertEqual('Consulta de rotina', self.schedule.procedure)

    def test_str(self):
        """ Checks if return str is correct """
        self.assertEqual('Izabela Guerreiro', str(self.schedule))

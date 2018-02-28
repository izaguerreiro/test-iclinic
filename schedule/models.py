""" Models """
from django.db import models


class Schedule(models.Model):
    """ Model for schedules """
    date = models.DateField('data')
    start_time = models.TimeField('horário de início')
    end_time = models.TimeField('horário final')
    patient = models.CharField('paciente', max_length=255)
    procedure = models.TextField('procedimento')

    def __str__(self):
        return self.patient

    class Meta:
        """ Class Meta """
        verbose_name = 'agenda'
        verbose_name_plural = 'agendas'

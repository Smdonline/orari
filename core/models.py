from django.db import models

class SMDManager(models.Model):
    nome = models.CharField(verbose_name='nome manager', max_length=255)
    cognome = models.CharField(verbose_name='cognome manager', max_length=255)
    ore = models.PositiveSmallIntegerField(verbose_name='ore settimanale', default=40)
    email = models.EmailField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.nome, self.cognome)


class Turno(models.Model):
    dip = models.ForeignKey(SMDManager,on_delete=models.CASCADE, related_name='turni')
    giorno = models.DateField()
    inizio = models.DateTimeField()
    fine = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s - %s -[%s %s ]' % (self.dip, self.giorno, self.inizio, self.fine)
    def durata(self):
        return self.fine - self.inizio
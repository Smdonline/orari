from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
import datetime
from core import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
# Create your views here.
days = [
    (0, _("Monday")), (1, _("Tuesday")), (2, _("Wednesday")),
    (3, _("Thursday")), (4, _("Friday")), (5, _("Saturday")),
    (6, _("Sunday"))
]
class ListTurni(ListView):
    model = models.Turno
    template_name = 'home/index.html'
    ordering = '-giorno'
    context_object_name = 'turni'
    date_field = 'giorno'

    def get_queryset(self):
        today = datetime.date.today()
        lunedi = today - datetime.timedelta(days=today.weekday() % 7)

        domenica = lunedi + datetime.timedelta(days=6)
        print(lunedi, "  ", domenica)
        querry =models.Turno.objects.all().filter(Q(giorno__range=[lunedi,domenica])).order_by('giorno')
        orari = {}
        for numar, zi in days:
            orari[zi] = [i for i in querry if i.giorno.weekday() == numar]
        return orari



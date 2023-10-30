from django import forms
from . import models
from django.db.models import Q

class TurnoForm(forms.ModelForm):
    class Meta:
        model = models.Turno
        fields = ('dip', 'giorno', 'inizio', 'fine')

    def clean_fine(self):
        giorno = self.cleaned_data.get('giorno')
        fine = self.cleaned_data.get('fine')
        inizio = self.cleaned_data.get('inizio')
        if fine.date() < giorno:
            raise forms.ValidationError('la fine deve essere piu grande di %s' % giorno)
        if fine <= inizio:
            raise forms.ValidationError('la fine deve essere pi grande di %s ' % inizio)
        return fine
    def clean_inizio(self):
        giorno = self.cleaned_data.get('giorno')
        inizio = self.cleaned_data.get('inizio')
        if inizio.date() < giorno:
            raise forms.ValidationError('%s deve essere piu grande di %s' % (inizio, giorno))

        return inizio


    def clean(self):
        clean_data = self.cleaned_data
        giorno=clean_data.get('giorno')
        inizio=clean_data.get('inizio')
        fine=clean_data.get('fine')
        dip = clean_data.get('dip')
        turni  = models.Turno.objects.all().filter(dip=dip, giorno=giorno
        ).exclude(id=self.instance.pk)
        if turni:
            for turno in turni:
                if inizio >= turno.inizio and inizio < turno.fine:
                    raise forms.ValidationError('esiste gia un turno [%s %s] che contiene %s' % (turno.inizio.strftime("%H:%M"),turno.fine.strftime("%H:%M"),inizio.strftime("%H:%M")))
                if fine > turno.inizio and fine <= turno.fine:
                    raise forms.ValidationError('esiste gia un turno [%s %s] che contiene %s' % (turno.inizio.strftime("%H:%M"),turno.fine.strftime("%H:%M"),fine.strftime("%H:%M")))


        return clean_data




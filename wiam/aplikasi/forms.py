# forms.py
from django import forms
from .models import Anggota

class AnggotaForm(forms.ModelForm):
    class Meta:
        model = Anggota
        fields = ['nama', 'nim', 'alamat']

class PinjamBukuForm(forms.Form):
    buku_id = forms.IntegerField()
    anggota_id = forms.IntegerField()

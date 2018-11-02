from django import forms

class LaporanForm(forms.Form):
    tgl_awal = forms.CharField(max_length=20)
    tgl_akhir = forms.CharField(max_length=20)

from django.db import models
from pendaftaran.pilihan import *
import datetime

class DataObat(models.Model):
    '''
    Model Untuk Data Obat
    fungsi kadaluwarsa() self explanatory
    '''
    nama_obat = models.CharField(max_length=50, help_text="Masukkan nama obat dan dosisnya")
    satuan = models.CharField(max_length=3, choices=SAT_OBAT_CHOICES, help_text="Satuan pemakaian obat", blank=True)
    jumlah = models.PositiveIntegerField(help_text="Jumlah")
    tanggal_kadaluwarsa = models.DateField(help_text="Masukkan tanggal ED yang paling dekat", blank=True)
    no_batch = models.CharField(max_length=30, blank=True, help_text="Pisahkan dengan \";\" bila lebih dari 1")
    generik = models.BooleanField(default=True, help_text="Tandai bila termasuk obat generik")
    def __str__(self):
        return self.nama_obat
    def kadaluwarsa(self):
        hitung_delta = (self.tanggal_kadaluwarsa - datetime.date.today()) / 30
        sisa_bulan = str(hitung_delta.days)
        return sisa_bulan + " Bulan"
    kadaluwarsa.short_description = 'Waktu Kadaluwarsa'
    class Meta:
        verbose_name_plural = 'Daftar Obat & Bahan Habis Pakai'
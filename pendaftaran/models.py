from django.db import models
from .pilihan import *
from apotek.models import DataObat
import datetime

class DataPasien(models.Model):
    """
    Model Untuk Data Pasien
    fungsi usia() untuk menghitung usia dengan cara tanggal hari ini dikurangi tanggal lahir
    lalu hasilnya dikonversi kedalam tahun
    """
    no_bpjs = models.CharField(max_length=15, help_text="Bila belum ada kartu, masukkan 000", default="000")
    nama_pasien = models.CharField(max_length=50, help_text="Masukkan Nama Sesuai Kartu")
    tanggal_lahir = models.DateField(help_text="Wajib diisi")
    sudah_mati = models.BooleanField(default=False, help_text="Tandai Bila Sudah Meninggal")
    tanggal_mati = models.DateField(help_text="Tanggal Meninggal", verbose_name="Tanggal Meninggal", blank=True, null=True)
    golongan_darah = models.CharField(max_length=3, blank=True, choices=GOLONGAN_DARAH_CHOICES)
    alamat = models.CharField(max_length=2, choices=KOMPLEKS_CHOICES)
    agama = models.CharField(max_length=2, choices=AGAMA_CHOICES, blank=True)
    jenis_kelamin = models.CharField(max_length=1, blank=True, choices=JENIS_KELAMIN_CHOICES)
    pekerjaan = models.CharField(choices=PEKERJAAN_CHOICES, blank=True, max_length=2)
    no_hp = models.CharField(max_length=20, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nama_pasien
    def usia(self):
        """"
        mengetahui usia dgn cara menghitung selisih antara tahun skrg dgn tahun tgl lahir \
        dirender ke kolom usia
        """
        hitung_delta = (datetime.datetime.now().year - self.tanggal_lahir.year)
        #hitung_hari = hitung_delta.days / 360
        usia_ke_str = str(hitung_delta)
        usianya = usia_ke_str + " Thn"
        return usianya
    def waktu(self):
        return datetime.date.today()

    class Meta:
        verbose_name_plural = "Data Pasien"

class Kunjungan(models.Model):
    nama_pasien = models.ForeignKey(DataPasien, on_delete=models.CASCADE)
    #rawat_jalan = models.BooleanField(default=True)
    rawat_inap = models.BooleanField(default=False)
    tanggal_kunjungan = models.DateField(help_text="Tanggal pasien berobat", verbose_name="Tgl Berobat")
    diagnosa = models.TextField(blank=True)
    tensi = models.CharField(max_length=15, help_text="mmHg", blank=True)
    berat_badan = models.CharField(max_length=8, help_text="Kilogram", blank=True)
    kadar_hb = models.CharField(max_length=8, blank=True)
    gula_darah = models.CharField(max_length=10, blank=True, help_text="Kadar gula darah sewaktu")
    kolesterol = models.CharField(max_length=10, blank=True, help_text="Kadar kolesterol total")
    asam_urat = models.CharField(max_length=10, blank=True, help_text="Kadar asam urat")
    pemeriksaan_lain = models.TextField(blank=True)
    catatan = models.TextField(blank=True, help_text="Jika ada obat racikan tulis disini, atau tulis catatan apa saja")
    obat_sudah = models.BooleanField(default=False, verbose_name="Obat Sudah ?")

    def __str__(self):
        return str(str(self.nama_pasien) + " " + str(self.tanggal_kunjungan))
    class Meta:
        verbose_name_plural = "Data Kunjungan"

class Resep(models.Model):
    nama_pasien = models.ForeignKey(Kunjungan, on_delete=models.CASCADE)
    nama_obat = models.ForeignKey(DataObat, on_delete=models.CASCADE)
    jumlah = models.PositiveSmallIntegerField()
    aturan_pakai = models.CharField(max_length=10, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.nama_obat)
    class Meta:
        verbose_name_plural = "Resep"

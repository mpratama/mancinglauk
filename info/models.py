from django.db import models

# Create your models here.
class Informasi(models.Model):
    tanggal_informasi = models.DateField(help_text="Tanggal Pengumuman Ditulis")
    judul = models.CharField(max_length=30)
    isi = models.TextField()
    def __str__(self):
        return self.judul
    class Meta:
        verbose_name_plural = "Papan Pengumuman"

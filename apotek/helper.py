from .models import DataObat
from pendaftaran.models import DataPasien
import datetime

def dumpdataobat():
    data_obat = open('./datamentah/dataobat.csv')
    for obat in data_obat:
        a = obat.replace('\n', '').split('|')
        b = DataObat(nama_obat=a[0], jumlah=a[1], tanggal_kadaluwarsa=a[2])
        b.save()
        print(a[0] + " sudah masuk")
        #print(a[0] + " " + a[1] + " " + a[2])

def dumpdatapasien():
    data_pasien = open('./datamentah/dp.csv')
    for p in data_pasien:
        a = p.replace('\n', '').split('|')
        #print(a[0] + " " + a[1].upper() + " " + a[2] + " " + a[3] + " " + a[4])
        b = DataPasien(no_bpjs=a[0], nama_pasien=a[1], tanggal_lahir=a[2], alamat=a[3], jenis_kelamin=a[4])
        b.save()
        print("%s sudah masuk" % a[1])

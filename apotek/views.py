from django.shortcuts import render
import csv
from pendaftaran.models import Resep
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

@login_required(login_url='/pendaftaran/login/')
def index(request):
    return render(request, 'apotek/index.html')

def lapgen(request):
    response = HttpResponse(content_type='text/csv')
    tanggal_awal = request.POST["tgl_awal"]
    tanggal_akhir = request.POST["tgl_akhir"]
    if request.method == "POST":
        if request.POST["jenis_laporan"] == "mentah":
            response['Content-Disposition'] = 'attachment; filename="laporan_apotek_mentah.csv"'
            wr = csv.writer(response)
            data_grabbed = Resep.objects.filter(nama_pasien__tanggal_kunjungan__range=(tanggal_awal, tanggal_akhir)).order_by('nama_pasien__tanggal_kunjungan')
            wr.writerow(("Tanggal Kunjungan", "Nama Pasien", "Diagnosa", "Nama Obat", "Jumlah", "Aturan Pakai"))
            for data in data_grabbed:
                wr.writerow((str(data.nama_pasien.tanggal_kunjungan), data.nama_pasien.nama_pasien.nama_pasien.upper(), data.nama_pasien.diagnosa, data.nama_obat.nama_obat.upper(), data.jumlah, data.aturan_pakai))
            return response
        else:
            response['Content-Disposition'] = 'attachment; filename="laporan_obat.csv"'
            x = 2
            wr = csv.writer(response)
            data_grabbed = Resep.objects.filter(nama_pasien__tanggal_kunjungan__range=(tanggal_awal, tanggal_akhir)).order_by('nama_obat__nama_obat')
            wr.writerow(("Nama Obat", "Jumlah", "Jumlah Total"))
            for data in data_grabbed:
                wr.writerow((data.nama_obat.nama_obat.upper().replace('(', '').replace(')', ''), data.jumlah, "=sumif(A2:A" + str(len(data_grabbed) + 1) +",A" + str(x) + ",B2:B" + str(len(data_grabbed) + 1) + ")"))
                x = x + 1
            return response

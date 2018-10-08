from django.contrib.admin import ModelAdmin, AdminSite, TabularInline
from .models import DataObat
from pendaftaran.models import Kunjungan
from pendaftaran.admin import ResepInline

# Register your models here.
class ApotekSite(AdminSite):
    site_header = "SIP PKM Tayando"
    site_title = "Puskesmas Perawatan Tayando Yamtel"
    index_title = "Bagian Apotek"

apotek_admin_site = ApotekSite(name="apotek_admin")


class KunjunganAdmin(ModelAdmin):
    inlines = [
        ResepInline,
    ]
    fieldsets = [
        ('Data Kunjungan', {'fields': [('nama_pasien', 'tanggal_kunjungan'), 'obat_sudah']}),
        ('Data', {'fields': [('tensi', 'berat_badan'),  'diagnosa', 'catatan'], 'classes':'collapse'}),
        ('Pemeriksaan Lab', {'fields': [('kadar_hb', 'gula_darah', 'kolesterol', 'asam_urat', 'pemeriksaan_lain')], 'classes': ('collapse',)}),
    ]
    list_display = ('nama_pasien', 'tanggal_kunjungan', 'diagnosa', 'obat_sudah')
    list_filter = ['tanggal_kunjungan']
    ordering = ['tanggal_kunjungan']
    list_per_page = 50

class DataObatAdmin(ModelAdmin):
    fieldsets = [
        ('Nama Obat, Jumlah & Satuan', {'fields': [('nama_obat','generik'), ('satuan', 'jumlah')]}),
        ('Tanggal Kadaluwarsa', {'fields': [('no_batch','tanggal_kadaluwarsa')]}),
    ]
    list_display = ('nama_obat', 'satuan', 'jumlah', 'kadaluwarsa')
    search_fields = ['nama_obat']
    ordering = ['nama_obat']
    list_filter = ['satuan', 'tanggal_kadaluwarsa']
    list_per_page = 50

apotek_admin_site.register(DataObat, DataObatAdmin)
apotek_admin_site.register(Kunjungan, KunjunganAdmin)
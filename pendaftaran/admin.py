from django.contrib import admin
from .models import DataPasien, Kunjungan, Resep
from django.contrib.auth.models import User, Group
from apotek.models import DataObat
# Register your models here.

class ResepInline(admin.TabularInline):
    model = Resep
    autocomplete_fields = ['nama_obat']

class KunjunganAdmin(admin.ModelAdmin):
    inlines = [
        ResepInline,
    ]
    fieldsets = [
        ('Data Kunjungan', {'fields': [('nama_pasien', 'tanggal_kunjungan')]}),
        ('Jenis Kunjungan', {'fields': [('rawat_inap', 'obat_sudah',)]}),
        ('Data Pemeriksaan', {'fields': [('tensi', 'berat_badan'), 'diagnosa', 'catatan']}),
        ('Pemeriksaan Lab', {'fields': [('kadar_hb', 'gula_darah', 'kolesterol', 'asam_urat', 'pemeriksaan_lain')], 'classes': ('collapse',)}),
    ]
    list_display = ('nama_pasien', 'tanggal_kunjungan', 'diagnosa', 'obat_sudah')
    list_filter = ['tanggal_kunjungan', 'rawat_inap']
    autocomplete_fields = ['nama_pasien']
    search_fields = ['diagnosa', 'nama_pasien__nama_pasien']
    ordering = ['-tanggal_kunjungan', 'nama_pasien__nama_pasien']
    list_per_page = 30
    #exclude = ('obat_sudah',)

class DataObatAdmin(admin.ModelAdmin):
    search_fields = ['nama_obat']

class DataPasienAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Data Kartu', {'fields': [('no_bpjs')]}),
        ('Detail Pasien', {'classes': ('extrapretty',),'fields': ['nama_pasien', 'tanggal_lahir', ('jenis_kelamin', 'golongan_darah'), ('alamat', 'no_hp'), 'pekerjaan', 'agama']}),
        ('Data Kematian', {'fields': [('sudah_mati', 'tanggal_mati')], 'classes': ('collapse',)}),
    ]
    list_display = ('nama_pasien', 'jenis_kelamin', 'alamat', 'usia')
    list_filter = ['alamat', 'jenis_kelamin']
    search_fields = ['nama_pasien', 'no_bpjs']
    ordering = ['nama_pasien']
    list_per_page = 20

admin.site.register(DataPasien, DataPasienAdmin)
admin.site.register(Kunjungan, KunjunganAdmin)
admin.site.register(DataObat, DataObatAdmin)
#admin.site.unregister(User)
#admin.site.unregister(Group)

admin.site.site_header = "SIP PKM Tayando"
admin.site.site_title = "Puskesmas Perawatan Tayando Yamtel"
admin.site.index_title = "Bagian Pendaftaran"

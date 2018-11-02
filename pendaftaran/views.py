from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from info.models import Informasi
# Create your views here.

def index(request):
    tahun_now = datetime.now().year
    info_list = Informasi.objects.order_by('-tanggal_informasi')[:5]
    index_context = {'tahun_sekarang': tahun_now, 'list_informasi': info_list}
    return render(request, 'pendaftaran/index.html', index_context)

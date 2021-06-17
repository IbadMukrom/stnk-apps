from django.contrib import admin
from stnk.models import Opd, Asset

class OpdAdmin(admin.ModelAdmin):
    list_display = ('nama_opd',)

class AssetAdmin(admin.ModelAdmin):
    list_display = ('opd', 'kode_barang', 'nama_barang', 'nomor_register', 'tahun_pembelian', 'pabrik', 'rangka','nomor_polisi', 'bpkb', 'harga', 'keterangan', 'aktif',)

admin.site.register(Opd, OpdAdmin)
admin.site.register(Asset, AssetAdmin)
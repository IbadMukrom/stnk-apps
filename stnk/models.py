from django.db import models

# Create your models here.

class Opd(models.Model):
    nama_opd = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nama_opd

class Asset(models.Model):
    ket_bpkb = (
        ('BPKAD','BPKAD'),
        ('HILANG','HILANG',),
        ('OPD', 'OPD',),
    )
    kon = (
        ('B', 'B'),
        ('RR', 'RR'),
        ('RB', 'RB'),
    )

    opd              = models.ForeignKey(Opd, on_delete=models.CASCADE)
    kode_barang      = models.CharField(max_length=15)
    nama_barang      = models.CharField(max_length=255)
    nama_pemegang    = models.CharField(max_length=100)
    nomor_register   = models.IntegerField()
    tahun_pembelian  = models.IntegerField()
    pabrik           = models.CharField(max_length=255)
    rangka           = models.CharField(max_length=255)
    nomor_polisi     = models.CharField(max_length=100)
    bpkb             = models.CharField(max_length=100)
    harga            = models.DecimalField(max_digits=15, decimal_places=2)
    keterangan       = models.CharField(max_length=100)
    roda             = models.IntegerField()
    bpkb_disimpan    = models.CharField(choices=ket_bpkb, max_length=100)
    pajak            = models.DateField()
    pengesahan       = models.DecimalField(max_digits=15, decimal_places=2)
    penggantian_stnk = models.DecimalField(max_digits=15, decimal_places=2)
    kondisi          = models.CharField(choices=kon, max_length=100)
    aktif            = models.BooleanField(default=False)
    masa_aktif       = models.DateField(auto_now=False)


    def __str__(self):
        return self.nama_barang


from django.db import models

class Buku(models.Model):
    judul = models.CharField(max_length=100)
    pengarang = models.CharField(max_length=50)
    penerbit = models.CharField(max_length=50)
    tahun_terbit = models.IntegerField()

class RakBuku(models.Model):
    nama = models.CharField(max_length=50)
    lokasi = models.CharField(max_length=50)

class Penerbit(models.Model):
    nama = models.CharField(max_length=50)
    alamat = models.CharField(max_length=100)
    
    def _str_(self):
         return '{}. {}'. format(self.id,self.nama)



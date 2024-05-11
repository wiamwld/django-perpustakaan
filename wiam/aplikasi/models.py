from django.db import models

class Mahasiswa(models.Model):
    npm = models.CharField(max_length=100)
    nama = models.CharField(max_length=50)
    alamat = models.TextField()
    
    def _str_(self):
         return '{}. {}'. format(self.id,self.nama)



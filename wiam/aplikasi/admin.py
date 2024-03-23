from django.contrib import admin

from .models import Buku 
admin.site.register(Buku)

from .models import RakBuku
admin.site.register(RakBuku)

from .models import Penerbit
admin.site.register(Penerbit)
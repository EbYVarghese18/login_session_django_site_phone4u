from django.contrib import admin
from .models import Phones, Tablets, Watches

# Register your models here.
admin.site.register(Phones)
admin.site.register(Tablets)
admin.site.register(Watches)
from django.contrib import admin

# Register your models here.
from coffees.models import *

admin.site.register(Coffee)
admin.site.register(OriginPlace)
admin.site.register(MainProcessing)
admin.site.register(Grinding)

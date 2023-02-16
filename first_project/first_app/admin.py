from django.contrib import admin

# Register your models here.
from first_app.models import webpage,Accessrecord,Topic

admin.site.register(webpage)
admin.site.register(Topic)
admin.site.register(Accessrecord)
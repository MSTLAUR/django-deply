from django.contrib import admin
from .models import Lead




admin.site.site_header = "Welcome to CLOUD SCHOOL Piano 🎹 "
admin.site.site_title = "CLOUD SCHOOL Piano 🎹"
admin.site.index_title = "welcome back 🕶"



admin.site.register(Lead)





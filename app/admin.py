from django.contrib import admin
from app.models import Questions, Tags, Answers
# Register your models here.
admin.site.register(Questions)
admin.site.register(Tags)
admin.site.register(Answers)
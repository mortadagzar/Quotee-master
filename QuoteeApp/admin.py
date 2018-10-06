from django.contrib import admin
from .models import users_profiles,Feedback,input_quote
# Register your models here.

admin.site.register(users_profiles)
admin.site.register(Feedback)
admin.site.register(input_quote)
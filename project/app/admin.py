from django.contrib import admin

# Register your models here.

from .models import user,post,like
admin.site.register(user)
admin.site.register(post)
admin.site.register(like)
from django.contrib import admin
from .models import useraccount,answer,User


# Register your models here.
admin.site.register(useraccount)
admin.site.register(answer)
admin.site.register(User)

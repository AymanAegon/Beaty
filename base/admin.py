from django.contrib import admin
from .models import User, Beat, Message


admin.site.register(User)
admin.site.register(Beat)
admin.site.register(Message)

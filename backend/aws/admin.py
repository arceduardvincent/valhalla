from django.contrib import admin
from .models import AccountID, InstanceID, ImageName, Region

admin.site.register(AccountID)
admin.site.register(InstanceID)
admin.site.register(ImageName)
admin.site.register(Region)


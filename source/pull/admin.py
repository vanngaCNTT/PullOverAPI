from django.contrib import admin
from .models import Categories, GenericPull, SpecificPull, Colors, PullImage
# Register your models here.

admin.site.register(Categories)
admin.site.register(GenericPull)
admin.site.register(SpecificPull)
admin.site.register(Colors)
admin.site.register(PullImage)

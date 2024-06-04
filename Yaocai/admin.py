from django.contrib import admin

# Register your models here.
from Yaocai.models import Yaocai, CategoryType

admin.site.register(Yaocai)
admin.site.register(CategoryType)
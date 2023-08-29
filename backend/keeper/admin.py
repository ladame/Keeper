from django.contrib import admin
from .models import Keeper

# Register your models here.
class KeeperAdmin(admin.ModelAdmin):
    list_display = ('title', 'note')

admin.site.register(Keeper, KeeperAdmin)

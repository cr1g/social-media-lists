from django.contrib import admin

from .models import SocialNetwork


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

from django.contrib import admin

from .models import Account, Person, PersonsCollection


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'person', 'network', 'email', 'first_name', 'last_name'
    )


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')


@admin.register(PersonsCollection)
class PersonsCollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

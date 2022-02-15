from rest_framework import serializers

from common.serializers import SocialNetworkSerializer
from .models import Account, Person, PersonsCollection


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        exclude = ('is_deleted',)

    def to_representation(self, instance):
        repr = super().to_representation(instance)

        repr['network'] = \
            SocialNetworkSerializer(instance.network).data

        if repr['avatar']:
            repr['avatar'] = \
                f'/media/{repr["avatar"].split("/media/")[-1]}'

        return repr


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        exclude = ('is_deleted',)

    def to_representation(self, instance):
        repr = super().to_representation(instance)

        accounts = instance.accounts.filter(is_deleted=False)
        serializer = AccountSerializer(accounts, many=True)
        for account in serializer.data:
            account.pop('person')

        repr['accounts'] = serializer.data

        return repr


class PersonsCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonsCollection
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)

        repr['persons'] = [{
            'id': person.id,
            'username': person.username
        } for person in instance.persons.filter(is_deleted=False)]

        return repr

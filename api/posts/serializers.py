from rest_framework import serializers

from persons.serializers import AccountSerializer, PersonSerializer
from .models import Post


class PersonsCollectionSerializer(serializers.Serializer):
    """
    PersonsCollection serializer used for 
    list/read operations for Post(s).
    """
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)


class PersonSerializer(serializers.Serializer):
    """
    Person serializer used for 
    list/read operations for Post(s).
    """
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    collections = PersonsCollectionSerializer(read_only=True, many=True)


class AccountSerializer(AccountSerializer):
    """
    Altered Account serializer used for 
    list/read operations for Post(s).
    """
    person = PersonSerializer(read_only=True)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ('is_deleted',)

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['account'] = AccountSerializer(instance.account).data
        return repr

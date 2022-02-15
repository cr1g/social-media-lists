from django.db import transaction
from rest_framework import status
from rest_framework.views import Response

from common.queryset import SoftDeletedQueryset
from common.views import BasicModelViewSet
from .models import Account, Person, PersonsCollection
from .serializers import AccountSerializer, PersonSerializer, \
    PersonsCollectionSerializer


class AccountViewSet(SoftDeletedQueryset, BasicModelViewSet):
    """
    Accounts management ViewSet.
    """
    queryset = Account.objects.all().select_related('network')
    serializer_class = AccountSerializer

    @transaction.atomic
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        posts = instance.posts.select_for_update()
        for post in posts:
            post.is_deleted = True
            post.save()

        instance.is_deleted = True
        instance.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class PersonViewSet(SoftDeletedQueryset, BasicModelViewSet):
    """
    Persons management ViewSet.
    """
    queryset = Person.objects.all() \
        .prefetch_related('accounts')
    serializer_class = PersonSerializer

    @transaction.atomic
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        accounts = instance.accounts.select_for_update()
        for account in accounts:
            posts = account.posts.select_for_update()
            for post in posts:
                post.is_deleted = True
                post.save()

            account.is_deleted = True
            account.save()

        instance.is_deleted = True
        instance.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class PersonsCollectionViewSet(BasicModelViewSet):
    """
    PersonsCollections management ViewSet.
    """
    queryset = PersonsCollection.objects.all() \
        .prefetch_related('persons')
    serializer_class = PersonsCollectionSerializer

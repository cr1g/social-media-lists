from django.db import transaction
from rest_framework import status, viewsets
from rest_framework.views import Response
from rest_framework_simplejwt.views import TokenObtainPairView, \
    TokenRefreshView

from common.queryset import SoftDeletedQueryset
from .models import SocialNetwork
from .serializers import CustomTokenObtainPairSerializer, \
    CustomTokenRefreshSerializer, SocialNetworkSerializer


class BasicModelViewSet(viewsets.ModelViewSet):
    """
    `BasicModelViewSet` is just a regular `ModelViewset`, except that
    `update()` acts like `partial_update()`.
    """

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Authentication token generator view.
    """
    serializer_class = CustomTokenObtainPairSerializer


class CustomTokenRefreshView(TokenRefreshView):
    """
    Refresh token generator view.
    """
    serializer_class = CustomTokenRefreshSerializer


class SocialNetworkViewSet(SoftDeletedQueryset, BasicModelViewSet):
    """
    SocialNetworks management ViewSet.
    """
    queryset = SocialNetwork.objects.all()
    serializer_class = SocialNetworkSerializer

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

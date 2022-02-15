from rest_framework import status
from rest_framework.views import Response

from common.queryset import SoftDeletedQueryset
from common.views import BasicModelViewSet
from .filters import PostFilterSet
from .models import Post
from .serializers import PostSerializer


class PostViewSet(SoftDeletedQueryset, BasicModelViewSet):
    """
    Posts management ViewSet.
    """
    queryset = Post.objects.all() \
        .select_related('account__person', 'account__network') \
        .prefetch_related('account__person__collections')
    serializer_class = PostSerializer
    filterset_class = PostFilterSet

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

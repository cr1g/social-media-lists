class SoftDeletedQueryset:
    """
    Override `rest_framework.generics.GenericAPIView`'s
    `get_queryset()` method in order to exclude soft deleted 
    instances through the `is_deleted` field.
    """
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

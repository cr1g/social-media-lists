from rest_framework import routers

from .views import AccountViewSet, PersonViewSet, PersonsCollectionViewSet

router = routers.SimpleRouter()
router.register('accounts', AccountViewSet, basename='accounts')
router.register('collections', PersonsCollectionViewSet, basename='collections')
router.register('persons', PersonViewSet, basename='persons')

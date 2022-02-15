from rest_framework import routers

from .views import SocialNetworkViewSet

router = routers.SimpleRouter()
router.register('social-networks', SocialNetworkViewSet, basename='social_networks')

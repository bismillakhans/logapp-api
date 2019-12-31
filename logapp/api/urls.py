from logapp.api.views import EntryViewSet, VehicleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet, base_name='vehicles')
router.register(r'entries', EntryViewSet, base_name='entries')

urlpatterns = router.urls

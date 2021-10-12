from django.urls import path, include
from coredata.views import IpViewSet, RblViewSet, UserViewSet
# from iplookup.views import IpLookupViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'ips', IpViewSet)
router.register(r'rbls', RblViewSet)
router.register(r'users', UserViewSet)
# router.register(r'iplookup', IpLookupViewSet, basename="iplookup")


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),

    #path('iplookup/', include('iplookup.urls'), name='iplookup-detail'),

]

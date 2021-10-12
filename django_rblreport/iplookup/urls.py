from django.urls import path, re_path
from iplookup import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # path('snippets/', views.snippet_list),
    # path('<int:ip>/', views.IpLookupView),
    # re_path(r'^(?P<ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})/$',
    #         views.IpLookupView),
    # re_path(r'^(?P<ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})/$',
    #         views.IpLookupViewSet),
    re_path(r'^(?P<ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})/$',
            views.IpLookupView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

from django.urls import path
from .views import validate_license,activate_license,usage_statistics

urlpatterns=[
    path('validate_license/', validate_license, name='validate_license'),
    path('activate_license/', activate_license, name='activate_license'),
    path('usage_statistics/', usage_statistics, name='usage_statistics'),
]

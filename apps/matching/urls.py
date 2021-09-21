from django.urls import path

from apps.matching.views import *

urlpatterns = [
    path('', Matching.as_view(), name=Matching.name),
]
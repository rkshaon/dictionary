from django.urls import path

from configure_api.views import LanguageListCreateView


urlpatterns = [
    path('languages', LanguageListCreateView.as_view()),
]
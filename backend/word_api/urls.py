from django.urls import path

from word_api.views import WordListCreateView



urlpatterns = [
    path('', WordListCreateView.as_view()),
]
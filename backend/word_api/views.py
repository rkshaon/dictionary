from rest_framework import generics

from word_api.models import Word

from word_api.serializers import WordSerializer



class WordListCreateView(generics.ListCreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
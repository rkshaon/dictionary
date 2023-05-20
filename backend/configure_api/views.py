from rest_framework import generics

from configure_api.models import Language

from configure_api.serializers import LanguageSerializer



class LanguageListCreateView(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
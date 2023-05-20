from rest_framework import serializers

from configure_api.models import Language



class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'
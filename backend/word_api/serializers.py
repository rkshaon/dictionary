from rest_framework import serializers

from word_api.models import Word



class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'
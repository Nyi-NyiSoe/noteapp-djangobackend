import rest_framework.serializers as serializers
from .models import *

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


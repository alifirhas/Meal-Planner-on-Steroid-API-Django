from rest_framework import serializers
from base.models import TingkatAktivitas

class TingkatAktivitasSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TingkatAktivitas
        fields = ['name', 'nilai', 'gender']
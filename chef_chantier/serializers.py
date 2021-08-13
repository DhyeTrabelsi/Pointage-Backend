from chef_chantier.models import *
from rest_framework import serializers 

class chef_chantierSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = chef_chantier
        fields = ('id',
                  'nom',
                  'prenom',
                  'cin',
                  'login',
                  'password')
class missionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = mission
        fields = ('id',
                  'description',
                  'date_debut',
                  'date_fin',
                  'lieu',
                  'état',
                  'User')

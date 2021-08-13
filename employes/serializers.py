from rest_framework import serializers 
from employes.models import *
 
 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id',
                  'first_name',
                  'last_name',
                  'cin',
                  'username',
                  'password',
                  'codeQR',
                  'poste',
                  'image',
                  'email',
                  'telephone',
                  'is_superuser',
                  'is_staff']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class pointageSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = pointage
        fields = ('id',
                  'entre',
                  'sortie',
                  'retard',
                  'absance',
                  'user')


class salaireSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = salaire
        fields = ('id',
                  'mois',
                  'heurs_base',
                  'heurs_sup',
                  'primes',
                  'total',
                  'user')


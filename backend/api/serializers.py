from django.contrib.auth.models import User
from rest_framework import serializers

# Serializer to define User Api representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [ 'url', 'username', 'email', 'is_staff' ]
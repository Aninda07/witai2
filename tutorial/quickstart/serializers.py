
from rest_framework import serializers
from .models import Contact
from .models import Montact


class ContactSerializer(serializers.ModelSerializer):
    #Utterences = serializers.CharField(max_length=100)
    #Intent = serializers.CharField(max_length=200)
    #Entity = serializers.CharField(max_length=200)
    #Traits = serializers.CharField(max_length=200)

    class Meta:
        model = Contact
        fields = ('Utterance', 'Entities', 'Traits', 'Shrug', 'Details')


class MontactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Montact
        fields = ('Chat', 'Intent', 'Sender_ID',)




















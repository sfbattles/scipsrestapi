from rest_framework import serializers
from .models import Agent


class AgentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Agent
        fields = ('id', 'url', 'agent_no', 'name','address',
                'city','state','zipcode','status')
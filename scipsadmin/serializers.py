from rest_framework import serializers
from .models import Agent, AgentMaster, PhoneType,
                    AgentAddress, AgentEmail


class AgentSerializer(serializers.ModelSerializer)
    class Meta:
        model = Agent
        fields = ('id','agent_no', 'name','address',
                'city','state','zipcode','status')
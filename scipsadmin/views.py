from django.shortcuts import render
from rest_framework import viewsets
from . models import Agent
from . serializers import AgentSerializer

class AgentView(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


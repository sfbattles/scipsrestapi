from django.contrib import admin
from .models import Agent
from .models import PhoneType
from .models import AgentPhone
from .models import AgentMaster
from .models import AgentEmail

# Register your models here.
admin.site.register(Agent)
admin.site.register(PhoneType)
admin.site.register(AgentPhone)
admin.site.register(AgentMaster)
admin.site.register(AgentEmail)


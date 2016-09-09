from django.contrib import admin
from .models import GASite, UKSite, ALPHASite, APACSite

admin.site.register(ALPHASite)
admin.site.register(GASite)
admin.site.register(UKSite)
admin.site.register(APACSite)


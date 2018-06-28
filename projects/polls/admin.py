# from django.contrib import admin

# from .models import *

# admin.site.register(Question)

# admin.site.register(Choice)

# admin.site.register(LastVoter)


from django.contrib import admin
from django.apps import apps

app = apps.get_app_config('polls')

for model_name, model in app.models.items():
    admin.site.register(model)
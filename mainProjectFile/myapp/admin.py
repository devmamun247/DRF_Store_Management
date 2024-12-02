from django.contrib import admin

# Register your models here.

from .models import *    # here all models are imported
# from .models import Model  # here specifique  model imported

admin.site.register(Model)
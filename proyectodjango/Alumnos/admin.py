from django.contrib import admin

# Register your models here.
from .models import Materia
admin.site.register(Materia)

from .models import Alumno
admin.site.register(Alumno)
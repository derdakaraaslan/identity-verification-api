from django.contrib import admin
from .models import Identity, Process, Face

# Register your models here.
@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ['id', 'started_at', 'finished_at', 'avg_distance']

@admin.register(Identity)
class IdentityAdmin(admin.ModelAdmin):
    pass



@admin.register(Face)
class FaceAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'process_id', 'distance']
from django.contrib import admin
from common.models import Lines


@admin.register(Lines)
class LinesAdmin(admin.ModelAdmin):
    list_display = ['contest',]
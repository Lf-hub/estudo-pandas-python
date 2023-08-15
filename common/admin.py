from django.contrib import admin
from common.models import Lines, Summary


@admin.register(Lines)
class LinesAdmin(admin.ModelAdmin):
    list_display = ['contest',]

admin.site.register(Summary)

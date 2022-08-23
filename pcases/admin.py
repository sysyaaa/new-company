from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe


@admin.register(models.PrevCases)
class PrevCasesAdmin(admin.ModelAdmin):

    list_per_page: int = 10

    list_display = (
        "subject",
        "content",
        "create_date",
        "image",
    )

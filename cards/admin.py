from django.contrib import admin

from cards.models import DiscountCard


@admin.register(DiscountCard)
class DiscountCardAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "phone",
        "discount_percent",
        "bonus_points",
        "created_at",
        "last_used_at",
    )

from django.db import models


class DiscountCard(models.Model):
    """Дисконтна картка постійного клієнта."""

    phone = models.CharField("Номер телефону", max_length=20)
    full_name = models.CharField("Повне ім'я власника", max_length=200)
    discount_percent = models.PositiveSmallIntegerField("Відсоток знижки")
    bonus_points = models.PositiveIntegerField("Накопичені бонуси", default=0)
    created_at = models.DateTimeField("Дата створення", auto_now_add=True)
    last_used_at = models.DateTimeField(
        "Дата останнього використання", null=True, blank=True
    )

    class Meta:
        verbose_name = "Дисконтна картка"
        verbose_name_plural = "Дисконтні картки"

    def __str__(self):
        return f"{self.full_name} ({self.phone}) — {self.discount_percent}%"

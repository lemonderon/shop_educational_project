from datetime import timedelta

from django.db import models
from django.utils import timezone

ACTIVE_PERIOD = timedelta(days=183)

class DiscountCardQuerySet(models.QuerySet):
    def active(self):
        return self.filter(last_used_at__gte=timezone.now() - ACTIVE_PERIOD)

class DiscountCard(models.Model):
    """Дисконтна картка постійного клієнта."""

    phone = models.CharField("Номер телефону", max_length=20, unique=True)
    last_used_at = models.DateTimeField(
        "Дата останнього використання", null=True, blank=True, db_index=True
    )
    first_name = models.CharField("Ім'я", max_length=100, default="")
    last_name = models.CharField("Прізвище", max_length=100, default="")
    discount_percent = models.PositiveSmallIntegerField("Відсоток знижки")
    bonus_points = models.PositiveIntegerField("Накопичені бонуси", default=0)
    created_at = models.DateTimeField("Дата створення", auto_now_add=True)
    objects = DiscountCardQuerySet.as_manager()

    class Meta:
        verbose_name = "Дисконтна картка"
        verbose_name_plural = "Дисконтні картки"

    def __str__(self):
        return f"{self.full_name} ({self.phone}) — {self.discount_percent}%"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

    @property
    def is_active(self):
        if self.last_used_at is None:
            return False
        return self.last_used_at >= timezone.now() - ACTIVE_PERIOD

import re

from django.db import migrations


def normalize_phone(raw):
    digits = re.sub(r"\D", "", raw)  # лишаємо тільки цифри
    if len(digits) == 12 and digits.startswith("380"):  # +380671234567
        return "+" + digits
    if len(digits) == 10 and digits.startswith("0"):  # 0671234567
        return "+38" + digits
    if len(digits) == 9:  # 671234567
        return "+380" + digits
    raise ValueError(f"Не вдалося розпізнати номер: {raw!r}")


def normalize_phones(apps, schema_editor):
    DiscountCard = apps.get_model("cards", "DiscountCard")

    # 1. Нормалізуємо всі номери
    for card in DiscountCard.objects.all():
        card.phone = normalize_phone(card.phone)
        card.save(update_fields=["phone"])

    # 2. Об'єднуємо картки з однаковим номером
    phones = (
        DiscountCard.objects.values_list("phone", flat=True)
        .order_by("phone")
        .distinct()
    )
    for phone in list(phones):
        cards = list(DiscountCard.objects.filter(phone=phone).order_by("created_at"))
        if len(cards) < 2:
            continue
        main, *duplicates = cards  # лишаємо найстарішу картку
        for dup in duplicates:
            main.bonus_points += dup.bonus_points
            main.discount_percent = max(main.discount_percent, dup.discount_percent)
            if dup.last_used_at and (
                main.last_used_at is None or dup.last_used_at > main.last_used_at
            ):
                main.last_used_at = dup.last_used_at
            dup.delete()
        main.save()


class Migration(migrations.Migration):
    dependencies = [
        ("cards", "0005_remove_full_name"),
    ]

    operations = [
        migrations.RunPython(normalize_phones, migrations.RunPython.noop),
    ]

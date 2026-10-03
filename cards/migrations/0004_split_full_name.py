from django.db import migrations


def split_full_name(apps, schema_editor):
    DiscountCard = apps.get_model("cards", "DiscountCard")
    for card in DiscountCard.objects.all():
        parts = card.full_name.strip().title().split(maxsplit=1)
        card.first_name = parts[0] if parts else ""
        card.last_name = parts[1] if len(parts) > 1 else ""
        card.save(update_fields=["first_name", "last_name"])

def join_full_name(apps, schema_editor):
    DiscountCard = apps.get_model("cards", "DiscountCard")
    for card in DiscountCard.objects.all():
        card.full_name = f"{card.first_name} {card.last_name}".strip()
        card.save(update_fields=["full_name"])


class Migration(migrations.Migration):
    dependencies = [
        ("cards", "0003_add_first_last_name"),
    ]

    operations = [
        migrations.RunPython(split_full_name, join_full_name),
    ]

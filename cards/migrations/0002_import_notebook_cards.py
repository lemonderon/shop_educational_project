from django.db import migrations

CARDS_SQL = """
INSERT INTO cards_discountcard
    (full_name, phone, discount_percent, bonus_points, created_at, last_used_at)
VALUES
    ('Ольга Коваленко', '067 123 45 67', 5, 120,
     '2025-03-14 10:00:00', '2026-08-30 12:00:00'),
    ('Петренко Іван', '+380501112233', 10, 450,
     '2024-11-02 10:00:00', '2026-09-20 12:00:00'),
    ('марія шевчук', '(093)555-44-33', 3, 0,
     '2026-01-10 10:00:00', '2026-01-10 12:00:00'),
    ('Андрій Бондар', '0661234567', 7, 80,
     '2025-06-01 10:00:00', '2025-12-24 12:00:00'),
    ('Коваленко Ольга', '+380671234567', 5, 30,
     '2026-05-05 10:00:00', '2026-06-15 12:00:00'),
    ('Тарас Мельник-Шевченко', '097 000 11 22', 15, 1200,
     '2023-09-01 10:00:00', '2026-09-25 12:00:00');
"""


class Migration(migrations.Migration):
    dependencies = [
        ("cards", "0001_initial"),
    ]

    operations = [
        migrations.RunSQL(CARDS_SQL, migrations.RunSQL.noop),
    ]

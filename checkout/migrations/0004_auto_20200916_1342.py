# Generated by Django 3.0.6 on 2020-09-16 16:42

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_order_orderitem'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='order',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
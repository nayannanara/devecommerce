# Generated by Django 3.0.6 on 2020-08-20 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_delete_contato'),
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together={('cart_key', 'product')},
        ),
    ]
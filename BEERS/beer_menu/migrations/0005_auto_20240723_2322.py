# Generated by Django 2.2.19 on 2024-07-23 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beer_menu', '0004_auto_20240723_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='alcohol',
            field=models.TextField(verbose_name='Алкоголь в %'),
        ),
    ]
# Generated by Django 5.0.3 on 2024-04-24 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitters', '0006_rename_status_sitter_duty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitter',
            name='date_admitted',
            field=models.DateField(),
        ),
    ]

# Generated by Django 5.0.3 on 2024-04-22 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitters', '0003_alter_sitter_dateadmited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitter',
            name='dateAdmited',
            field=models.DateTimeField(),
        ),
    ]

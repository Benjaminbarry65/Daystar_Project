# Generated by Django 5.0.3 on 2024-04-23 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitters', '0004_alter_sitter_dateadmited'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sitter',
            old_name='dateAdmited',
            new_name='date_admitted',
        ),
        migrations.RenameField(
            model_name='sitter',
            old_name='Gender',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='sitter',
            old_name='Name',
            new_name='name',
        ),
    ]

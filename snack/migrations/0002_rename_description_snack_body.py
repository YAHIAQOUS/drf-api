# Generated by Django 3.2.7 on 2021-09-05 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snack', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snack',
            old_name='description',
            new_name='body',
        ),
    ]

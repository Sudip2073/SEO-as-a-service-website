# Generated by Django 4.0.3 on 2022-04-24 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competitors', '0011_rename_name_compare_names'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compare',
            old_name='names',
            new_name='Compare_name',
        ),
    ]

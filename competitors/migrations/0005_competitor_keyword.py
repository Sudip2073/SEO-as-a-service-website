# Generated by Django 4.0.3 on 2022-04-13 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitors', '0004_remove_competitor_keyword'),
    ]

    operations = [
        migrations.AddField(
            model_name='competitor',
            name='Keyword',
            field=models.TextField(blank=True),
        ),
    ]

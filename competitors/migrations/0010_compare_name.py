# Generated by Django 4.0.3 on 2022-04-24 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitors', '0009_compare'),
    ]

    operations = [
        migrations.AddField(
            model_name='compare',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

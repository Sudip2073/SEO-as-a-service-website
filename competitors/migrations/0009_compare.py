# Generated by Django 4.0.3 on 2022-04-24 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitors', '0008_key_competename'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Link', models.CharField(max_length=100, null=True)),
                ('Domain_trust', models.IntegerField(blank=True)),
                ('Domain_Citation', models.IntegerField(blank=True)),
                ('Page', models.IntegerField(blank=True)),
                ('Domain_Authority', models.IntegerField(blank=True)),
                ('Total_backlinks', models.IntegerField(blank=True)),
                ('Linking_domains', models.IntegerField(blank=True)),
                ('Primary_Topic', models.CharField(max_length=100)),
                ('Primary_Topical_trust_flow', models.IntegerField(blank=True)),
                ('Linking_subnets', models.IntegerField(blank=True)),
                ('Linking_IP_address', models.IntegerField(blank=True)),
                ('Governmental_refdomains', models.IntegerField(blank=True)),
                ('Backlinks', models.IntegerField(blank=True)),
                ('Educational_domains', models.IntegerField(blank=True)),
                ('Backlink_Educational', models.IntegerField(blank=True)),
                ('Organic_Search', models.IntegerField(blank=True)),
                ('Alexa_Rank', models.IntegerField(blank=True)),
                ('Nepal_Rank', models.IntegerField(blank=True)),
            ],
        ),
    ]

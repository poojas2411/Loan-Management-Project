# Generated by Django 4.2.1 on 2023-05-28 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_usefull_links'),
    ]

    operations = [
        migrations.CreateModel(
            name='What_we_offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Heading', models.CharField(max_length=50, null=True)),
                ('sub_heading', models.TextField(null=True)),
            ],
        ),
    ]

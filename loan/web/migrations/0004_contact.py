# Generated by Django 4.2.1 on 2023-05-28 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_car_loan_money_home_loan_money_userinfo_money'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('message', models.TextField(null=True)),
            ],
        ),
    ]

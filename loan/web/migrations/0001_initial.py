# Generated by Django 4.2.1 on 2023-05-26 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car_loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_type', models.CharField(max_length=50)),
                ('Bank_name', models.CharField(max_length=50)),
                ('Account_number', models.BigIntegerField()),
                ('Bank_ifsc', models.CharField(max_length=50)),
                ('Aadhaar_no', models.CharField(max_length=50)),
                ('pancard_number', models.CharField(max_length=50)),
                ('Address', models.TextField(max_length=100)),
                ('phone_no', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Home_loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_type', models.CharField(max_length=50)),
                ('Bank_name', models.CharField(max_length=50)),
                ('Account_number', models.BigIntegerField()),
                ('Bank_ifsc', models.CharField(max_length=50)),
                ('Aadhaar_no', models.CharField(max_length=50)),
                ('pancard_number', models.CharField(max_length=50)),
                ('Address', models.TextField(max_length=100)),
                ('phone_no', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='userinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_type', models.CharField(max_length=50)),
                ('Bank_name', models.CharField(max_length=50)),
                ('Account_number', models.BigIntegerField()),
                ('Bank_ifsc', models.CharField(max_length=50)),
                ('Aadhaar_no', models.CharField(max_length=50)),
                ('pancard_number', models.CharField(max_length=50)),
                ('Address', models.TextField(max_length=100)),
                ('phone_no', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]

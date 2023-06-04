# Generated by Django 4.2.1 on 2023-05-26 15:54

from django.db import migrations, models
import django_enumfield.db.fields
import web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car_loan',
            name='status',
            field=django_enumfield.db.fields.EnumField(default=1, enum=web.models.status_enum),
        ),
        migrations.AddField(
            model_name='home_loan',
            name='status',
            field=django_enumfield.db.fields.EnumField(default=1, enum=web.models.status_enum),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='status',
            field=django_enumfield.db.fields.EnumField(default=1, enum=web.models.status_enum),
        ),
        migrations.AlterField(
            model_name='car_loan',
            name='Aadhaar_no',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='car_loan',
            name='Account_number',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='car_loan',
            name='Address',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='car_loan',
            name='Bank_ifsc',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='car_loan',
            name='Bank_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='car_loan',
            name='Email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='car_loan',
            name='loan_type',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='car_loan',
            name='pancard_number',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='car_loan',
            name='phone_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='home_loan',
            name='Aadhaar_no',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='home_loan',
            name='Account_number',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='home_loan',
            name='Address',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='home_loan',
            name='Bank_ifsc',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='home_loan',
            name='Bank_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='home_loan',
            name='Email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='home_loan',
            name='loan_type',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='home_loan',
            name='pancard_number',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='home_loan',
            name='phone_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='Aadhaar_no',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='Account_number',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='Address',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='Bank_ifsc',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='Bank_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='Email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='loan_type',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='pancard_number',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='phone_no',
            field=models.IntegerField(null=True),
        ),
    ]

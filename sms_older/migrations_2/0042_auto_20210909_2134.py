# Generated by Django 3.1.5 on 2021-09-09 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0041_remove_customer_sender_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='created_at',
        ),
        migrations.AddField(
            model_name='customer',
            name='sender_Id',
            field=models.CharField(default='ROBERMS', max_length=11),
        ),
    ]

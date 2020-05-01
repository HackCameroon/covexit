# Generated by Django 2.2.12 on 2020-05-01 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_rename_waitinglist_to_mailinglist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='zip_and_city',
        ),
        migrations.AddField(
            model_name='useraccount',
            name='city',
            field=models.CharField(default='', max_length=200, verbose_name='City'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useraccount',
            name='postcode',
            field=models.CharField(default='', max_length=20, verbose_name='Postcode'),
            preserve_default=False,
        ),
    ]
